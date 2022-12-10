
from time import sleep,time
from threading import Thread, Event
from collections import namedtuple



class TimeScalers( 
        namedtuple( "TimeScalers", 
        [ "secs_min", "mins_hr", "hrs_day", "days_wk", "wks_mn", "mns_season", "seasons_yr" ]
        )):
    __slots__ = ()

    def days_per_month(self) :
        return self.days_wk * self.wks_mn 
    def days_per_season(self) :
        return self.days_per_month() * self.mns_season
    def days_per_year(self) : 
        return self.days_per_season() * self.seasons_yr


class TimeOfDay( namedtuple( "TimeOfDay", ["minute", "hour"], defaults=[0,0] ) ):
    __slots__ = ()

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}"

class Calendar( namedtuple( "Calendar", [ "day", "month", "year", "week", "season"], defaults=[1,1,1100,1,1] )):
    __slots__ = ()
    def __str__(self):
        return f"{self.month:02d}/{self.day:02d}/{self.year} week:{self.week} season:{self.season}"


class TimeKeeper(Thread):
    active_timers = {}

    @classmethod
    def get(cls,name):
        return cls.active_timers.get(name)

    def __init__(self, scaling_vals, reg_name=None):
        self._reg_name = reg_name
        if self._reg_name:
            self.active_timers[self._reg_name]=self
        self._exitflag = False
        self._timeScaleBy = TimeScalers( *scaling_vals )
        # XXX there's a wierd one off issue when the fields first roll in check_for_roll,
        #  probably something obvious but moving on, workaround is force everything to roll on the first check
        self._timeScaleCnts = [max(self._timeScaleBy)] * len(self._timeScaleBy) 
        self._cur_time = TimeOfDay()    
        self._cur_date = Calendar()
        super().__init__()

    # __enter__, __exit__ for context manager support
    def __enter__(self):
        self.start()
        return self

    def __exit__(self,exc_type,exc_value,exe_tb):
        self.shutdown()

    def shutdown(self):
        if (self._reg_name and self._reg_name in self.active_timers):
            del self.active_timers[self._reg_name]
        self.flagstop()
        if (self.is_alive()): self.join()

    def flagstop(self):
        self._exitflag = True

    def heart_beat(self,secs=1.0):
        t = time()
        while not self._exitflag:
            curTime = time()
            t = min(t,time()) + secs   # min() to guard against system time moving backward
            yield max(t-time(),0)      

    def run(self):
        hb = self.heart_beat()
        while True:
            sleep(next(hb))
            if (self._exitflag):
                break;
            curvals = [self._cur_time, self._cur_date]
            if (self.check_for_roll(0, curvals)):
                self._cur_time = curvals[0]
                self._cur_date = curvals[1]
                print( f"{self._cur_time} {self._cur_date} {time()}" )

    def check_for_roll(self, i, time_date):
        self._timeScaleCnts[i] += 1
        if self._timeScaleCnts[i] < self._timeScaleBy[i]:
            return i
        self._timeScaleCnts[i] = 0
        getattr(self, "_"+self._timeScaleBy._fields[i])(time_date)
        return self.check_for_roll(i+1, time_date) if (i+1 < len(self._timeScaleBy)) else i

    def _secs_min(self, time_date):
        day_time = time_date[0]
        time_date[0] = day_time._replace( minute = day_time.minute+1 )

    def _mins_hr(self, time_date):
        day_time = time_date[0]
        time_date[0] = day_time._replace( minute = 0, hour = day_time.hour+1 )

    def _hrs_day(self, time_date):
        day_time = time_date[0]
        time_date[0] = day_time._replace( minute = 0, hour = 0 )
        cal_vals = time_date[1]
        time_date[1] = cal_vals._replace( day = cal_vals.day+1 )

    def _days_wk(self, time_date):
        cal_vals = time_date[1]
        time_date[1] = cal_vals._replace( week = cal_vals.week+1 )

    def _wks_mn(self, time_date):
        cal_vals = time_date[1]
        time_date[1] = cal_vals._replace( day = 1, month = cal_vals.month+1 )

    def _mns_season(self, time_date):
        cal_vals = time_date[1]
        time_date[1] = cal_vals._replace( season = cal_vals.season+1 )

    def _seasons_yr(self, time_date):
        cal_vals = time_date[1]
        time_date[1] = cal_vals._replace( month = 1, week = 1, season = 1, year = (cal_vals.year+1)%10000 )


if __name__ == '__main__':
    """
    # move into unit test
    TimeKeeper( ( 2, 2, 2, 2, 2, 2, 4 ),"MyTimer" )
    print(f"active_timers: {TimeKeeper.active_timers}")
    TimeKeeper.get("MyTimer").start()
    sleep(4)
    TimeKeeper.get("MyTimer").shutdown()
    print(f"active_timers after shutdown: {TimeKeeper.active_timers}")
    chk = TimeKeeper.get("Named")
    """
    with TimeKeeper( ( 1, 2, 2, 2, 2, 2, 2 ),"MyTimer"  ) as tk:
        for _ in range( 1, 150 ): 
            sleep(1)
        

