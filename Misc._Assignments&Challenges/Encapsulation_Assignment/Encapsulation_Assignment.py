#Establishes the class
class ProtectedInfo:
    #Initilializes subseqent objects, passing itself in as the argument
    def __init__(self):
        #Uses the protected method to assign the value of phone number and calls the self argument
        # to assign it as an object under the ProtectedInfo class
        self._phone = "555-555-5555"
        #Uses the private method to assign the value of name 
        self.__name = "John Doe"
        
    #Defines the function that allows for name to be retrived outside the ProtectedInfo class
    def getName(self):
        print(self.__name)

#Establishes an external object that calls on contents of the ProtectedInfo class
RetrieveInfo = ProtectedInfo()
#Extracts the phone number object and prints is value
print(RetrieveInfo._phone)
#Calls the the function that allows for and executes the name to be printed outide the ProtectedInfo class
RetrieveInfo.getName()
