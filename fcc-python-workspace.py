
# Strings and Lists

# words = 'His e-mail is q-lar@freecodecamp.org'
# pieces = words.split()
# parts = pieces[3].split('-')
# n = parts[1]
# print(n)


# Python Dictionaries

# dict = {"Fri": 20, "Thu": 6, "Sat": 1}
# dict["Thu"] = 13
# dict["Sat"] = 2
# dict["Sun"] = 9
# print(dict)



# Dictionaries: Common Applications
# counts = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
# print(counts.get('kris', 0))



# Python Dictionaries
# Key, Colon, Value
# dict = {"Fri": 20, "Thu": 6, "Sat": 1, "Sun": 9, "Mon": 8}
# dict["Thu"] = 13
# dict["Sat"] = 2
# dict["Sun"] = 10
# dict["Mon"] = 7
# print(dict)




# Dictionaries: Common Applications
# The get method for dictionaries
# Default value if key does not exist(and no traceback)
# counts = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
# print(counts.get('kris', 0))




# Dictionaries and Loops
counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    if counts[key] > 10:
        print(key, counts[key])