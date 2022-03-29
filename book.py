
class Book :
    bookName=""
    listBook=[]
    
    def __init__(self, bookName):
        self.bookName=bookName
    
    
    def insert_buy(self,quantity, price):
        id=len(Book.listBook)+1
        typeAction="BUY"
        ordername=Order(typeAction,quantity,price,id)
        print(f"--- Insert {ordername} on {self.bookName}")
        Book.listBook.append(ordername)
        Book.Interface(self)
        
    
    
    
    def insert_sell(self,quantity, price):
        id=len(Book.listBook)+1
        typeAction="SELL"
        
        ordername=Order(typeAction,quantity,price,id)
        print(f"--- Insert {ordername} on {self.bookName}")
        
        quantity=Book.ComparareExActions(self,quantity,price)
        
        ordername=Order(typeAction,quantity,price,id)
        Book.listBook.append(ordername)
        
        Book.Interface(self)
    
    
    
    
    
    def Interface(self):
        Book.listBook=Book.TriList(self)
        print(f"Book on {self.bookName}")
        
        for i in range(len(Book.listBook)):
            if (Book.listBook[i].quantity!=0):
                
                print(f"     {str(Book.listBook[i])}")
                
        print("--------------------------------------------\n")
        
    
    
    def TriList(self):
        listSell=[]
        listBuy=[]
        
        for i in range(len(self.listBook)):
            if(self.listBook[i].typeAction =="SELL"):
                listSell.append(self.listBook[i])
            else:
                listBuy.append(self.listBook[i])
        self.listBook=[]
        
        listSell.sort(key=lambda Book : Book.price,reverse=True)
        listBuy.sort(key=lambda Book : Book.price,reverse=True)
        

        for i in range(len(listSell)):
            self.listBook.append(listSell[i])
        for i in range(len(listBuy)):
            self.listBook.append(listBuy[i])
        
            
        return self.listBook
    
    
    
    
    def ComparareExActions(self,nb,prix):
        
        for i in range(len(self.listBook)):
            compteurIntern = 0
            if (nb > 0):
                
                if (self.listBook[i].price >= prix and self.listBook[i].typeAction == "BUY"):
                    while (nb > 0 and self.listBook[i].quantity >0):
                        self.listBook[i].quantity = self.listBook[i].quantity - 1
                        compteurIntern = compteurIntern +1
                        nb = nb - 1
                if (compteurIntern >= 1):
                    print(f"Execute {compteurIntern} at {self.listBook[i].price} on {self.bookName}")
    
        return nb

class Order:
    def __init__(self, typeAction, quantity, price,id):
        self.typeAction=typeAction
        self.quantity=quantity
        self.price=price
        self.id=id
        
    def __str__(self):
        return f"{self.typeAction}   {self.quantity}@{self.price}   id={self.id}"
# def main():
#     book = Book("TEST")
#     book.insert_buy(10, 10.0)
#     book.insert_sell(120, 12.0)
#     book.insert_buy(5, 10.0)
#     book.insert_buy(2, 11.0)
#     book.insert_sell(1, 10.0)
#     book.insert_sell(10, 10.0)

# if __name__ == "__main__":
#     main()

