#Establishes the parent class "Personalia" and instantiates a fictional profile
class Personalia:
    fname = "John"
    lname = "Smith"
    phone = "555-5555-555"
    email = "johnsmith@email.com"
    address = "505 Main st. 12345 - Townsville, OR"

#Establishes a method within the Personalia class that promts the user to provide an email address that if it
# matches the email address of the "John Smith" object, will print his personal info 
    def getPersonalia(self):
        email_search = input("Please enter an email to look up their personal info: ")
        if (email_search == self.email):
            print("Name: {} {}\nPhone: {}\nAddress: {}".format(self.fname,self.lname,self.phone,self.address))
        else:
            print("We have no one registered to that email in our system") 


#Establishes the child class "EmploymentInfo" that inherits the attributes of the "Personalia" class, inlcuding
#  the "getPersonalia method and the "John Smith" object, which it adds some values to
class EmploymentInfo(Personalia):
    employer = "Bob's burgers"
    title = "Line Cook"
    employeeID = "98765"

#Nests the parent method "getPersonalia" polymorphously inside the "EmploymentInfo" child class which allows for
# the employeeID value to perform the same function as in the parent class
    def getPersonalia(self):
        employee_search = input("Please enter an employee ID to look up their personal info: ")
        if (employee_search == self.employeeID):
            print("Name: {} {}\nPhone: {}\nAddress: {}".format(self.fname,self.lname,self.phone,self.address))
        else:
            print("We have no one registered to that ID in our system") 


#Establihses another child class and polymorphous use of the parent class method
class Education(Personalia):
    school = "Greendale Community College"
    degree = "MBA"
    studentID = "65432"

    def getPersonalia(self):
        student_search = input("Please enter an student ID to look up the student info: ")
        if (student_search == self.studentID):
            print("Name: {} {}\nPhone: {}\nAddress: {}".format(self.fname,self.lname,self.phone,self.address))
        else:
            print("We have no one registered to that ID in our system") 

#Establishes the queries and ties them to their respective classes
query = Personalia()
query1 = EmploymentInfo()
query2 = Education()


#Calls the method by query in their respective classes and controlls the order of the output
if __name__ == "__main__":
    query.getPersonalia()
    query1.getPersonalia()
    query2.getPersonalia()
