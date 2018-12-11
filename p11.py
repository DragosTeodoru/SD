class CashRegister : 
    # The objects is defined inside the constructor with Pirce and count number
    def __init__(self) : 
        self._itemCount = 0 
        self._totalPrice = 0.0
    # The price is added to the previous item's price and the count is rised by 1 every items is added
    def addItem(self, price) : 
        self._itemCount = self._itemCount + 1 
        self._totalPrice = self._totalPrice + price 
    # Calling the total price of the item
    
    def getTotal(self) :
        return self._totalPrice 
    # Calling the number of objects added
    def getCount(self) : 
        return self._itemCount 
    # Resets everything
    def clear(self) : 
        self._itemCount = 0 
        self._totalPrice = 0.0
    #Task 3.c
    def getPounds(self):
        print((int(self._totalPrice)),"£")
      
    
#Task 3.b
register1 = CashRegister()
register1.addItem(0.90) 
register1.addItem(0.95) 
register2 = CashRegister() 
register2.addItem(1.90)

print ("number of items: ",register1._itemCount)
print ("Total: ",register1._totalPrice)
print ("number of items: ",register2._itemCount)
print ("Total: ",register2._totalPrice)
#Task 3.c
register1.getPounds()
register2.getPounds()   
