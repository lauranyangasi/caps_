z = None
print(z)
print("great - how - are - you" )\

print('great', '-', 'how', '-', 'are', '-', 'you')
print('great-' + 'how-are-you')
pets = ["Dog", "Cat", "Parrot", "Monkey", "Rabbit"]
pets[0] = "Lion"
pets[1] = "Tiger"

pets.append("snake")

print(pets)
str = "Technology"
print(str[:3])


r = set('xyz')
r.add('fan')
r.update(set(['u', 'v']))
print(r)
print(round(100.000056, 3))
fruit = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
if fruit[2] == "mango":
    print(f"{fruit[-5]} is nicer than the other fruits")
else:
    print(f"{fruit[-5]} is not nicer than the other fruits")

def person(name,age):
    x = ("portia", 9)
    if name == "Alice":
        print("Hi, Alice.")
    elif age < 12:
        print("you are not Alice, Kiddo.")
    else :
        print("An adult")

grade1 = 80
grade2 = 90
average = (grade1 + grade2) / 2
grade1 = 100
average