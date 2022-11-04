class Suit():
    def __init__(self):
        self._descriptors = None

    @staticmethod
    def suit_factory(suit):
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
