def check_age(age):
    if age > 18:
        print("eligible for voting")
    else:
        raise ValueError("age less than 18")


val = int(input("enter age"))
try:
    check_age(val)
except ValueError as e:
    print(f"{e}")
