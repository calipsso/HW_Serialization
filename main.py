class UserPlayer:
    def __init__(self, name):
        self.name = name
        self.__wallet = 100
    def updateWallet(self, coins):
        self.__wallet = self.__wallet + coins
    def showWallet(self):
        print(f"U have{self.__wallet} coins now")

class WalletFunctor:
    def __init__(self, startCoins=100):
        self.__startCoins = startCoins
    #def __call__(self, 0):


user1 = UserPlayer("Joe")
user1.updateWallet(50)
user1.showWallet()

