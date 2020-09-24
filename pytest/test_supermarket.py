import pytest

class Checkout:

    class Discount:
        def __init__(self, quantity, price):
            self.quantity = quantity
            self.price = price

    def __init__(self):
        self.prices = {}
        self.items = {}
        self.discounts = {}

    def addPrice(self, item, price):
        self.prices[item] = price
    
    def addItem(self, item):
        if item not in self.prices:
            raise Exception('Bad Item')
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def calculateTotal(self):
        total = 0
        for item, cnt in self.items.items():
           total += self.calculateItem(item, cnt)
        return total
    
    def calculateItem(self, item, cnt):
        total = 0
        if item in self.discounts:
            discount = self.discounts[item]
            if cnt >= discount.quantity:
                total += self.calculateItemDiscountedTotal(item, cnt, discount)
            else:
                total += self.prices[item] * cnt
        else:
            total += self.prices[item] * cnt
        return total

    def calculateItemDiscountedTotal(self, item, cnt, discount):
        total = 0
        noOfDiscounts = cnt/discount.quantity
        total += noOfDiscounts * discount.price
        remaining = cnt % noOfDiscounts
        total += remaining * self.prices[item]
        return total

    def addDiscount(self, item, quantity, price):
        discount = self.Discount(quantity, price)
        self.discounts[item] = discount


@pytest.fixture()
def checkout():
    checkout = Checkout()
    checkout.addPrice('ball', 1)
    checkout.addPrice('guitar', 2)
    checkout.addPrice('violin', 3)
    return checkout

def test_canCalculateTotal(checkout):
    checkout.addItem('ball')
    assert checkout.calculateTotal() == 1

def test_canAddMultipleItems(checkout):
    checkout.addItem('ball')
    checkout.addItem('guitar')
    checkout.addItem('violin')
    assert checkout.calculateTotal() == 6

def test_canAddDiscount(checkout):
    checkout.addDiscount('ball', 3, 2)

#@pytest.mark.skip # doesn't test the below code snippet
def test_canApplyDiscountRule(checkout):
    checkout.addDiscount('ball', 3, 2)
    checkout.addItem('ball')
    checkout.addItem('ball')
    checkout.addItem('ball')
    assert checkout.calculateTotal() == 2

def test_ExceptionWithBadItem(checkout):
    with pytest.raises(Exception):
        checkout.addItem('c')