# Bank (bank_name,person_name,account_number,balance)
# (desposit(amount),
# withdraw(amount),
# bal_enq()

class Bank:

    bank_name = str

    person_name = str

    account_number = int

    balance = int

    def set_bank(bank_name,person_name,account_number,balance):
        
        self.bank_name = bank_name

        self.person_name = person_name

        self.account_number = account_number

        self.balance = balance
        
    def display_bank(self):

        print(self.bank_name,self.person_name,self.account_number,self.balance)

class Bank:
    def set_customer_details(self,person_name,acc_no,bal):

        self.bank_name = "SBI"

        self.person_name = person_name
        
        self.acc_no = acc_no
        
        self.bal = bal

    def bal_enq(self):

        print(f"dear{self.bank_name} customer your acc{self.acc_no}avl bal is {self.bal}")

    def desposit(self,amount):

        self.bal += amount

        print(f"your {self.bank_name} acc {self.acc_no} has been credited with amoun {amount} aval bal {self.bal}")

    def withdraw(self,amount):

        if self.bal < amount:

            print("transaction failed due to insufficient bal")

        else:

            self.bal -= amount

            print(f"your{self.bank_name} acc {self.acc_no} has been debited with amount {amount} available balance is {self.bal}")

bank_instance1 = Bank()

bank_instance1.set_customer_details("vipin",1234,2000)

bank_instance1.withdraw(25000)

bank_instance1.bal_enq()

# Object oriented features

# Topic for tomorrow : looping (while,for,break,continue)