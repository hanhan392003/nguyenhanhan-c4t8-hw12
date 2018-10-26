import requests, json

r = requests.get('https://jsonplaceholder.typicode.com/users', auth=('user','pass'))
# print(r.json())



with open('test2.json','w') as out:
    json.dump(r.json(), out)

with open('test2.json', encoding = 'utf-8') as data:
    dataRead = json.loads(data.read())

# for i in range(len(r.json())):
#     print(r.json()[i])

for i in range(len(dataRead)):
    print(dataRead[i])
    # print(type(dataRead[i]))
find_success = False
for i in dataRead:
    if i['username'] == "Delphine":
        find_success = True
        find_name = i['username']
    
if find_success == True:
    print(find_name)
else:
    print("can't find")

e = input("enter the username ").upper()
find_success1 = False
for i in dataRead:
    if i['username'].upper() == e:
        find_success1 = True
        find_name1 = i['username']
    
if find_success1 == True:
    print(find_name1)
else:
    print("can't find")
