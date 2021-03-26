people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "cho", "house": "Raveclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

def f(person):
    return person["house"]


people.sort(key=f)

print(people)


def f(person):

    return person["name"]

people.sort(key=f)

print(people)



people.sort(key=lambda person:person["house"])

print(people)

