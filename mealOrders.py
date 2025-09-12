def makeEmptyOrder():
    return ()

def add_burgerToOrder(order,burger):
    return order + (burger,)

def printReciept(order):
    return None

def removeOrder(order):
    return ()

def enoughMoney(order,moneyInMyPocket):
    return False


myOrder = makeEmptyOrder()
myOrder = add_burgerToOrder(myOrder,'BVPB')
myOrder = add_burgerToOrder(myOrder,'BCPCPB')
