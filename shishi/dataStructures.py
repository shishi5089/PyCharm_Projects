# 3 main data structures
# tuple, list, dictionary
# tuple is for fixed data eg days of the week

months = ('Jan' , 'Feb' , 'Mar' , 'Apr' , 'May' , 'Jun')
# above is an example of a tuple

names = ['Shishi' , 'Malea' , 'Gerard' , 'Wayne' , 'Shem']
# above is an example of a list

person = {'names': 'Sheila Nangila' , 'age': 20, 'height': 5.6, 'gender': 'F'} #storing key data pairs
# above is an example of a dictionary

# access data
# know position where item is placed
print(months[0])
print(months)

for month in months :
    print(month)

print("-------------------------------------------")

print(names[0])
print(names)

for name in names :
    print(name)

print("-------------------------------------------")

print(person['names'])
print(person['age'])
print(person['gender'])
print(person['height'])

for key in person:
    print(person[key])

print("--------------------------------------------")

for key, value in person.items():
    print(key, value)

print("--------------------------------------------")
# adding data
# tuple == immutable object
# list == mutable element

names.append("Tiffy")
names.append("Sara")
print(names)

person["weight"] = 80
person["color"] = "chocolate"

print(person)

# to remove from a list
names.remove("Shem")
person.pop('weight')
print(names)
print(person)

# to clear from a list
names.clear()
person.clear()
print(names)
print(person)

print("--------------------------------------------")
people =[{"name":"Hayley","age":17},{"name":"Adelheid","age":81},{"name":"Ingeberg","age":69},{"name":"Carolann","age":45},{"name":"Torin","age":27},{"name":"Gleda","age":48},{"name":"Elke","age":11},{"name":"Luce","age":80},{"name":"Gaylord","age":69},{"name":"Susanne","age":84},{"name":"Rafaelia","age":76},{"name":"Janie","age":12},{"name":"Lucias","age":58},{"name":"Demetre","age":62},{"name":"Aubrette","age":97},{"name":"Wrennie","age":40},{"name":"Ariana","age":76},{"name":"Ryan","age":90},{"name":"Waring","age":50},{"name":"Padriac","age":73},{"name":"Rosie","age":11},{"name":"Terese","age":45},{"name":"Rosemonde","age":28},{"name":"Clarette","age":67},{"name":"Juliann","age":16},{"name":"Oran","age":77},{"name":"Meade","age":34},{"name":"Kele","age":75},{"name":"Stace","age":20},{"name":"Netti","age":58},{"name":"Corrinne","age":43},{"name":"Porter","age":29},{"name":"Selle","age":93},{"name":"Loni","age":79},{"name":"Rhett","age":16},{"name":"Beaufort","age":78},{"name":"Bette","age":24},{"name":"Raynard","age":20},{"name":"Theodor","age":8},{"name":"Alfreda","age":19},{"name":"Letta","age":65},{"name":"Shanta","age":21},{"name":"Orelle","age":22},{"name":"Gerri","age":72},{"name":"Jeff","age":7},{"name":"Alexi","age":98},{"name":"Paolina","age":85},{"name":"Eunice","age":44},{"name":"Petra","age":93},{"name":"Wynnie","age":84},{"name":"Yetta","age":12},{"name":"Pam","age":56},{"name":"Cassy","age":47},{"name":"Berton","age":34},{"name":"Drusilla","age":64},{"name":"Editha","age":36},{"name":"Aguste","age":63},{"name":"Linnea","age":44},{"name":"Julita","age":52},{"name":"Eirena","age":70},{"name":"Bard","age":93},{"name":"Gabi","age":89},{"name":"Byrle","age":67},{"name":"Logan","age":85},{"name":"Hughie","age":92},{"name":"Addie","age":18},{"name":"Jessalin","age":83},{"name":"Lyell","age":45},{"name":"Thalia","age":17},{"name":"Agnola","age":60},{"name":"Sylvester","age":12},{"name":"Betteann","age":56},{"name":"Vitoria","age":99},{"name":"Lanny","age":11},{"name":"Krissie","age":9},{"name":"Donovan","age":38},{"name":"Lynnell","age":81},{"name":"Ole","age":86},{"name":"Lenora","age":11},{"name":"Fernanda","age":13},{"name":"Guntar","age":55},{"name":"Bambi","age":93},{"name":"Hilary","age":42},{"name":"Ealasaid","age":8},{"name":"Mitzi","age":66},{"name":"Cayla","age":27},{"name":"Kasey","age":45},{"name":"Frieda","age":23},{"name":"Lion","age":65},{"name":"Elysee","age":41},{"name":"Lemar","age":14},{"name":"Martha","age":1},{"name":"Yancy","age":34},{"name":"Lena","age":36},{"name":"Ax","age":40},{"name":"Lissy","age":37},{"name":"Gaultiero","age":23},{"name":"Aldwin","age":50},{"name":"Gianina","age":60},{"name":"Errol","age":7}] # list of dictionaries

p1 = people[0] # represents first dictionary in list
print(p1)
print(p1["name"] , p1["age"])

total = 0
for p in people:
    total += p["age"] # cumulative addition
    print(p["name"])

print(total/len(people))

print("--------------------------------------------")
# to sort a list
print(people)

from operator import itemgetter

sortedList = sorted(people, key=itemgetter('age')) # from ascending
sortedList2 = sorted(people, key=itemgetter('age'), reverse=True) # from descending

print(sortedList)
print(sortedList2)

for user in sortedList:
    print(user["name"] , user["age"])

print("--------------------------------------------")
for folk in sortedList2:
    print(folk["name"], folk["age"])

print("--------------------------------------------")