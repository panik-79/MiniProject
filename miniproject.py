# A simple Python function
import time
import random
import datetime
import os
from twilio.rest import Client


# greets the user
def greeting():
    print()
    print("WELCOME TO LA'OPALA CAFE !")
    print()

# wait_func() adds a delay
def wait_func():
    print("Please wait ", end="")
    for i in range(0, 3):
        print(".", end="")
        time.sleep(1)
    print()

# taking user_details as input from the user :
def user_info():
    print("Please enter your login details")
    user_name = input("Enter your name : ")
    password = input("Enter the password : ")
    contact_no = input("Enter your Contact number : ")
    wait_func()
    print(f"Hey, {user_name}")
    locality = input("Address : ")
    flat_number = input("Flat No. : ")
    wait_func()
    print(f"Your address is Flat No. {flat_number} , {locality}")

# otp_function() sends and verifies the otp using 3rd party Twilio API
def otp_function():
    # OTP SENDER
    otp = random.randint(1000, 9999)
    account_sid = "AC228071cb024f37dad6b2970f83a99c74"
    auth_token = 'c1fa18f3fe71bb1cfc47ada1b2994625'
    client = Client(account_sid, auth_token)
    msg = client.messages.create(
        body=f"Your OTP is {otp}",
        from_="+15139603290",
        to="+919522234236"
    )
    # OTP VERIFICATION
    user_otp = int(input("Enter OTP : "))
    time.sleep(1)
    if otp == user_otp:
        print("Successfully Verified !")
    else:
        print("Invalid OTP !")
        print("Press 1 to retry .")
        retry = int(input())
        if retry == 1:
            otp_function()
        else:
            exit()

# food_menu
list_foods = ["Aloo Tikki Burger Rs 100.00",
              "Chatpata Naan Aloo Rs 100.00",
              "Pizza Rs 120.00",
              "Chocolate Brownie Rs 165.00",
              "Spicy Paazta Rs 100.00",
              "White Sauce Paazta Rs 129.00",
              "Masala Chaap Rs 109.00",
              "Veg Noodles Rs 110.00",
              "Spring Roll Rs 149.00",
              "Crispy Corn Rs 119.00",
              "Manchurian Rs 119.00",
              "Masala Dosa Rs 100.00",
              "Spicy Veg Momos Rs 119.00",
              "Tandoor Momos Rs 129.00",
              "Steamed Momos Rs 109.00",
              "Masala Sandwich Rs 149.00",
              "Club Sandwich Rs 180.00",
              "Cheesy Corn Rs 149.00",
              "Bombay Bhel Rs 115.00",
              "Paneer Rolls Rs 200.00"]

# drinks_menu
list_drinks = ["Coca-Cola Rs 35.00",
                "Fanta Rs 35.00",
                "Black Tea Rs 20.00",
                "Sprite Rs 35.00",
                "Limca Rs 35.00",
                "Milk Tea Rs 15.00",
                "Lemon Tea Rs 30.50",
                "Kesariya Milk Rs 45.00",
                "Water Rs 20.00",
                "Virgin Mojito Rs 99.00",
                "Mojito Rs 89.00",
                "Black Coffee Rs 39.00",
                "Cappuccino Rs 69.00",
                "Americano Rs 79.00",
                "Espresso Rs 89.00",
                "Latte Rs 99.00",
                "Milkshake Rs 99.00",
                "Mixed Fruit Juice Rs 75.00",
                "Coconut Crush Rs 89.00",
                "Cold Coffee Rs 89.00"]


list_item_price = [0] * 100


def def_default():
    global list_drinks, list_foods, cart_items, list_item_price
    cart_items = [0] * 100

# main func()
def main():
    while True:
        inp = str(input("Please enter M to open Menu : ")).upper()
        if len(inp) == 1:
            if inp == 'M':
                print("\n" * 2)
                order_menu()
                break

            else:
                print("\n" * 2 + "ERROR: Invalid Input (" + str(inp) + "). Try again!")
        else:
            print("\n" * 2 + "ERROR: Invalid Input (" + str(inp) + "). Try again!")



#order_menu() function provides 3 options to choose from:
# 1) FOODS AND DRINKS MENU 2) MAIN MENU 3) EXIT
def order_menu():
    while True:
        print("-" * 20 + "ORDER PAGE" + "-" * 20 + "\n\n"
                                                   "\t(F) FOODS AND DRINKS\n"
                                                   "\t(M) MAIN MENU\n"
                                                   "\t(E) EXIT\n" +
              "_" * 72)
        print("\n")
        inp = str(input("Please Select Your Option: ")).upper()
        if len(inp) == 1:
            if inp == 'F':
                print("\n" * 2)
                food_and_drinks()
                break
            elif inp == 'M':
                print("\n" * 2)
                main()
                break
            elif inp == 'E':
                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
                break
            else:
                print("\n" * 2 + "ERROR: Invalid Input (" + str(inp) + ").")
        else:
            print("\n" * 2 + "ERROR: Invalid Input (" + str(inp) + ").")

# slicer_func() uses string slicing method to differentiate
# item from its price using index of 'Rs'
def slicer_func():
    i = 0
    while i <= (len(list_foods) - 1):
        if 'Rs' in list_foods[i]:
            list_foods[i] = str(list_foods[i][:list_foods[i].index('Rs') - 1]) + ' ' * (
                        20 - (list_foods[i].index('Rs') - 1)) + str(list_foods[i][list_foods[i].index('Rs'):])
        i += 1

    i = 0
    while i <= (len(list_drinks) - 1):
        if 'Rs' in list_drinks[i]:
            list_drinks[i] = str(list_drinks[i][:list_drinks[i].index('Rs') - 1]) + ' ' * (
                        20 - (list_drinks[i].index('Rs') - 1)) + str(list_drinks[i][list_drinks[i].index('Rs'):])
        i += 1


