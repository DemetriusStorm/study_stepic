# Inheritance
#
# Classes are designed to allow for more code reuse, but what if we need a class that looks
# a lot like a class we already have? If the bulk of a class's definition is useful, but we have a new use case
# that is distinct from how the original class was used, we can inherit from the original class.
# Think of inheritance as a remix — it sounds a lot like the original, but there's something... different about it.
#
# class User:
#   is_admin = False
#   def __init__(self, username)
#     self.username = username
#
# class Admin(User):
#   is_admin = True
#
# Above we defined User as our base class. We want to create a new class that inherits from it,
# so we created the subclass Admin. In the above example, Admin has the same constructor as User.
# Only the class variable is_admin is set differently between the two.
#
# Sometimes a base class is called a parent class. In these terms, the class inheriting from it,
# the subclass, is also referred to as a child class.
# Instructions
# 1. In script.py we've already defined the class Bin. Create a subclass of Bin called RecyclingBin.
class Bin:
    pass


class RecyclingBin(Bin):
    pass


# ===================================================================
# Exceptions
#
# There's one very important family of class definitions built in to the Python language.
# An Exception is a class that inherits from Python's Exception class.
#
# We can validate this ourselves using the issubclass() function. issubclass()
# is a Python built-in function that takes two parameters. issubclass() returns True if the first argument
# is a subclass of the second argument. It returns False if the first class is not a subclass of the second.
# issubclass() raises a TypeError if either argument passed in is not a class.
#
# issubclass(ZeroDivisionError, Exception)
# # Returns True
#
# Above, we checked whether ZeroDivisionError, the exception raised when attempting division by zero,
# is a subclass of Exception. It is, so issubclass returns True.
#
# Why is it beneficial for exceptions to inherit from one another? Let's consider an example where
# we create our own exceptions. What if we were creating software that tracks our kitchen appliances?
# We would be able to design a suite of exceptions for that need:
#
# class KitchenException(Exception):
#   """
#   Exception that gets thrown when a kitchen appliance isn't working
#   """
#
# class MicrowaveException(KitchenException):
#   """
#   Exception for when the microwave stops working
#   """
#
# class RefrigeratorException(KitchenException):
#   """
#   Exception for when the refrigerator stops working
#   """
#
# In this code, we define three exceptions. First, we define a KitchenException that acts as the parent to our other,
# specific kitchen appliance exceptions. KitchenException subclasses Exception,
# so it behaves in the same way that regular Exceptions do. Afterward we define MicrowaveException
# and RefrigeratorException as subclasses.
#
# Since our exceptions are subclassed in this way, we can catch any of KitchenException's subclasses
# by catching KitchenException. For example:
#
# def get_food_from_fridge():
#   if refrigerator.cooling == False:
#     raise RefrigeratorException
#   else:
#     return food
#
# def heat_food(food):
#   if microwave.working == False:
#     raise MicrowaveException
#   else:
#     microwave.cook(food)
#     return food
#
# try:
#   food = get_food_from_fridge()
#   food = heat_food(food)
# except KitchenException:
#   food = order_takeout()
#
# In the above example, we attempt to retrieve food from the fridge and heat it in the microwave.
# If either RefrigeratorException or MicrowaveException is raised, we opt to order takeout instead.
# We catch both RefrigeratorException and MicrowaveException in our try/except block because
# both are subclasses of KitchenException.
#
# Explore Python's exception hierarchy in the Python documentation!
# Instructions
# 1. In script.py we've defined a CandleShop class for our new candle shop that we've named
# Here's a Hot Tip: Buy Drip Candles. We want to define our own exceptions for when we run out of candles to sell.
# Define your own exception called OutOfStock that inherits from the Exception class.
# 2. Have CandleShop raise your OutOfStock exception when CandleShop.buy() tries to buy a candle that's out of stock.
# Define your exception up here:
class OutOfStock(Exception):
    pass


