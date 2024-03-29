# the goal of this code is to use strings instead of lists/dictionaries
# to create a shopping menu

shop_name = "PawsN'Cart"
total_cost = '';total_items = 0
currencies = "£ € $ ¥";currencies.split()
session_ended = False
add = "Added";remove = "Removed"
shopping_cart = "Shopping Cart:\n"
def receipt():
    print(f"Thank You For Shopping At {shop_name}\n\n\
Your Purchase List:{shopping_cart.replace("Shopping Cart:","")}\n\
Number Of Items Purchased: {total_items}\n\n\
Total Cost: {currencies[0]}{total_cost}")

def zeroend(): # visual for end session option
    zero = "End_Session"
    for i, end in enumerate(zero.split()):
        end = end.replace('_',' ')
        print(f"[{i}] {end}")

def menu_nonitems(): # other options
    nonitems = "Shopping_Cart Back"
    for i, option in enumerate(nonitems.split(),8):
        option = option.replace('_',' ')
        print(f"[{i}] {option}")

main_menu_list = "End_Session Sale Dog Cat Bird Other_Pets \
Own_Brand Seasonal Checkout"
def main_menu():
    print("Main Menu:")
    main_items = len(main_menu_list.split())
    for main_items, main_option in enumerate(main_menu_list.split()):
        main_option = main_option.replace('_',' ')
        print(f"[{main_items}] {main_option}")
# sale vars and funcs
sale_menu_list = "HappyPup_Dry_Dog_Food_(5KG) \
MEGA'P'_Dry_Guinea_Pig_Food_(5KG) Cat_Atax_Wet_Cat_Food_(5KG)"
sale_menu_list = sale_menu_list.split()
sale_menu_cost = "0 6.99 5.99 7.95";sale_men_cost = sale_menu_cost.split()
def sale_menu():
    print("\nSale Menu:");zeroend();sale_len = len(sale_menu_cost)
    for sale_len, sale_item in enumerate(sale_menu_list,1):
        sale_item = sale_item.replace('_',' ')
        print(f"[{sale_len}] {sale_item}")
    menu_nonitems()

def sale_item_add(total_items, total_cost, shopping_cart):
    """func prints selected option, adds to shopping cart"""
    total_items += 1
    total_cost += sale_menu_cost[int(sale_menu_option)]
    shopping_cart += f"{sale_menu_list[int(sale_menu_option)-1].replace('_',' ')} \
: {currencies[0]}{sale_menu_cost[int(sale_menu_option)]}\n"
    print(f"{sale_menu_list[int(sale_menu_option)-1].replace('_',' ')} \
: {currencies[0]}{sale_men_cost[int(sale_menu_option)]} {add}")
 
def sale_selection():
    """output option changes based on user selection"""
    if sale_menu_option == "1":
        sale_item_add()
    elif sale_menu_option == "2":
        sale_item_add()
    elif sale_menu_option == "3":
        sale_item_add()
    elif sale_menu_option == "8":
        print(f"{shopping_cart}\nTotal Items: {total_items}\n\
Total Cost: {currencies[0]}{total_cost}") # shopping cart
    else:
        print("Invalid Input")
# dog vars and funcs
dog_menu_list = "HappyPup_Dry_Dog_Food HappyPup_Wet_Dog_Food \
Dogogo_Dry_Dog_Food Dogogo_Wet_Dog_Food"
dog_menu_list = dog_menu_list.split()
dog_menu_cost = "0 6.99 8.99 7.99 9.99";dog_menu_cost = dog_menu_cost.split()
def dog_menu():
    print("\nDog Menu:");zeroend();dog_len = len(dog_menu_list)
    for dog_len, dog_item in enumerate(dog_menu_list,1):
        dog_item = dog_item.replace('_',' ');print(f"[{dog_len}] {dog_item}")
    menu_nonitems()
        
def dog_item_add(total_items,total_cost,shopping_cart):
    """func prints selected option, adds to shopping cart"""
    total_items += 1
    total_cost += dog_menu_cost[int(dog_menu_option)]
    shopping_cart += f"{dog_menu_list[int(dog_menu_option)-1].replace('_',' ')} \
: {currencies[0]}{dog_menu_cost[int(dog_menu_option)]}\n"
    print(f"{dog_menu_list[int(dog_menu_option)-1].replace('_',' ')} \
: {currencies[0]}{dog_menu_cost[int(dog_menu_option)]} {add}\n")