slicer_func()

# sorter_func() sorts the food and drinks menu list according to the price
def menu_sorter():
    global list_foods, list_drinks
    list_foods = sorted(list_foods)
    list_drinks = sorted(list_drinks)

    # converting prices to float from string using slicing
    i = 0
    while i < len(list_foods):
        list_item_price[i] = float(list_foods[i][int(list_foods[i].index("Rs") + 2):])
        i += 1

    i = 0
    while i < len(list_drinks):
        list_item_price[20 + i] = float(list_drinks[i][int(list_drinks[i].index("Rs") + 2):])
        i += 1


menu_sorter()

# displays food and drinks menu with proper indentation
# from where user can choose items of his choice any number of times
def food_and_drinks():
    while True:
        print("-" * 26 + "ORDER FOODS & DRINKS" + "-" * 26)
        print("\n")
        print(" |NO| |FOOD NAME|         |PRICE|    |  |NO| |DRINK NAME|        |PRICE|\n")

        i = 0
        while i < len(list_foods) or i < len(list_drinks):
            var_space = 1
            if i <= 8:
                var_space = 2

            if i < len(list_foods):
                food = " (" + str(i + 1) + ")" + " " * var_space + str(list_foods[i]) + "  | "
            else:
                food = " " * 36 + "| "
            if i < len(list_drinks):
                drink = "(" + str(21 + i) + ")" + " " + str(list_drinks[i])
            else:
                drink = ""
            print(food, drink)
            i += 1
    # Three option to the user to choose from :
        print("\n (M) MAIN MENU                   (P) PAYMENT                   (E) EXIT\n" + "_" * 72)

        inp = input("Please Select Your Option: ").upper()
        if inp == 'M':
            print("\n" * 2)
            main()
            break
        if inp == 'E':
            print("-" * 32 + "THANK YOU" + "-" * 31 + "\n")
            break
        if inp == 'P':
            print("\n" * 2)
            show_bill()
            break
        try:
            int(inp)
            if (int(inp) <= len(list_foods) and int(inp) > 0) or (int(inp) <= len(list_drinks) + 20 and int(inp) > 20):
                try:
                    print("\n" + "_" * 72 + "\n" + str(list_foods[int(inp) - 1]))
                except:
                    pass
                try:
                    print("\n" + "_" * 72 + "\n" + str(list_drinks[int(inp) - 21]))
                except:
                    pass

                quantity = input("How Many You Want to Order?: ").upper()
                if int(quantity) > 0:
                    cart_items[int(inp) - 1] += int(quantity)
                    print("\n" * 2)
                    print("Successfully Ordered!")
                    food_and_drinks()
                    break
                else:
                    print("\n" * 2 + "ERROR: Invalid Input (" + str(quantity) + ").")
        except:
            print("\n" * 2 + "ERROR: Invalid Input (" + str(inp) + ").")

# shows the bill to the user
def show_bill():
    print("Generating your bill . . . ")
    print()
    wait_func()
    while True:
        print("-" * 30 + "YOUR BILL" + "-" * 30 + "\n")
        total_price = 0

        date_time = "\n\n\n" + " " * 17 + "*" * 35 + "\n" + " " * 17 + "DATE: " + str(datetime.datetime.now())[:19] + "\n" + " " * 17 + "-" * 35
        i = 0
        print(date_time)
        while i < len(cart_items):
            if cart_items[i] != 0:
                if (i >= 0) and (i < 20):
                    date_time += "\n" + " " * 17 + str(list_foods[i]) + "  x  " + str(cart_items[i])
                    print(" " * 17 + str(list_foods[i]) + "  x  " + str(cart_items[i]))
                    total_price += list_item_price[i] * cart_items[i]
                if (i >= 20) and (i < 40):
                    date_time = date_time + "\n" + " " * 17 + str(list_drinks[i - 20]) + "  x  " + str(cart_items[i])
                    print(" " * 17 + str(list_drinks[i - 20]) + "   x  " + str(cart_items[i]))
                    total_price += list_item_price[i] * cart_items[i]
                i += 1
            else:
                i += 1

        date_time = date_time + "\n" + " " * 17 + "-" * 35 + "\n" + " " * 17 + "TOTAL PRICES:       Rs " + str(
            round(total_price, 2)) + "\n" + " " * 17 + "*" * 35
        print(" " * 17 + "_" * 35 + "\n" + " " * 17 + "TOTAL PRICES:       Rs " + str(round(total_price, 2)))

        print("\n (P) PAY           (M) MAIN MENU              (E) EXIT\n" + "_" * 72)
        inp = str(input("Please Select Your Option : ")).upper()
        if inp == 'P':
            print("\n" * 2)
            print("Successfully Paid!")

            def_default()
        elif inp == 'M':
            print("\n" * 2)
            main()
            break
        elif ('E' in inp) or ('e' in inp):
            print("-" * 31 + "THANK YOU" + "-" * 31 + "\n")
            break


### Calling the functions according to precedence
def_default()
greeting()
user_info()

# OTP_function() is commented because to get the OTP , number should be registered
# on the website of third-party Twilio API

#otp_function()


main()

