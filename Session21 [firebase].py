"""#python -m pip install -U --force-reinstall pip
    pip install firebase-admin

    If facing errors ,try updating your pip
    python -m pip install -U--force-reinstall pip

  2. Go to firebase.google.com
     Create a New Project(edit project id of ur choice )
     Use location as India

  3. Create Database inn ur Account
      Create Firebase in Test Mode
      Location --> Asia South1[ depends upon ur choice

  4. Go to settings
      Project Settings--> Service accounts

   5. Copy this downloaded json file in Pycharm Project and

   6. Copy the Snippet and paste it in ur program
      """


import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("kartikTech.json")
firebase_admin.initialize_app(cred)
print(">>this is awesome")



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
   customer = Customer(1)
   customer.showCustomerDetails()
   customerdata = customer.__dict__
   print(customerdata,type(customerdata))

   # db is refrence to FireStore Database
   db = firestore.client()
   db.collection("customers").document(customer.email).set(customerdata)
   print(">> Customer Saved")

if __name__ == "__main__":
    main()


