dictionary = {
    "Schlüssel" : "Wert",
    "Hotel": "Trivagu"
}

def addItem(key, value):
    dictionary[key] = value

addItem("Horst", "Kurt")
print(dictionary["Horst"])

#printValue
print('Schlüssel', dictionary)


#valueIsEqual
def check_key(key, value, dict):
    return dict.get(key) == value

check_value = check_key('Hotel', 'Trivagu', dictionary)
print(check_value)

#deleteItem

del dictionary["Horst"]

check_value = check_key('Horst', 'Kurt', dictionary)
print(check_value)

#printKeys

print("Keys are listed below")
def printKeys(dictionary):
    for i in dictionary.keys():
        print(i)

printKeys(dictionary)


#printValues

print("Values are listed below")
def printValues(dictionary):
    for i in dictionary.values():
        print (i)

printValues(dictionary)