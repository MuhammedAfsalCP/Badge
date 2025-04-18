# if else if 
# this used to descition making
# age = 15

# if age >= 18:
#     print("Adult")
# elif age >= 13:
#     print("Teenager")
# else:
#     print("Child")


# loop

# is used to excute repeated codes

# # while
# is used repete code while condition true time

# x = 1
# while x <= 5:
#     print(x)
#     x += 1



# # for
# used to iterate over a sequence

# for i in range(5):  # 0 to 4
#     print(i)

# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)



# # break
# is used to exit early
# for i in range(5):
#     if i == 3:
#         break
#     print(i)  # 0 1 2


# # continue
# skip the current iteration
# for i in range(5):
#     if i == 2:
#         continue
#     print(i)  # 0 1 3 4


# else with loops
# the else only working loop finshnormaly without break keyword

# for i in range(3):
#     print(i)
# else:
#     print("Loop finished!")

# for i in range(3):
#     if i == 1:
#         break
# else:
#     print("Won't run because of break")


# for i in range(3):
#     for j in range(2):
#         print(i, j)


# list

# a mutabale orderd collection of items you can change its contant

# my_list = [1, 2, 3, "apple", 4.5]


# Tuple
# a immutable ordered collection once created cannot be modified

# my_tuple = (1, 2, 3, "apple")

# set
# a mutable uncorderd collection of unique items
#  my_set = {1, 2, 3, 4}

# forzernset
# a immutable unorderd collection of unique items

# my_frozenset = frozenset([1, 2, 3, "apple"])

# dict
# a unorderd collection of key value pairs

# my_dict = {"name": "Afsal", "age": 25}
# my_dict["city"] = "Kuttippuram"   # Adding new key-value
# del my_dict["age"]                # Removing key 'age'
# print(my_dict)  # Output: {'name': 'Afsal', 'city': 'Kuttippuram'}


# comprantion
# list dict set comprantions provide a compact way of to process data
# my_list = [x * 2 for x in range(5)] 