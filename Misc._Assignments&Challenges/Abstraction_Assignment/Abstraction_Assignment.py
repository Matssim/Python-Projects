#Imports the abc modules that allows for abstract base classes to be creates and using the abstract method
from abc import ABC, abstractmethod

#Defines the parent class and passes in the ABC module 
class Introduction(ABC):
    #Defines the first function, using the regular print() method to print the first introductory message
    def Greeting(self):
        print("Hi there! What is your name?")
    #Uses the abstract method to establish a the GetName function, passing in the name argument without knowing
    # what that is/will be
    @abstractmethod
    def GetName(self, name):
        pass

#Defines the child class passing in the attributes of the (parent) Introduction class
class Response(Introduction):
    #Adds a method to the GetName function, to print a response message based on the abstract name argument
    def GetName(self, name):
        print("Good to meet you {}!".format(name))

#Establishes an object using the child class to call on it's functions
obj = Response()
#Calls the parent class function to print the initial greeting
obj.Greeting()
#Calls the child class function and passes in the user's input as the abstract name argument
obj.GetName(input("Enter name: "))
































