Name = input("What is your name? ")
print("Your name is:", Name)

Qn = "What's your age " + Name + "? "
age = input(Qn)
age = int(age)

TF = age > 18
print(Name, "is an adult?", TF)
