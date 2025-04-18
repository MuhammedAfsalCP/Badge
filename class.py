# # class
# # class is bluepring for creating objects
# class Person:
#     def __init__(self, name, age):
#         self.name = name  # attribute
#         self.age = age

#     def greet(self):  # method
#         print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# # Creating an object
# p1 = Person("Afsal", 22)
# p1.greet()

# init method is a constroctor in python.it runs automaticaly when an object is created

# class Car:
    # def __init__(self, brand):
    #     self.brand = brand

# self
# this keyword refercce to current object used to access atribute and methods inside the class

# def set_name(self, name):
#     self.name = name

# encapsulation
# wrapping data and methods together
# you can hide data using private variables

# class BankAccount:
#     def __init__(self):
#         self.__balance = 0  # private

#     def deposit(self, amount):
#         self.__balance += amount

#     def get_balance(self):
#         return self.__balance

# # Create an object of BankAccount
# account = BankAccount()

# # Deposit money
# account.deposit(1000)

# # Get the current balance
# balance = account.get_balance()

# # Print the balance
# print("Current balance:", balance)
