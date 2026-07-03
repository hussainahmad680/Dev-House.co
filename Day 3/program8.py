numbers = [3,1,2,7,5,3,7,9,8,2]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append (number)
print (uniques)