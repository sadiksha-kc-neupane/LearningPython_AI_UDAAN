# name1 =["ram","hari","sita"]  #list
# name2 ={"ram","hari","sita"} #sets
# name3 =("ram","hari","sita")#tuples

countries =["Nepal","USA","germany","France","Nepal"]
countries_tuple =("Nepal","USA","germany","France","Nepal")
countries_set ={"Nepal","USA","germany","France","France","USA"}

# print(countries[-1])  

# countries.append("Italy")  #-- to add items at end of the list
# countries.pop() #-- Removes the items from the end of the list
# countries.insert(2,"italy")  #added to the 2nd index of the list , you can add  at index of your choice
# countries.remove("germany")  #remove takes an argumemt as an whaat you want to remove from the list
# countries[1] = "india"  #to add to index and what you wwant to add 
 
# print(countries)


# print(countries_tuple.count("Nepal"))   #count numberof items inside tuples
# print(countries_tuple.index("Nepal"))   #to know the index of the item inside tuple

# print(countries_set)

Person ={
    "Name":"Diksha",
    "address": "itahari",
    "age" : "22",
    "email" : "hello@gmail.com"
}  #This is dictionary 

print(Person["age"])
Person["color"]="Red"
print(Person)


Person.pop("address")

print(Person)