def dog_selection(): 
    """output option changes based on user selection of dog item"""
    if dog_menu_option == "1":
        dog_item_add()
    elif dog_menu_option == "2":
        dog_item_add()
    elif dog_menu_option == "3":
        dog_item_add()
    elif dog_menu_option == "4":
        dog_item_add()
    elif dog_menu_option == "8":
        print(f"{shopping_cart}\nTotal Items: {total_items}\n\
Total Cost: {currencies[0]}{total_cost}") # shopping cart
    else:
        print("Invalid Input")
# cat vars and funcs
cat_menu_list = "Cat_Atax_Wet_Cat_Food KATT'in_Wet_Cat_Food"
cat_menu_list = cat_menu_list.split()
cat_menu_cost = "0 7.95 9.99";cat_menu_cost = cat_menu_cost.split()
def cat_menu():
    print("\nCat Menu:");zeroend();cat_len = len(cat_menu_list)
    for cat_len, cat_item in enumerate(cat_menu_list,1):
        cat_item = cat_item.replace('_',' ');print(f"[{cat_len}] {cat_item}")
    menu_nonitems()

def cat_item_add(total_items,total_cost,shopping_cart):
    """func prints selected option, adds to shopping cart"""
    total_items += 1
    total_cost += cat_menu_cost[int(cat_menu_option)]
    shopping_cart += f"{cat_menu_list[int(cat_menu_option)-1].replace('_',' ')} \
: {currencies[0]}{cat_menu_cost[int(cat_menu_option)]}\n"
    print(f"\n{cat_menu_list[int(cat_menu_option)-1].replace('_',' ')} \
: {currencies[0]}{cat_menu_cost[int(cat_menu_option)]} {add}\n")
        
def cat_selection():
    """output option changes based on user selection of cat item"""
    if cat_menu_option == "1":
        cat_item_add()
    elif cat_menu_option == "2":
        cat_item_add()
    elif cat_menu_option == "3":
        cat_item_add()
    elif cat_menu_option == "4":
        cat_item_add()
    elif cat_menu_option == "8":
        print(f"{shopping_cart}\nTotal Items: {total_items}\n\
Total Cost: {currencies[0]}{total_cost}") # shopping cart
    else:
        print("Invalid Input")
# bird vars and funcs
bird_menu_list = "LOLBird_Seed Flappy_Bird_Feed Flappy_Bird_Seed"
bird_menu_list = bird_menu_list.split()
bird_menu_cost = "0 6.99 6.95 7.95";bird_menu_cost = bird_menu_cost.split()
def bird_menu():
    print("\nBird Menu:");zeroend();bird_len = len(bird_menu_list)
    for bird_len, bird_item in enumerate(bird_menu_list,1):
        bird_item = bird_item.replace('_',' ');print(f"[{bird_len}] {bird_item}")
    menu_nonitems()
    
def bird_item_add(total_items,total_cost,shopping_cart): 
    """func prints selected option, adds to shopping cart"""
    total_items += 1
    total_cost += bird_menu_cost[int(bird_menu_option)]
    shopping_cart += f"{bird_menu_list[int(bird_menu_option)-1].replace('_',' ')} \
: {currencies[0]}{bird_menu_cost[int(bird_menu_option)]}\n"
    print(f"\n{bird_menu_list[int(bird_menu_option)-1].replace('_',' ')} \
: {currencies[0]}{bird_menu_cost[int(bird_menu_option)]} {add}\n")
        
def bird_selection(): 
    """output option changes based on user selection"""
    if bird_menu_option == "1":
        bird_item_add()
    elif bird_menu_option == "2":
        bird_item_add()
    elif bird_menu_option == "3":
        bird_item_add()
    elif bird_menu_option == "4":
        bird_item_add()
    elif bird_menu_option == "8":
        print(f"{shopping_cart}\nTotal Items: {total_items}\n\
Total Cost: {currencies[0]}{total_cost}") # shopping cart
    else:
        print("Invalid Input")
# other pet vars and funcs
other_pet_menu_list = "Fish_Food Lizard_Snack Guinea_Pig_Hay"
other_pet_menu_list = other_pet_menu_list.split()
other_pet_menu_cost = "0 4.99 8.99 5.45"
other_pet_menu_cost = other_pet_menu_cost.split()
def other_pets_menu():
    print("\nOther Pets Menu:");zeroend();opet_len = len(other_pet_menu_list)
    for opet_len, opet_item in enumerate(other_pet_menu_list,1):
        opet_item = opet_item.replace('_',' ')
        print(f"[{opet_len}] {opet_item}")
    menu_nonitems()
    
