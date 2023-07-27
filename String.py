String functions

a="Hello"
print(a)

a="hello world1"
print(a[6])

a="Rishita"
print(len(a))

a="Hello world"
print(a.upper())

a="RISHITA"
print(a.lower())

a="Hello, world"
print(a.strip())

txt="hello world"
print(txt.replace("h","j"))

txt="hello, world"
print(txt.split(","))

message=""" Never gonna give up
Never gonna let you down
"""
print(message)

txt=input("Enter your name ")
if("R" and "a" in txt):
  print(txt)
else:
  print("R is no available in your name")

lists

fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits)

fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()
print(fruits)

fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()
print(x)

fruits = ['apple', 'banana', 'cherry']
x = fruits.count("cherry")
print(x)

fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)

sets

x = {"apple", "banana", "cherry"}
y = {"mango", "grapes", "apple"}
z = x.difference(y)
print(z)

x = {"apple", "banana", "cherry"}
y = {"mango", "grapes", "apple"}
z = x.isdisjoint(y)
print(z)

fruits = {"apple", "banana", "cherry"}
fruits.pop() 
print(fruits)

x = {"apple", "banana", "cherry"}
y = {"mango", "grapes", "apple"}
z = x.symmetric_difference(y) 
print(z)

x = {"apple", "banana", "cherry"}
y = {"mango", "grapes", "apple"}
z = x.union(y) 
print(z)

dictonary

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.popitem()
print(car)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.get("model")
print(x)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("model", "Bronco")
print(x)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.values()
print(x)







