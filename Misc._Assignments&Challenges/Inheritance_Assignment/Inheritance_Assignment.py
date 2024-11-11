# The below code is a fictional catalog for a company that offers both products and services,
#to illustrate the relationship between parent- and child classes, and inheritance.
# For the purposes of this exercise, the attributes of each class have mostly been directly assigned,
#to illustrate what examples of instances could be, while in a real-world application, the values of
#the clasees would rather be calling on columns of a database etc.

#Establishes the parent class "Catalog" and defines attributes that every instance will have
class Catalog:
    Catalog_id = input("Please enter the category id: ")
    Branch_id = "98765"
    Branch_name = "Portland, OR"

#Establishes a child class "Products" that inherits the attributes from the Catalog class
#and adds another couple of attibutes that will only apply to instances of this class
class Products(Catalog):
    Product_name = "Electrical water pump, model 1"
    Unit_price = 500

#Establishes a child class "Services" that inherits the attributes from the Catalog class
#and adds another couple of attibutes that will only apply to instances of this class
class Services(Catalog):
    Description = "General product inspection and service assessment"
    Technician_type = "Hydroelectrical engineer"
    Hourly_rate = 50.89
