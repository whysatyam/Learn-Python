def max_num(num1, num2, num3):                   # we can compare numbers , strings , booleans etc
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(100 , 200, 500))

# >= greater than or equal to
# <= less than or equal to
# == equal to
# != not equal to