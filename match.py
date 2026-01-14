def check_number(x):
    match x:
        case 10:
            return "It's 10"
        case 20:
            return "It's 20"
        case _:
            return "It's neither 10 nor 20"

print (check_number(10))
print (check_number(30))