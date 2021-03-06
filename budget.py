class Budget:

    '''A budget app that contains a list of food,
    entertainment and clothing in its category'''

    def __init__(self, category, balance = 0):
        self.category = category
        self.balance = balance


    # A function that accepts money from its user
    def deposit(self):
        deposit_amount = int(input("Enter amount to deposit: \n"))
        self.balance += deposit_amount
        return f"Your new balance in your {self.category} budget is ${self.balance:,.2f}."


    # A function for taking out fund from user's account
    def withdraw(self):
        withdraw_amount = int(input("How much would you like to withdraw? \n"))
        if withdraw_amount > self.balance:
            return "Insufficient funds!!"
        else:
            self.balance -= withdraw_amount
            return f"Please take your cash. \n\n Your new balance is ${self.balance:,.2f}."


    # A function for sending funds to different categories in our app
    def transfer(self):
        print(f"transfer from your {self.category} budget")
        transfer_fund = int(input("Enter amount to transfer: \n"))
        if transfer_fund >= self.balance:
            print("Insufficient fund!!")
        else:
            self.balance -= transfer_fund
            return f"Transfer Successful! \n New balance is ${self.balance:,.2f}"
            
    
    def check_balance(self):
        return f"Your account balance is ${self.balance:,.2f}"


food = Budget("food", 3000)
print(food.check_balance())
