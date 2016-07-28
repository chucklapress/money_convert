class Money:
    def __init__(self, abrv, val):
        self.abrv = abrv
        self.val = val



    def __str__(self):
        return "{}, {}".format(self.abrv, self.val)

    def __eq__(self,other):
        return "{}, {}".format(self.abrv, self.val) == "{}, {}".format(self.abrv, self.val)

    def __ne__(self, other):
        return "{}, {}".format(self.abrv, self.val) != "{}, {}".format(self.abrv, self.val)

    def __le__(self, other):
        return "{}, {}".format(self.abrv, self.val) <= "{}, {}".format(self.abrv, self.val)

    def __lt__(self, other):
        return "{}, {}".format(self.abrv, self.val) < "{}, {}".format(self.abrv, self.val)

    def __gt__(self, other):
        return "{}, {}".format(self.abrv, self.val) > "{}, {}".format(self.abrv, self.val)

    def __ge__(self, other):
        return "{}, {}".format(self.abrv, self.val) >= "{}, {}".format(self.abrv, self.val)

    def __mul__(self, other):
        return Money((self.val * other.val), self.currency)

    #def __add__(self, other):
       #return Money.self.val + other.val

    def __add__(self, other):
        return Money((self.val + other.val), self.currency)


    def __sub__(self, other):
        return Money((self.val - other.val), self.currency)


    def currency(self):
        if self.abrv == "USD":
            return self.val * 1

        elif self.abrv == "JPY":
            return self.val * 0.0090

        elif self.abrv == "EUR":
            return self.val * 1.11

        elif self.abrv == "BTC":
            return self.val * 532.50




money = Money("JPY", 1)

print(money.currency())

one_amount = Money("USD",50).currency()

other_amount = Money("BTC",40).currency()

print(other_amount + one_amount)

print(one_amount * other_amount)

print(one_amount)

print(other_amount)

print(one_amount <= other_amount)

print(one_amount >= other_amount)

print(one_amount != other_amount)

print(one_amount == other_amount)

print(one_amount - other_amount)

print(one_amount + one_amount)
