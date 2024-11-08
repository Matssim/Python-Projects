myDictionary = {'index1': 1, 'index2': 2, 'index3': 355}
dic_users = {'em_1234': {'fname': 'Bob', 'lname': 'Smith', 'phone': '123-456-7890'}, 'em_1235': {'fname': 'Mary', 'lname': 'Jones', 'phone': '152-364-5764'}}

print(dic_users['em_1235'])
print(dic_users['em_1235']['phone'])
print ('User: {} {} \nPhone: {}'.format(dic_users['em_1235']['fname'],dic_users['em_1235']['lname'], dic_users['em_1235']['phone']))

