birthyear = input("please enter your Birth Year ") #when we use input function, we will always get a string
age = 2022 - int(birthyear) #conversing to int from string
print(age)

print(type(birthyear))
print(type(age)) #to see the type of variables


#exercise 1
weight = input("Enter your weight in pounds: ")
print(.4535924*int(weight))