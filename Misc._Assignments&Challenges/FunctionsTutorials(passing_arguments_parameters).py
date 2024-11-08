

mySentence = 'loves the color'

color_list = ['red','blue','green','pink','teal','black']

def color_function(name): #defines the function and establishes the argument 'MATS' (passed from the  'lst' definition below) as a parameter which is called by the 'msg' definition below.
    lst = [] #establishes lst as a list and gives it the content of whatever is passed in the square brackets in it's definition below ('MATS' as 'name' in this case)
    for i in color_list: #creates a for loop that iterates over the elements of the 'color_list' and declares i as the variable for each elemnt value in the list   
        msg = "{} {} {}".format(name,mySentence,i) #establishes the message variable by three wildcards that .format populates with the name passsed from the lst/function definition ('MATS'), the sentence and each element in the 'color_list' 
        lst.append(msg) #tells the loop to add each iteration of the msg variable to the 'lst'-list  
    return lst #!notice the back-indentation! effectively ends the loop after the last iteration of msg is added and returns the 'lst'-list of 'msg'-values

lst = color_function('MATS') #establishes lst as a variable and assigns the color-function as its value with the argument of 'MATS' which said function will call 

for i in lst: #establishes a loop for each iteration ('i') in the 'lst'-list, i.e. each value of 'msg'
    print(i) #tells the program to print the value of (each iteration of-) i/'msg' 


print("-----Next Statement-----")


def get_name(): 
    go = True #establishes the go variable and assigns it the boolean value True
    while go: #establishes a loop that while the variable go is has the bollean value True--> 
        name = input('What is your name? ') #displays a user input with the prompt asking for their name and establihses that input as the value of the name variable
        if name == '': #if the input is empty the following print command will run --
            print("You need to provide your name")
        elif name == 'Sally': #if the input is "Sally" the following print command will run
            print("You are not authorized to use this software") 
        else: #if none of the conditions above are met (if/elif), it will change the value of go to False, effectively ending the loop
            go = False
    lst = color_function(name) #calls the color_function, establishes it as the value of lst and passes in calls the name input as a parameter
    for i in lst: #establishes a loop for each iteration of the lst-list, which is the color-function with the user input name as a paramter
        print(i) #tells the function to print the output, depending on the input 

get_name() #tells the program to run the get_name function


