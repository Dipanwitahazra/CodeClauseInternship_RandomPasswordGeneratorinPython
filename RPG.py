import random
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*_"
while True:
    pass_length = int(input("enter the length of req. password: "))
    pass_count = int(input("enter the number of req. passwords: "))
    for i in range(0, pass_count):
        password = ""
        for j in range(0,pass_length):
            pass_char = random.choice(characters)
            password = password+pass_char
        print("The generated password is",password)
    repeat = input("Do you want to generate more generators?")
    if repeat == "no" or repeat == "No":
        break
print("OK")




