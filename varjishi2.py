import random
import math

num_integers = 5000
upper_bound = 100

for i in range(5000):
    num = random.randint(1,100)

    if num % 17 == 0 and num % 2 == 0 and num % 5 == 0:

        num *= (num , 1/3)

print('jami dzamiaa',num)


#2

def capitalize(word):
    
    return word.capitalize()

sia = ["donkey", "dog", "dingo"]

capitalized_results = list(map(capitalize, sia))

print("Capitalized words:", capitalized_results)

#3 

grades = [["anuki", 8], ["deako", 9], ["salome", 3]]


student_count = 0
max_grade = float('-inf')  


for item in grades:
    student_name, grade = item  
    student_count += 1  
    if grade > max_grade:  
        max_grade = grade

print("Number of students:", student_count)
print("Maximum grade:", max_grade)


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
        """Constructor that initializes the list and prints it."""
        self.elements = elements
        print("Initial list:", self.elements)

    def calculate_stats(self):
        """Calculates and prints the average, minimum, and maximum of the elements."""
        total_sum = sum(self.elements)
        count = len(self.elements)
        average = total_sum / count if count > 0 else 0
        min_element = min(self.elements)
        max_element = max(self.elements)
        print("Average of elements:", average)
        print("Minimum element:", min_element)
        print("Maximum element:", max_element)

    def chamateba(self, index, element):
        """Inserts an element into the list at the specified index."""
        self.elements.insert(index, element)
        print(f"List after inserting {element} at index {index}:", self.elements)

    def cashla(self, element):
        """Removes the specified element from the list if it exists."""
        if element in self.elements:
            self.elements.remove(element)
            print(f"List after removing {element}:", self.elements)
        else:
            print(f"Element {element} not found in the list.")

# Create an object of the List class with an initial list
my_list = List([10, 20, 30, 40, 50])

# Calculate and display the average, minimum, and maximum of the elements
my_list.calculate_stats()

# Use chamateba to insert an element
my_list.chamateba(2, 25)

# Use cashla to remove an element
my_list.cashla(40)


#6
class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number  # Unique account number
        self.account_holder = account_holder  # Account holder's name
        self.balance = balance  # Current balance, default is 0

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def get_balance(self):
        """Return the current balance of the account."""
        return self.balance

    def __str__(self):
        """String representation of the BankAccount."""
        return f"BankAccount(account_number: {self.account_number}, account_holder: {self.account_holder}, balance: {self.balance})"


# Example usage
account = BankAccount(12345, "John Doe", 1000)
print(account)  # Display account details
account.deposit(500)
account.withdraw(200)
print("Final balance:", account.get_balance())
