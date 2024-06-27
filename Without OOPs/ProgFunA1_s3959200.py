
"""
Name: Krishnakanth Srikanth
Student ID: s3959200
The highest part attempted: Part 1, Part 2, Part 3
Any problems in code and requirements that have not met: Nil
Most challenging task and outcome: Being from a Mechanical Engineering background, I found it more challenging to meet the requirements.
                       This project made me learn a lot and helped me grow my knowledge.
"""

"""
This program is for the restaurant ordering system to process customer's order
and is used by the cashiers or the restaurant managers from a restaurant.
"""

# Initializing the required lists
customer_set = {"Kate", "Tom"} # Used set because, sets will not allow duplicate entries to get added to it
available_dish_dict = {"hamburger": 12.5, "coke": 3.0, "pizza": 14.0} # Used dictionary because, we can have the dishes and its cost stored as a key and value pair
rewards_program_customer_set = {"Kate"}
non_rewards_program_customer_set = {"Tom"}
sold_dishes = [None, None, None]
order_cust_list = list(customer_set.copy())
ordered_dish_dict = {}
total_cost_list = []
ordered_quantity = []
service_fee_list = []
cust_history_dict = {}

run = True
while run:
    print("Welcome to the RMIT restaurant ordering system!\n")
    print("##" * 30)
    print("You can choose from the following options: \n"
          "1: Order a meal\n"
          "2: Add/update dishes and prices\n"
          "3: Display existing customers information\n"
          "4: Display existing dishes information\n"
          "5: Add sold-out dishes\n"
          "6: Display the most frequent customer\n"
          "7: Display a customer order history\n"
          "0: Exit the program")
    print("##" * 30, "\n")
    choose_option = int(input("Choose one option:\n"))

