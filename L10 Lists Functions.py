lucky_numbers = [4, 3, 5, 2, 1]
friends = ["sia", "zayn", "harry", "louis"]

lucky_numbers.append(8)       # use append to add a new element to the list
print(lucky_numbers)

lucky_numbers.reverse()       # reverses the order of list
print(lucky_numbers)

friends.insert(2, "liam")     # this function will insert "liam" to index position 2
print(friends)

friends.remove("sia")         # helps in removing elements from the list
print(friends)

friends.extend(lucky_numbers)  # combines 2 lists together
print(friends)


animals = ["cow", "dog", "cat", "elephant", "elephant", "giraffe"]

print(animals.index("cat"))       # to check position of a element in list

print(animals.count('elephant'))  # to check how many times a value has been repeated in a list

animals.sort()           # for strings - represents list in alphabetical order & for numerical values - ascending order
print(animals)

animals.pop()                  # removes the last element from the list
print(animals)

animals2 = animals.copy()     # creates another list by copying
print(animals2)

animals.clear()               # removes all the elements from the list
print(animals)




