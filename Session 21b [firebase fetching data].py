
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("kartikTech.json")
firebase_admin.initialize_app(cred)




class Customer:

    def __init__(self, mode):
        if mode == 1:
            self.id = 0
            self.name = input("Enter Customer Name: ")
            self.phone = input("Enter Customer Phone: ")
            self.email = input("Enter Customers Email: ")
        elif mode == 2:
            self.id = int(input("Enter Customer ID: "))
            sql = "select * from Customer where id = {}".format(self.id)


            self.name = input("Enter Customer Name: ")
            self.phone = input("Enter Customer Phone: ")
            self.email = input("Enter Customers Email: ")
        else:
            pass

    def showCustomerDetails(self):
        print("{} | {} | {} ".format( self.name, self.phone, self.email))



# APPLICATION :)
def main():
    db = firestore.client()
    docRef = db.collection("customers").document("Dave@gmail.com").get()
    docDict = docRef.to_dict()
    print(docDict)
    cRef = Customer()
    cRef.name = docRef["name"]
    cRef.phone = docRef["phone"]
    cRef.email = docRef["email"]

    cRef.showCustomerDetails()