def otherpet_item_add(total_items,total_cost,shopping_cart): 
    """func prints selected option, adds to shopping cart"""
    total_items += 1
    total_cost += other_pet_menu_cost[int(other_menu_option)]
    shopping_cart += f"{other_pet_menu_list[int(other_menu_option)-1].replace('_',' ')} \
: {currencies[0]}{other_pet_menu_cost[int(other_menu_option)]}\n"
    print(f"\n{other_pet_menu_list[int(other_menu_option)-1].replace('_',' ')} \
: {currencies[0]}{other_pet_menu_cost[int(other_menu_option)]} {add}\n")
        
def otherpet_selection():
    """output option changes based on user selection of other item"""
    if other_menu_option == "1":
        otherpet_item_add()
    elif other_menu_option == "2":
        otherpet_item_add()
    elif other_menu_option == "3":
        otherpet_item_add()
    elif other_menu_option == "4":
        otherpet_item_add()
    elif other_menu_option == "8":
        print(f"{shopping_cart}\nTotal Items: {total_items}\n\
Total Cost: {currencies[0]}{total_cost}") # shopping cart
    else:
        print("Invalid Input")
#own brand vars and funcs
own_menu_list = f"{shop_name}_Wet_Dog_Food {shop_name}_Dry_Dog_Food \
{shop_name}_Wet_Cat_Food {shop_name}_Dry_Cat_Food"
own_menu_list = own_menu_list.split()
own_menu_cost = "0 5.99 4.99 6.99 6.49";own_menu_cost.split()
def own_brand_menu():
    print("\nOwn Brand Menu:");zeroend();own_len = len(own_menu_list)
    for own_len, own_item in enumerate(own_menu_list,1):
        own_item = own_item.replace('_',' ');print(f"[{own_len}] {own_item}")
    menu_nonitems()
        
def own_item_add(total_items,total_cost,shopping_cart): 
    """func prints selected option, adds to shopping cart"""
    total_items += 1
    total_cost += own_menu_cost[int(own_brand_option)]
    shopping_cart += f"{own_menu_list[int(own_brand_option)-1].replace('_',' ')} \
: {currencies[0]}{own_menu_cost[int(own_brand_option)]}\n"
    print(f"\n{own_menu_list[int(own_brand_option)-1].replace('_',' ')} \
: {currencies[0]}{own_menu_cost[int(own_brand_option)]} {add}\n")
        
def own_selection(): 
    """output option changes based on user selection"""
    if own_brand_option == "1":
        own_item_add()
    elif own_brand_option == "2":
        own_item_add()
    elif own_brand_option == "3":
        own_item_add()
    elif own_brand_option == "4":
        own_item_add()
    elif own_brand_option == "8":
        print(f"{shopping_cart}\nTotal Items: {total_items}\n\
Total Cost: {currencies[0]}{total_cost}") # shopping cart
    else:
        print("Invalid Input")
# seasonal vars and funcs
seamen = "Winter_Snow Frosty_Ice Slay_Bells"
seamen = seamen.split()
seamen_cost = "0 2.99 3.99 5.99";seamen_cost = seamen_cost.split()
def seasonal_menu():
    zeroend();print("\nSeasonal Menu:");sea_len = len(seamen)
    for sea_len, sea_item in enumerate(seamen,1):
        sea_item = sea_item.replace('_',' ');print(f"[{sea_len}] {sea_item}")
    menu_nonitems()
    
def sea_item_add(total_items,total_cost,shopping_cart): 
    """func prints selected option, adds to shopping cart"""
    total_items += 1
    total_cost += seamen_cost[int(sea_menu_option)]
    shopping_cart += f"{seamen[int(sea_menu_option)-1].replace('_',' ')} \
: {currencies[0]}{seamen_cost[int(sea_menu_option)]}\n"
    print(f"\n{seamen[int(sea_menu_option)-1].replace('_',' ')} \
: {currencies[0]}{seamen_cost[int(sea_menu_option)]} {add}\n")
        
def seasonal_selection(): 
    """output option changes based on user selection"""
    if sea_menu_option == "1":
        sea_item_add()
    elif sea_menu_option == "2":
        sea_item_add()
    elif sea_menu_option == "3":
        sea_item_add()
    elif sea_menu_option == "4":
        sea_item_add()
    elif sea_menu_option == "8":
        print(f"{shopping_cart}\nTotal Items: {total_items}\n\
Total Cost: {currencies[0]}{total_cost}") # shopping cart
    else:
        print("Invalid Input")

# checkout vars and funcs
checkout_menu_list = "Remove_Item Add_Item Checkout"
checkout_menu_list = checkout_menu_list.split()
def checkout_menu():
    """menu for user to checkout"""
    print("\nCheckout:");zeroend();check_len = len(checkout_menu_list)
    for check_len, check_option in enumerate(checkout_menu_list,1):
        check_option = check_option.replace('_',' ')
        print(f"[{check_len}] {check_option}")
    menu_nonitems()
          