# Update the class below to raise OutOfStock
class CandleShop:
    name = "Here's a Hot Tip: Buy Drip Candles"

    def __init__(self, stock):
        self.stock = stock

    def buy(self, color):
        if self.stock[color] < 1:
            raise OutOfStock
        self.stock[color] = self.stock[color] - 1


candle_shop = CandleShop({'blue': 6, 'red': 2, 'green': 0})
candle_shop.buy('blue')


# This should raise OutOfStock:
# candle_shop.buy('green')
# ===================================================================
# Overriding Methods
#
# Inheritance is a useful way of creating objects with different class variables,
# but is that all it's good for? What if one of the methods needs to be implemented differently? In Python,
# all we have to do to override a method definition is to offer a new definition for the method in our subclass.
#
# An overridden method is one that has a different definition from its parent class.
# What if User class didn't have an is_admin flag but just checked if it had permission for something based
# on a permissions dictionary? It could look like this:
#
# class User:
#   def __init__(self, username, permissions):
#     self.username = username
#     self.permissions = permissions
#
#   def has_permission_for(self, key):
#     if self.permissions.get(key):
#       return True
#     else:
#       return False
#
# Above we defined a class User which takes a permissions parameter in its constructor.
# Let's assume permissions is a dict. User has a method .has_permission_for() implemented,
# where it checks to see if a given key is in its permissions dictionary. We could then define our Admin user like this:
#
# class Admin(User):
#   def has_permission_for(self, key):
#     return True
#
# Here we define an Admin class that subclasses User. It has all methods, attributes, and functionality that User has.
# However, if you call has_permission_for on an instance of Admin, it won't check its permissions dictionary.
# Since this User is also an Admin, we just say they have permission to see everything!
# Instructions
# 1. In script.py, we've defined two classes, Message and User. Create an Admin class that subclasses the User class.
# 2. Override User's .edit_message() method in Admin so that an Admin can edit any messages.
class Message:
    def __init__(self, sender, recipient, text):
        self.sender = sender
        self.recipient = recipient
        self.text = text


class User:
    def __init__(self, username):
        self.username = username

    def edit_message(self, message, new_text):
        if message.sender == self.username:
            message.text = new_text


class Admin(User):
    def edit_message(self, message, new_text):
        message.text = new_text


# ===================================================================
# Super()
#
# Overriding methods is really useful in some cases but sometimes we want to add some extra
# logic to the existing method. In order to do that we need a way to call the method from the parent class.
# Python gives us a way to do that using super().
#
# super() gives us a proxy object. With this proxy object, we can invoke the method of an object's parent
# class (also called its superclass). We call the required function as a method on super():
#
# class Sink:
#   def __init__(self, basin, nozzle):
#     self.basin = basin
#     self.nozzle = nozzle
#
# class KitchenSink(Sink):
#   def __init__(self, basin, nozzle, trash_compactor=None):
#     super().__init__(basin, nozzle)
#     if trash_compactor:
#       self.trash_compactor = trash_compactor
#
# Above we defined two classes. First, we defined a Sink class with a constructor that assigns
# a rinse basin and a sink nozzle to a Sink instance. Afterwards, we defined a KitchenSink class that inherits
# from Sink. KitchenSink's constructor takes an additional parameter, a trash_compactor. KitchenSink then calls
# the constructor for Sink with the basin and nozzle it received using the super() function, with this line of code:
#
# super().__init__(basin, nozzle)
#
# This line says: "call the constructor (the function called __init__) of the class that is this class's
# parent class." In the example given, KitchenSink's constructor calls the constructor for Sink. In this way,
# we can override a parent class's method to add some new functionality (like adding a trash_compactor to a sink),
# while still retaining the behavior of the original constructor (like setting the basin and
# nozzle as instance variables).
# Instructions
# 1. You're invited to a potluck this week and decide to make your own special version of Potato Salad!
# In script.py you'll find a class called PotatoSalad, make a subclass of PotatoSalad called SpecialPotatoSalad.
# 2. Your special potato salad recipe is pretty similar to a regular potato salad, so let's start with making that.
# Create a new constructor for SpecialPotatoSalad that just calls the parent constructor for PotatoSalad.
# Make sure that SpecialPotatoSalad's constructor takes the same arguments as PotatoSalad.
# 3. The difference with your special potato salad is... you add raisins to it! You can't remember
# when you started doing this, but Dolores always hoots about it at her potlucks and if that isn't the nicest thing.
# You always use the full package of raisins for every potato salad you make, and each package has 40 raisins in it.
#
# In your constructor for SpecialPotatoSalad, after making regular potato salad, set self.raisins = 40.
class PotatoSalad:
    def __init__(self, potatoes, celery, onions):
        self.potatoes = potatoes
        self.celery = celery
        self.onions = onions


