string1 = "Hi there"

multString1 = """This is the first line,
this is the second line,
and this is the thrid line."""

list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
slice1 = slice(3, 6)
slice2 = slice(5)

print(list1[slice1])
print(list1[slice2])

print (len(multString1))

sentence1 = "         there           "

sentenceStr1 = sentence1.strip()
print("Hi", sentenceStr1, ", how are you?")

capsentence1 = string1.upper()
print(capsentence1)

if "h" in string1:
    print("present")

string2 = "qotation marks are written with the \" symbol"
print(string2)
