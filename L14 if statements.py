is_male = True
is_tall = True

if is_male or is_tall:
    print("you are a male or tall or both")
else:

    print("you are neither male nor tall")



is_short = False
is_female = True

if is_female and is_short:
    print("you are a short female")

elif is_female and not(is_short):
    print("you are a tall female")

elif is_short and not(is_female):
    print("you are short but not female")

else:
    print("you are neither female nor short")