class SpecialPotatoSalad(PotatoSalad):
    def __init__(self, potatoes, celery, onions):
        super().__init__(potatoes, celery, onions)
        self.raisins = 40


# ===================================================================
# Interfaces
#
# You may be wondering at this point why we would even want to have two different classes with
# two differently implemented methods to use the same method name. This style is especially useful when
# we have an object for which it might not matter which class the object is an instance of. Instead,
# we're interested in whether that object can perform a given task.
#
# If we have the following code:
#
# class Chess:
#   def __init__(self):
#     self.board = setup_board()
#     self.pieces = add_chess_pieces()
#
#   def play(self):
#     print("Playing chess!")
#
# class Checkers:
#   def __init__(self):
#     self.board = setup_board()
#     self.pieces = add_checkers_pieces()
#
#   def play(self):
#     print("Playing checkers!")
#
# In the code above we define two classes, Chess and Checkers. In Chess we define a constructor that
# sets up the board and pieces, and a .play() method. Checkers also defines a .play() method.
# If we have a play_game() function that takes an instance of Chess or Checkers, it could call the .play()
# method without having to check which class the object is an instance of.
#
# def play_game(chess_or_checkers):
#   chess_or_checkers.play()
#
# chess_game = Chess()
# checkers_game = Checkers()
# chess_game_2 = Chess()
#
# for game in [chess_game, checkers_game, chess_game_2]:
#   play_game(game)
# """
# Prints out the following:
# Playing chess!
# Playing checkers!
# Playing chess!
#
# In this code, we defined a play_game function that could take either a Chess object or a Checkers object.
# We instantiate a few objects and then call play_game on each.
#
# When two classes have the same method names and attributes, we say they implement the same interface.
# An interface in Python usually refers to the names of the methods and the arguments they take.
# Other programming languages have more rigid definitions of what an interface is,
# but it usually hinges on the fact that different objects from different classes can perform the same operation
# (even if it is implemented differently for each class).
# Instructions
# 1. In script.py we've defined an InsurancePolicy class. Create a subclass of InsurancePolicy called VehicleInsurance.
# 2. Create a different subclass of InsurancePolicy called HomeInsurance.
# 3. Give VehicleInsurance a .get_rate() method that takes self as a parameter.
# Return .001 multiplied by the price of the vehicle.
# 4. Give HomeInsurance a .get_rate() method that takes self as a parameter. Return .00005
# multiplied by the price of the home.
class InsurancePolicy:
    def __init__(self, price_of_item):
        self.price_of_insured_item = price_of_item


class VehicleInsurance(InsurancePolicy):
    def get_rate(self):
        return self.price_of_insured_item * .001


class HomeInsurance(InsurancePolicy):
    def get_rate(self):
        return self.price_of_insured_item * .00005


