class car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def description(self):
        return f"{self.make} {self.model}"

    def get_make(self):
        return self.make
    def get_model(self):
        return self.model
    
    def set_make(self, make):
        self.make = make
    def set_model(self, model):
        self.model = model
        
        
# create object 
car_object = car("Toyota", "Camry")
car_object.description()    



class person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def description(self):
        return f"{self.__name} {self.__age}"
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def set_name(self, name):
        self.__name = name
    def set_age(self, age):
        self.__age = age
        
        
# create object 
person_object = person("John", 25)
person_object.description()    

class BankAccount:
    def __init__(self, owner, balance):
        self.__owner = owner          # Private attribute
        self.__balance = balance      # Private attribute
    
    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposit successful. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")
    
    # Public method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawal successful. New balance: {self.__balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")
    
    # Public method to get balance (getter)
    def get_balance(self):
        return self.__balance
    
    # Public method to get owner (getter)
    def get_owner(self):
        return self.__owner

# Create an instance of BankAccount
my_account = BankAccount("Alice", 1000)

# Accessing public methods
print(f"Owner: {my_account.get_owner()}")
print(f"Initial Balance: {my_account.get_balance()}")

my_account.deposit(500)
my_account.withdraw(200)

# Trying to access private attributes directly (will raise AttributeError)
# print(my_account.__balance)  # This would cause an error  
