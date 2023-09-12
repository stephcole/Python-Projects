from abc import ABC, abstractmethod
class carnival(ABC):
    def rides(self, amount):
        print("Your {} tickets are enough for admission on 6 rides!".format(amount))
    def tickets(self, amount):
        pass

class snacks(carnival):
    def tickets(self, amount):
        print("You are able to purchase popcorn, candy, and 2 sodas with you {} tickets!".format(amount))

obj = snacks()
obj.rides("24")
obj.tickets("24")
