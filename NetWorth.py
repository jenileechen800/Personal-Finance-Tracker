from Data.Assets import Assets
from Data.Liabilities import Liabilities


class Net_Worth:
    def __init__(self):
        self.assets = Assets()
        self.liabilities = Liabilities()

    def net_worth(self):
        return self.assets - self.liabilities