# Option 1:
    def order_meal():
        """
        This function is used for ordering menu and print the receipt based on the menu and customer details.
        """
        # Getting input from the user about the customer's order
        user_name = input("Enter the name of the customer [e.g. Huong]: \n").strip()
        order_number = 0
        global customer_set
        global available_dish_dict
        global rewards_program_customer_set
        global non_rewards_program_customer_set
        global order_cust_list
        global ordered_dish_dict
        global total_cost_list
        global ordered_quantity
        global service_fee_list
        global cust_history_dict
        order_cust_list.append(user_name)
        ordered_dish_dict = {}
        service_fee_list = []
        ordered_quantity =[]
        total_cost_list = []

        start_order = True
        while start_order: # Using while loop to make the code block run until failure or the necessary condition is met
            # Checking for the entered dish is correct, its availability and cost
            a = True
            while a:  # Using while loop to run the function until the correct value is entered
                dish_name = input("Enter the dish [enter a valid dish only, e.g. hamburger, coke, pizza]: \n").strip()
                if dish_name not in sold_dishes:
                    if dish_name in available_dish_dict.keys():
                        price = available_dish_dict[dish_name]
                        ordered_dish_dict[dish_name] = [price]
                        a = False
                    else:
                        a = True
                else:
                    print(f"Sorry! {dish_name.title()} is out of stock. Please select other dish or go back to main menu to cancel ordering!")

            # Checking for quantity
            b = True
            while b:  # Using while loop to run the function until the correct value is entered
                quantity = input("Enter the dish quantity [enter a positive integer only, e.g. 1, 2, 3]: \n")
                if quantity <= '0':
                    b = True
                elif not quantity.isdigit():
                    b = True
                else:
                    b = False
                    quantity = int(quantity)
                    ordered_quantity.append(quantity)
                    ordered_dish_dict[dish_name].append(quantity)

            # Checking if user wants to order more
            more_order = True
            while more_order: # Using while loop to make the code block run until failure or the necessary condition is met
                order_more = input("Do you wish to order more?\n").strip()
                if order_more == 'y':
                    a = True
                    while a:  # Using while loop to run the function until the correct value is entered
                        dish_name = input("Enter the dish [enter a valid dish only, e.g. hamburger, coke, pizza]: \n").strip()
                        if dish_name not in sold_dishes:
                            if dish_name in available_dish_dict.keys():
                                price = available_dish_dict[dish_name]
                                ordered_dish_dict[dish_name] = [price]
                                a = False
                            else:
                                a = True
                        else:
                            print(f"Sorry! {dish_name.title()} is out of stock. Please select other dish or go back to main menu to cancel ordering!")

                    # Checking for quantity
                    b = True
                    while b:  # Using while loop to run the function until the correct value is entered
                        quantity = input("Enter the dish quantity [enter a positive integer only, e.g. 1, 2, 3]: \n")
                        if quantity <= '0':
                            b = True
                        elif not quantity.isdigit():
                            b = True
                        else:
                            b = False
                            quantity = int(quantity)
                            ordered_quantity.append(quantity)
                            ordered_dish_dict[dish_name].append(quantity)

                elif order_more == 'n':
                    more_order = False
                else:
                    more_order = True

            if not more_order:
                c = True
                while c:  # Using while loop to run the function until the correct value is entered
                    if user_name in customer_set and user_name in rewards_program_customer_set:
                        c = False
                        service_fee = 0
                        flag = True
                        while flag:
                            for dis, amt in ordered_dish_dict.items():
                                total_cost = (amt[0] * amt[1]) + service_fee
                                total_cost_list.append(total_cost)
                            flag = False

                    else:
                        customer_set.add(user_name)
                        register_rewards_program = input("The customer is not in the rewards program. Does the customer want to join the rewards program [enter y or n]? \n").strip()

                        if register_rewards_program == 'y':
                            c = False
                            rewards_program_customer_set.add(user_name)
                            print("Successfully add the customer to the rewards program.\n")
                            service_fee = 0
                            flag = True
                            while flag:
                                for dis, amt in ordered_dish_dict.items():
                                    total_cost = (amt[0] * amt[1]) + service_fee
                                    total_cost_list.append(total_cost)
                                flag = False
                        elif register_rewards_program == 'n':
                            c = False
                            non_rewards_program_customer_set.add(user_name)
                            check = True
                            while check:
                                for dis, amt in ordered_dish_dict.items():
                                    service_fee = amt[0] * amt[1] * 0.1
                                    service_fee_list.append(service_fee)
                                    total_cost = (amt[0] * amt[1]) + service_fee
                                    total_cost_list.append(total_cost)
                                    check = False
                        else:
                            c = True

                order_dict = {}
                order_dict = zip(ordered_dish_dict, ordered_quantity)
                # Printing the receipt for the customer's order
                print("**" * 30)
                print(f"Receipt of Customer {user_name}")
                print("**" * 30)
                food_desc = ""
                some = True
                while some:
                    for d_name, quant in order_dict:
                        print(f"{str(d_name).ljust(9)}: {str(available_dish_dict[d_name]).rjust(20)} (AUD) x {str(quant)}")
                        food_desc += str(quant) + " x " + str(d_name) + " "
                        some = False

                if user_name in non_rewards_program_customer_set:
                    print(f"Service fee:  {str(round(sum(service_fee_list), 2)).rjust(22)}(AUD)")
                else:
                    service_fee = 0
                    print(f"Service fee:  {str(service_fee).rjust(22)}(AUD)")

                print("--" * 30)
                print(f"Total cost: {round(sum(total_cost_list), 3):>23} (AUD)\n")
                history = {"Dishes": food_desc, "Total Cost": sum(total_cost_list)}
                if user_name not in cust_history_dict.keys():
                    cust_history_dict[user_name] = []
                cust_history_dict[user_name].append(history)
                start_order = False

# -------------------------------------