print(f"Welcome To {shop_name}\n")
# shop loop
while True:
    if session_ended == True:
        break
    main_menu() # mmo = main menu option
    mmo = input("\nEnter a Number From The Main Menu: ")
    if mmo == "0":
        print("Session Ended\nGoodbye")
        session_ended = True # end session
# sale menu
    elif mmo == "1":
        print("Sale Menu Selected")
        while True:
            sale_menu()
            sale_menu_option = input("\nEnter a Number From The Sale Menu: ")
            sale_selection()
            if sale_menu_option == "0":
                print("Session Ended\nGoodbye")
                session_ended = True
                break
            elif sale_menu_option == "9":
                print("Back To Main Menu\n");break
# dog menu
    elif mmo == "2":
        print("Dog Menu Selected")
        while True:
            dog_menu()
            dog_menu_option = input("\nEnter a Number From The Dog Menu: ")
            if dog_menu_option == "0":
                print("Session Ended\nGoodbye")
                session_ended = True
                break
            elif dog_menu_option == "9":
                print("Back To Main Menu\n");break
            dog_selection()
# cat menu            
    elif mmo == "3":
        print("Cat Menu Selected")
        while True:
            cat_menu()
            cat_menu_option = input("\nEnter a Number From The Cat Menu: ")
            if cat_menu_option == "0":
                print("Session Ended\nGoodbye")
                session_ended = True
                break
            elif cat_menu_option == "9":
                print("Back To Main Menu\n");break
            cat_selection()
# bird menu            
    elif mmo == "4":
        print("Bird Menu Selected")
        while True:
            bird_menu()
            bird_menu_option = input("\nEnter a Number From The Bird Menu: ")
            if bird_menu_option == "0":
                print("Session Ended\nGoodbye")
                session_ended = True
                break
            elif bird_menu_option == "9":
                print("Back To Main Menu\n");break
            bird_selection()
# other pets menu
    elif mmo == "5": 
        print("Other Pets Menu Selected")
        while True:
            other_pets_menu()
            other_menu_option = input("\nEnter a Number From The Other Pets Menu: ")
            if other_menu_option == "0":
                print("Session Ended\nGoodbye")
                session_ended = True
                break
            elif other_menu_option == "9":
                print("Back To Main Menu\n");break
            otherpet_selection()
# own brand menu
    elif mmo == "6": 
        print("Own Brand Menu Selected")
        while True:
            own_brand_menu()
            own_brand_option = input("\nEnter a Number From The Own Brand Menu: ")
            if own_brand_option == "0":
                print("Session Ended\nGoodbye")
                session_ended = True
                break
            elif own_brand_option == "9":
                print("Back To Main Menu\n");break
            own_selection()
# seasonal menu
    elif mmo == "7": 
        print("Seasonal Menu Selected")
        while True:
            seasonal_menu()
            sea_menu_option = input("\nEnter a Number From The Seasonal Menu: ")
            if sea_menu_option == "0":
                print("Session Ended\nGoodbye")
                session_ended = True
                break
            elif sea_menu_option == "9":
                print("Back To Main Menu\n");break
            seasonal_selection()
# checkout
    elif mmo == "8":
        print(f"Checkout Selected")
        while True:
            checkout_menu()
            chmo = input("\nEnter a Number From The Checkout Menu: ")
            if chmo == "0":
                print("Session Ended\nGoodbye");session_ended = True;break
            if chmo == "8":
                print(f"{shopping_cart}\nTotal Items: {total_items}\n\
Total Cost: {currencies[0]}{total_cost}") 
            elif chmo == "9":
                print(f"Back To Previous Menu\n");break
            elif chmo == "1":
                print(f"Remove Item Selected\n{shopping_cart}\n")
                input("\nWhich Item Would You Like To Remove: ")
            elif chmo == "2":
                print(f"Add Item Selected\n\n{shopping_cart}\n")
                input("\nWhich Item Would You Like To Add: ")
            elif chmo == "3":
                if shopping_cart == "Shopping Cart:\n":
                    print("\nThere Are No Items In Your Shopping Cart")
                    checkend = input("Would You Like To End Session? \
[Y]es/[N]o: ")
                    if checkend.upper() == "Y":
                        print("Session Ended\nGoodbye")
                        session_ended = True;break
                    elif checkend.upper() == "N":
                        print("Back To Checkout\n")
                        continue
                    else:
                        print("Invalid Input")
                else:
                    receipt()
                    session_ended = True;break
            else:
                print("Inavlid Input\n")
    else:
        print("Invalid Input\n")