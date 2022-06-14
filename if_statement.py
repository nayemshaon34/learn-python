is_hot = True
is_cold = True

if is_hot:
    print("It's a hot day")
    print("drink plenty of water")
#shift+tab

elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")


#exercise 1
price = 1000000
is_good_credit = False

if is_good_credit:
    down_payment = price * .1
else:
    down_payment = price * .2
print(f"Downpayment is: ${down_payment}")