# ===================================================================
# Polymorphism
#
# All this talk of interfaces demonstrates flexibility in programming. Flexibility in programming
# is a broad philosophy, but what's worth remembering is that we want to implement forms that are familiar in our programs so that usage is expected. For example, let's think of the + operator. It's easy to think of it as a single function that "adds" whatever is on the left with whatever is on the right, but it does many different things in different contexts:
#
# # For an int and an int, + returns an int
# 2 + 4 == 6
#
# # For a float and a float, + returns a float
# 3.1 + 2.1 == 5.2
#
# # For a string and a string, + returns a string
# "Is this " + "addition?" == "Is this addition?"
#
# # For a list and a list, + returns a list
# [1, 2] + [3, 4] == [1, 2, 3, 4]
#
# Look at all the different things that + does! The hope is that all of these things are, for the
# arguments given to them, the intuitive result of adding them together. Polymorphism is the term
# used to describe the same syntax (like the + operator here, but it could be a method name) doing
# different actions depending on the type of data.
#
# Polymorphism is an abstract concept that covers a lot of ground, but defining class hierarchies that
# all implement the same interface is a way of introducing polymorphism to our code.
# Instructions
# 1. In script.py a few different types of data are provided. Call len() on each of them.
# Is the same operation happening for each? How is it different? How is it similar? Does using len()
# to refer to these different operations make sense?
a_list = [1, 18, 32, 12]
a_dict = {'value': True}
a_string = "Polymorphism is cool!"

len(a_list)
len(a_dict)
len(a_string)


# ===================================================================
# Dunder Methods
#
# One way that we can introduce polymorphism to our class definitions is by using Python's special
# dunder methods. We've explored a few already, the constructor __init__ and the string representation
# method __repr__, but that's only scratching the tip of the iceberg.
#
# Python gives us the power to define dunder methods that define a custom-made class to look and
# behave like a Python builtin. What does that mean? Say we had a class that has an addition method:
#
# class Color:
#   def __init__(self, red, blue, green):
#     self.red = red
#     self.blue = blue
#     self.green = green
#
#   def __repr__(self):
#     return "Color with RGB = ({red}, {blue}, {green})".format(red=self.red, blue=self.blue, green=self.green)
#
#   def add(self, other):
#     """
#     Adds two RGB colors together
#     Maximum value is 255
#     """
#     new_red = min(self.red + other.red, 255)
#     new_blue = min(self.blue + other.blue, 255)
#     new_green = min(self.green + other.green, 255)
#
#     return Color(new_red, new_blue, new_green)
#
# red = Color(255, 0, 0)
# blue = Color(0, 255, 0)
#
# magenta = red.add(blue)
# print(magenta)
# # Prints "Color with RGB = (255, 255, 0)"
#
# In this code we defined a Color class that implements an addition function.
# Unfortunately, red.add(blue) is a little verbose for something that we have an intuitive symbol
# for (i.e., the + symbol). Well, Python offers the dunder method __add__ for this very reason!
# If we rename the add() method above to something that looks like this:
#
# class Color:
#   def __add__(self, other):
#     """
#     Adds two RGB colors together
#     Maximum value is 255
#     """
#     new_red = min(self.red + other.red, 255)
#     new_blue = min(self.blue + other.blue, 255)
#     new_green = min(self.green + other.green, 255)
#
#     return Color(new_red, new_blue, new_green)
#
# Then, if we create the colors:
#
# red = Color(255, 0, 0)
# blue = Color(0, 255, 0)
# green = Color(0, 0, 255)
#
# We can add them together using the + operator!
#
# # Color with RGB: (255, 255, 0)
# magenta = red + blue
#
# # Color with RGB: (0, 255, 255)
# cyan = blue + green
#
# # Color with RGB: (255, 0, 255)
# yellow = red + green
#
# # Color with RGB: (255, 255, 255)
# white = red + blue + green
#
# Since we defined an __add__ method for our Color class, we were able to add these
# objects together using the + operator.
# Instructions
# 1.
#
# In script.py there are two classes defined, Atom and Molecule.
#
# Give Atom a .__add__(self, other) method that returns a Molecule with the two Atoms.
class Atom:
    def __init__(self, label):
        self.label = label

    def __add__(self, other):
        return Molecule([self, other])


class Molecule:
    def __init__(self, atoms):
        if type(atoms) is list:
            self.atoms = atoms


