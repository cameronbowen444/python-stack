x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
} 
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x)

sports_directory["basketball"][1] = "Bryant"
sports_directory["soccer"][0] = "Andres"
print(sports_directory)

z[0]["y"] = 30
print(z)


students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iteratedictionary(list):
    for x in range(0,len(list)):
        output = ""
        for key,val in list[x].items():
            output += f" {key} - {val},"
        print(output)
iteratedictionary(students)


def iteratedictionary2(key_name, list):
    for x in range(0, len(list)):
        for key,val in list[x].items():
            if key == key_name:
                print(val)
iteratedictionary2("first_name", students)
iteratedictionary2("last_name", students)



dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key,val in some_dict.items():
        print(f"{len(val)} {key.upper()}")
        for i in range(0, len(val)):
            print(val[i])
printInfo(dojo)
