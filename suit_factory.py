from hemlock import Hemlock
from relic import Relic
from dragon import Dragon
from coral import Coral

class SuitFactory(suit):
    try:
        if suit == "HEMLOCK":
            return Hemlock()
        elif suit == "RELIC":
            return Relic()
        elif suit == "CORAL":
            return Coral()
        elif suit == "DRAGON":
            return Dragon()
        raise AssertionError("Suit is not valid.")
    except AssertionError as e:
        print(e)