sodium = Atom("Na")
chlorine = Atom("Cl")
salt = Molecule([sodium, chlorine])


# salt = sodium + chlorine
# ===================================================================
# Dunder Methods II
#
# Python offers a whole suite of magic methods a class can implement that will allow us to use the
# same syntax as Python's built-in data types. You can write functionality that allows custom
# defined types to behave like lists:
#
# class UserGroup:
#   def __init__(self, users, permissions):
#     self.user_list = users
#     self.permissions = permissions
#
#   def __iter__(self):
#     return iter(self.user_list)
#
#   def __len__(self):
#     return len(self.user_list)
#
#   def __contains__(self, user):
#     return user in self.user_list
#
# In our UserGroup class above we defined three methods:
#
#     __init__, our constructor, which sets a list of users to the instance variable self.
#     user_list and sets the group's permissions when we create a new UserGroup.
#     __iter__, the iterator, we use the iter() function to turn the list self.user_list
#     into an iterator so we can use for user in user_group syntax. For more information on iterators,
#     review Python's documentation of Iterator Types.
#     __len__, the length method, so when we call len(user_group) it will return the length
#     of the underlying self.user_list list.
#     __contains__, the check for containment, allows us to use user in user_group syntax to
#     check if a User exists in the user_list we have.
#
# These methods allow UserGroup to act like a list using syntax Python programmers will already be familiar with.
# If all you need is something to act like a list you could absolutely have used a list, but if you want to bundle
# some other information (like a group's permissions, for instance) having syntax that allows
# for list-like operations can be very powerful.
#
# We would be able to use the following code to do this, for example:
#
# class User:
#   def __init__(self, username):
#     self.username = username
#
# diana = User('diana')
# frank = User('frank')
# jenn = User('jenn')
#
# can_edit = UserGroup([diana, frank], {'can_edit_page': True})
# can_delete = UserGroup([diana, jenn], {'can_delete_posts': True})
#
# print(len(can_edit))
# # Prints 2
#
# for user in can_edit:
#   print(user.username)
# # Prints "diana" and "frank"
#
# if frank in can_delete:
#   print("Since when do we allow Frank to delete things? Does no one remember when he accidentally deleted the site?")
#
# Above we created a set of users and then added them to UserGroups with specific permissions.
# Then we used Python built-in functions and syntax to calculate the length of a UserGroup,
# to iterate through a UserGroup and to check for a User's membership in a UserGroup.
# Instructions
# 1. In script.py you'll find the class LawFirm. Give LawFirm a .__len__() method that will return
# the number of lawyers in the law firm.
# 2. Give LawFirm a .__contains__() method that takes two parameters: self and lawyer and
# checks to see if lawyer is in self.lawyers.
class LawFirm:
    def __init__(self, practice, lawyers):
        self.practice = practice
        self.lawyers = lawyers

    def __len__(self):
        return len(self.lawyers)

    def __contains__(self, lawyer):
        return lawyer in self.lawyers


d_and_p = LawFirm("Injury", ["Donelli", "Paderewski"])


# ===================================================================
# Create a class SortedList that inherits from the built-in type list.
# 2. Recall that lists have a .append() method that takes a two arguments, self and value.
# We're going to have SortedList perform a sort after every .append().
# Overwrite the append method, leave it blank for now with the pass keyword.
# 3. First, we want our new .append() to actually add the item to the list.
# Write the code that would get SortedList to behave like a normal list when calling the .append() method.
# 4. After you've appended the new value, sort the list.
# 5. Incredible! We subclassed a Python primitive and introduced new behavior to it.
# Some things to consider:
#     When a SortedList gets initialized with unsorted values (say if you call SortedList([4, 1, 5]))
#     those values don't get sorted! How would you change SortedList so that
#     the list is sorted right after the object gets created?
#     What other Python builtins have functionality "missing"? Could you write a new dictionary
#     that uses a fallback value when it tries to retrieve an item and can't?
#
class SortedList(list):
    def append(self, value):
        super().append(value)
        self.sort()
