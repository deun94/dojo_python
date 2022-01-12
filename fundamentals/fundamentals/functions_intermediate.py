#update values

# x = [ [5,2,3], [10,8,9] ] 
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

x = [ [5,2,3], [15,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Bryant'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Andres', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 30} ]

#iterate Through a List of Dictionaries

students = [
        {'first_name': 'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(students):
    for i in range (0,len(students)):
        output_str=""

        for key,val in students[i].items():
            #iterate EAHC key and values
            # print(f"{key}-{val}")
            output_str = output_str + key +" - " + val + ", "
        #need to move print statement here
        #but how1???
        #by moving the scope into the right loop
        print(output_str)


iterateDictionary(students)

# print(students[0]["first_name"])
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)

#Get values from a List of Dictionaries

def iterateDitionary2(key_name, students):
    for i in range (0, len(students)):
        if(key_name == "first_name"):
            print(students[i]["first_name"])
        elif(key_name =="last_name"):
            print(students[i]["last_name"])




iterateDitionary2("first_name", students)
iterateDitionary2("last_name", students)

#Iterate Through a Dictionary with List Values

dojo = {
    'locations': 
        ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': 
        ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_List):
    for key in some_List.keys():
        print(f"{len(some_List[key])} {key.upper()}")
        for val in some_List[key]:
            print(val)

printInfo(dojo)