# Option 2:
    def add_update_dish_cost():
        """
        This function helps the user's add/update the menu list with the dish name and price of the dishes.
        """
        input_list = input("Enter the dish name along with its price, [e.g. tea: 2.0]:\n").strip()

        # Splitting the string based on , we get key value pairs
        final_list = input_list.split(",")

        # Creating an empty dictionary
        add_updt_dis_cos = {}

        for i in final_list:
            # Get Key Value pairs separately to store in dictionary
            key_value = i.split(":")

            # Adding values to the dictionary based on the key
            key = key_value[0]
            add_updt_dis_cos[key] = key_value[1]

        # Looping through the items in the created dictionary
        for dish, cost in add_updt_dis_cos.items():
            dish = str(dish).strip()
            cost = float(cost)

            if dish in available_dish_dict.keys():
                available_dish_dict[dish] = cost

            elif dish not in available_dish_dict:
                available_dish_dict[dish] = cost

        print("Dish list with price after adding/updating: ", available_dish_dict)

# -------------------------------------

# Option 3:
    def existing_cust_info():
        """
        This function is used to retrieve customer information like name and
        whether the customer has signed up in rewards program or not.
        """
        global customer_set
        global rewards_program_customer_set
        global non_rewards_program_customer_set
        customer_list = list(customer_set).copy()
        print(customer_list)
        rewards = "Rewards Program Customer"
        non_rewards = "Not a Rewards Program Customer"

        print("****************************")
        print("Existing Customer Details\n")
        for i in range(len(customer_set)):
            if customer_list[i] in rewards_program_customer_set:
                print(f"{str(customer_list[i]).ljust(10)}: {rewards.rjust(5)}")
            else:
                print(f"{str(customer_list[i]).ljust(10)}: {non_rewards.rjust(5)}")
        print("****************************")

# -------------------------------------

# Option 4:
    def existing_dish_info():
        """
        This function is used to get information on the available dishes along with its cost.
        """
        global available_dish_dict

        print("****************************")
        print("Existing Dish Details\n")

        for dish, cost in available_dish_dict.items():
            print(f"{dish.ljust(9)}: {str(cost).rjust(5)} (AUD)")
        print("****************************")

# -------------------------------------

# Option 5:
    def sold_out_dishes():
        """
        This function is used to get details on the sold out dishes.
        """
        global sold_dishes
        sold_input = input("Enter the dishes that are sold out: \n").strip()
        sold_input_list = [i.strip() for i in sold_input.split(',')]

        for i, obj in enumerate(sold_input_list):
            if obj in available_dish_dict.keys():
                sold_dishes[i] = obj
            else:
                print("The entered dishes are invalid and they will not be added")

# -------------------------------------

# Option 6:
    def freq_cust():
        """
        This function is used to get the details of the most frequent customer to the restaurant.
        """
        global order_cust_list

        freq_customer = max(order_cust_list, key=order_cust_list.count)
        orders = order_cust_list.count(freq_customer)
        print(f"{freq_customer} has the maximum number of orders equal to {orders}!")

# -------------------------------------

# Option 7:
    def cust_order_hist(user_name):
        """
        This function is used to retrieve the order history of a particular customer.
        """
        global ordered_dish_dict

        print(f"This is the order history of {user_name}")
        print("Dishes".rjust(35), "Total Cost".rjust(35))
        ctr = 1
        for k in cust_history_dict[user_name]:
            print("Order", str(ctr).ljust(10), str(k['Dishes']).rjust(20), str(k['Total Cost']).rjust(28))
            ctr += 1

# -------------------------------------

# Option 0:
    def exit_program():
        """
        This function helps to exit the program based on user's input.
        """
        global run
        run = False

# -------------------------------------

# Functions created for the options available to select on the home screen
    if choose_option == 1:
        start = False
        order_meal()
    elif choose_option == 2:
        add_update_dish_cost()
    elif choose_option == 3:
        existing_cust_info()
    elif choose_option == 4:
        existing_dish_info()
    elif choose_option == 5:
        sold_out_dishes()
    elif choose_option == 6:
        freq_cust()
    elif choose_option == 7:
        correct = True
        while correct:
            check_cust = input("Please enter a customer name for checking order history:\n")
            if check_cust not in customer_set:
                correct = True
            else:
                correct = False
        cust_order_hist(check_cust)
    elif choose_option == 0:
        exit_program()
