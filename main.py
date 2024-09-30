class Bikeshop():
    def __init__(self,stock):
        self.stock = stock
    def ShowBike(self):
        print("Total bikes :",self.stock)
    def DisplayQuan(self,Q):
        if(Q<0):
            print("Print the valid quantity")
        elif(Q>self.stock):
            print("Quantity bikes are not availabe")
        else:
            print("Total price: ",Q*100)
            print("Availabe Quantity",self.stock-Q)

while True:
    obj = Bikeshop(100)
    userChoice = int(input("""""
        1. Display Bike
        2. Rent a Bike
        3. Exit
    """))
    if(userChoice == 1):
        obj.ShowBike()
    elif(userChoice == 2):
        n = int(input("Enter the quantity :---"))
        obj.DisplayQuan(n)
    else:
        break
