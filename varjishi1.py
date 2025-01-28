
#2

def fib(num):
   
    return num * 2  

def capitalize(word):
    
    return word.capitalize()


sia_numbers = [15, 3, 21, 32]
sia_words = ["donkey", "dog", "dingo"]


fib_results = list(map(fib, sia_numbers))


capitalized_results = list(map(capitalize, sia_words))


print("Fibonacci results:", fib_results)
print("Capitalized words:", capitalized_results)

#2 

def fib(num):
  
    return num // 2  

def capitalize(word):
    
    return word.capitalize()

sia_numbers = [15, 3, 21, 32]
sia_words = ["donkey", "dog", "dingo"]

donkey_results = list(map(fib, sia_numbers))

capitalized_results = list(map(capitalize, sia_words))


print("Donkey results:", donkey_results)
print("Capitalized words:", capitalized_results)

#3

grades = [["Apple", 8], ["Banna", 9], ["Peach", 3]]


total_quantity = 0


for item in grades:
    product_name, quantity = item  
    total_quantity += quantity  


print("Total quantity of all products:", total_quantity)


#4
import random
import math

numbers = []

for _ in range(100):
    numbers.append(random.randint(1, 100))

even_numbers = tuple(num for num in numbers if num % 2 == 0)
odd_numbers = {num for num in numbers if num % 2 != 0}

print("Even numbers (tuple):", even_numbers)
print("Odd numbers (set):", odd_numbers)

#5
class List:
    def __init__(self, elements):
    
        self.elements = elements
        print("Initial list:", self.elements)

    def calculate_stats(self):
        total_sum = sum(self.elements)
        min_element = min(self.elements)
        max_element = max(self.elements)
        print("Sum of elements:", total_sum)
        print("Minimum element:", min_element)
        print("Maximum element:", max_element)

    def chamateba(self, index, element):
        self.elements.insert(index, element)
        print(f"List after inserting {element} at index {index}:", self.elements)

    def cashla(self, element):
        if element in self.elements:
            self.elements.remove(element)
            print(f"List after removing {element}:", self.elements)
        else:
            print(f"Element {element} not found in the list.")

my_list = List([10, 20, 30, 40, 50])

my_list.calculate_stats()

my_list.chamateba(2, 25)

my_list.cashla(40)

#6
class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number  # Unique account number
        self.account_holder = account_holder  # Account holder's name
        self.balance = balance  # Current balance, default is 0

    def deposit(self, amount):
       
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"BankAccount(account_number: {self.account_number}, account_holder: {self.account_holder}, balance: {self.balance})"


# Example usage
account = BankAccount(12345, "John Doe", 1000)
print(account)  # Display account details
account.deposit(500)
account.withdraw(200)
print("Final balance:", account.get_balance())
