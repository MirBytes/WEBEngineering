people = [
    {"name": "Harry", "House": "Motra"},
    {"name": "Teymur", "House": "Gujrawala"},
    {"name": "Rana", "House": "Kang"}
]

people.sort(key = lambda person: person["name"])

print(people)