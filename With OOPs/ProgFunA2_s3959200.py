"""
Name: Krishnakanth Srikanth
Student ID: s3959200
The highest part attempted: PASS Level, CREDIT Level, DI Level and HD Level
Most challenging task and outcome: Being from a Mechanical Engineering background, I found it more challenging to meet the requirements.
                       This project made me learn a lot and helped me grow my knowledge. This project has a lot of new contents and has helped me
                       in growing my knowledge and idea to think out of box at some situations. Moreover, this has created a great interest in me
                       to do more projects, learn and grow.
                       Lesson I learned through this project is: "Never give up and with hardwork, determination anything is possible by anyone!"
"""

# Importing the required packages
import sys
import os


# Creating Exception classes
class ExceptionError(Exception):
    pass


class ValueError(ExceptionError):
    pass


class ItemNameError(ExceptionError):
    pass


class RewardsRegistrationError(ExceptionError):
    pass


class RewardsProgramError(ExceptionError):
    pass


# Creating Customer class
class Customer:
    """
    This class is created to handle all the customers.
    """
    def __init__(self, cust_id="", cust_type="", cust_name=""):
        """
        This function is the constructor for class Customer.
        """
        self.__cust_id = cust_id
        self.cust_type = cust_type
        self.__cust_name = cust_name

    @property
    def cust_id(self):
        """
        This function is the getter method for customer id.
        """
        return self.__cust_id

    @cust_id.setter
    def cust_id(self, cust_id):
        """
        This function is the setter method for customer id.
        """
        self.__cust_id = cust_id

    @property
    def cust_name(self):
        """
        This function is the getter method for customer name.
        """
        return self.__cust_name

    @cust_name.setter
    def cust_name(self, cust_name):
        """
        This function is the setter method for customer name.
        """
        self.__cust_name = cust_name

    def get_service_fee(self, cost):
        """
        This function is the getter method for service fee for the customers.
        """
        pass

    def get_discount(self, cost):
        """
        This function is the getter method for discount of the customers.
        """
        pass

    # def display_info(self):
    #     print(f'ID: {self.cust_id}, Type: {self.cust_type}, Name: {self.cust_name}')

    def display_info(self):
        """
        This function is used to display the details of all the customers.
        """
        for i in range(0, len(operations.customer_list)):
            print(f'ID: {operations.customer_list[i].cust_id}, Type: {self.cust_type}, Name: {operations.customer_list[i].cust_name}')


# Creating BronzeCustomer class
class BronzeCustomer(Customer):
    """
    This class is created to handle Bronze customers.
    """
    __service_fee_rate = 0.1

    def __init__(self, cust_id="", cust_type="", cust_name="", service_fee_rate=0.1):
        """
        This function is the constructor for class BronzeCustomer.
        """
        super().__init__(cust_id, cust_type, cust_name)
        self.service_fee_rate = service_fee_rate

    @staticmethod
    def get_service_fee_rate():
        """
        This function is the getter method for service fee rate of Bronze customers.
        """
        return BronzeCustomer.__service_fee_rate

    def get_service_fee(self, cost):
        """
        This function is the getter method for service fee of Bronze customers.
        """
        updated_service_fee_rate = round(cost * BronzeCustomer.get_service_fee_rate(), 2)
        return updated_service_fee_rate

    # Option 5:
    @staticmethod
    def set_service_fee_rate():
        """
        This function is the setter method for service fee for all the Bronze customers.
        """
        value = operations.get_positive_float("Enter a value to set the service fee for all bronze customers: \n")
        BronzeCustomer.__service_fee_rate = value

    def get_discount(self, cost):
        """
        This function is the getter method for discount of Bronze customers.
        """
        bronze_discount = 0
        return bronze_discount

    def display_info(self):
        """
        This function is used to display details of Bronze customers.
        """
        for i in range(0, len(operations.customer_list)):
            if operations.customer_list[i].cust_type == "B":
                print(f'ID: {operations.customer_list[i].cust_id}, Type: {self.cust_type}, Name: {operations.customer_list[i].cust_name}')


# Creating SilverCustomer class
class SilverCustomer(Customer):
    """
    This class is created to handle Silver customers..
    """
    def __init__(self, cust_id="", cust_type="", cust_name=""):
        """
        This function is the constructor for class SilverCustomer.
        """
        super().__init__(cust_id, cust_type, cust_name)

    def get_service_fee(self, cost):
        """
        This function is the getter method for service fee of Silver customers.
        """
        service_fee_rate = 0
        return service_fee_rate

    def get_discount(self, cost):
        """
        This function is the getter method for discount of Silver customers.
        """
        silver_discount = 0
        return silver_discount

    def display_info(self):
        """
        This function is used to display details of Silver customers.
        """
        for i in range(0, len(operations.customer_list)):
            if operations.customer_list[i].cust_type == "S":
                print(f'ID: {operations.customer_list[i].cust_id}, Type: {self.cust_type}, Name: {operations.customer_list[i].cust_name}')


# Creating GoldCustomer class
class GoldCustomer(Customer):
    """
    This class is created to handle Gold customers.
    """
    def __init__(self, cust_id="", cust_type="", cust_name="", discount_rate=0.08):
        """
        This function is the constructor for class GoldCustomer.
        """
        super().__init__(cust_id, cust_type, cust_name)
        self.__discount_rate = discount_rate

    @property
    def discount_rate(self):
        """
        This function is the getter method for discount rate.
        """
        return self.__discount_rate

    @discount_rate.setter
    def discount_rate(self,value):
        self.__discount_rate = value

    def get_service_fee(self, cost):
        """
        This function is the getter method for service fee of Gold customers.
        """
        gold_service_fee = 0
        return gold_service_fee

    def get_discount(self, cost):
        """
        This function is the getter method for discount.
        """
        discount = self.discount_rate * cost
        return discount
    #
    # def find(self):
    #     input_id = operations.get_input_for_set_discount()
    #     customer_finder = operations.find_customers(input_id)
    #     if customer_finder is None:
    #         print("None")
    #     else:
    #         self.discount_rate
    #     goldCustomer.set_discount(input_id, discount_value)

    # Option 6:
    def set_discount(self, input_id, value):
        """
        This function is the setter method for discount.
        """
        #input_id = operations.get_input_for_set_discount()
        customer_finder = operations.find_customers(input_id)
        if customer_finder is None:
            print("No results found!")
        else:
            if customer_finder.cust_type == 'G':
                self.discount_rate = value
        operations.customer_list.append(self.discount_rate)
        print(
            f'ID: {customer_finder.cust_id}, Type: {customer_finder.cust_type}, Name: {customer_finder.cust_name}, Discount: {self.discount_rate}')

    def display_info(self):
        """
        This function is used to display the details of the Gold customers.
        """
        for i in range(0, len(operations.customer_list)):
            if operations.customer_list[i].cust_type == "G":
                print(f'ID: {operations.customer_list[i].cust_id}, Type: {self.cust_type}, Name: {operations.customer_list[i].cust_name}, Service Fee Rate: {str(0)}, Discount: {operations.customer_list[i].discount_rate}')


# Creating Items class
class Items:
    """
    This class is created to handle Items.
    """
    def __init__(self, item_id="", item_type="Item", item_name="", item_price=0):
        """
        This function is the constructor of class Items.
        """
        self.__item_id = item_id
        self.item_type = item_type
        self.__item_name = item_name
        self.__item_price = item_price

    @property
    def item_id(self):
        """
        This function is the getter method for item id.
        """
        return self.__item_id

    @item_id.setter
    def item_id(self, item_id):
        """
        This function is the setter method for item id.
        """
        self.__item_id = item_id

    @property
    def item_name(self):
        """
        This function is the getter method for item name.
        """
        return self.__item_name

    @item_name.setter
    def item_name(self, item_name):
        """
        This function is the setter method for item name.
        """
        self.__item_name = item_name

    @property
    def item_price(self):
        """
        This function is the getter method for item price.
        """
        return self.__item_price

    @item_price.setter
    def item_price(self, item_price):
        """
        This function is the setter method for item price.
        """
        self.__item_price = item_price

    def display_info(self):
        """
        This function is used to display the details of the items available in the restaurant.
        """
        for i in range(0, len(operations.items_list)):
            print(f'ID: {operations.items_list[i].item_id}, Type: {self.item_type}, Name: {operations.items_list[i].item_name}, Price: ${operations.items_list[i].item_price}')


# Creating FoodDish class
class FoodDish(Items):
    """
    This class is created to handle FoodDish.
    """
    def __init__(self, item_id="", item_type="FoodDish", item_name="", item_price=0):
        """
        This function is the constructor for class FoodDish
        """
        super().__init__(item_id, item_type, item_name, item_price)

    def display_info(self):
        """
        This function is used to display FoodDish details.
        """
        for i in range(0, len(operations.items_list)):
            if operations.items_list[i].item_type == 'F':
                print(f'ID: {operations.items_list[i].item_id}, Type: {self.item_type}, Name: {operations.items_list[i].item_name}, Price: ${operations.items_list[i].item_price}')


# Creating Drink class
class Drink(Items):
    """
    This class is created to handle Drinks.
    """
    def __init__(self, item_id="", item_type="Drink", item_name="", item_price=0):
        """
        This funtion is the constructor of class Drink.
        """
        super().__init__(item_id, item_type, item_name, item_price)

    def display_info(self):
        """
        This function is used to display Drink details.
        """
        for i in range(0, len(operations.items_list)):
            if operations.items_list[i].item_type == 'D':
                print(f'ID: {operations.items_list[i].item_id}, Type: {self.item_type}, Name: {operations.items_list[i].item_name}, Price: ${operations.items_list[i].item_price}')


# Creating Banquet class
class Banquet(Items):
    """
    This class is created to handle Banquet details
    """
    def __init__(self, item_id="", item_type="Banquet", item_name="", item_price=0, item_components=[]):
        """
        This function is the constructor for class Banquet
        """
        super().__init__(item_id, item_type, item_name, item_price)
        self.__item_components = item_components

    @property
    def item_components(self):
        """
        This is the getter method for item components
        """
        return self.__item_components

    @item_components.setter
    def item_components(self, *value):
        """
        This is the setter method for item components
        """
        for i in value:
            self.item_components.append(i)

    def display_info(self):
        """
        This function is used to display Banquet details
        """
        for i in range(0, len(operations.items_list)):
            if operations.items_list[i].item_type == 'B':
                print(f'ID: {operations.items_list[i].item_id}, Type: {self.item_type}, Name: {operations.items_list[i].item_name}, Components: {operations.items_list[i].item_components}, Price: ${operations.items_list[i].item_price}')


# Creating Orders class
class Orders:
    """
    This class is created to handle all Orders.
    """
    def __init__(self, cust_name="", item_name="", quantity=0):
        self.cust_name = cust_name
        self.item_name = item_name
        self.quantity = quantity

    def compute_cost(self, username, item, quantity):
        """
        This function is used to compute the cost of customer. ie Display original cost (the total cost without service fee and discount),
        the service fee, and the discount.
        """
        compute_cost_list = []
        for i in operations.customer_list:
            if i.cust_type == 'G':
                if username in i.cust_name:
                    discount = i.discount_rate
                    service_fee = 0
                    cust_type = "G"
                    compute_cost_list.append(username)
                    compute_cost_list.append(cust_type)
                    compute_cost_list.append(discount)
                    compute_cost_list.append(service_fee)
            elif i.cust_type == 'S':
                if username in i.cust_name:
                    discount = 0
                    service_fee = 0
                    cust_type = "S"
                    compute_cost_list.append(username)
                    compute_cost_list.append(cust_type)
                    compute_cost_list.append(discount)
                    compute_cost_list.append(service_fee)
            else:
                if username in i.cust_name:
                    discount = 0
                    service_fee = 0.1
                    cust_type = "B"
                    compute_cost_list.append(username)
                    compute_cost_list.append(cust_type)
                    compute_cost_list.append(discount)
                    compute_cost_list.append(service_fee)

        for j in operations.items_list:
            if item in j.item_name or item in j.item_id:
                price = j.item_price
                compute_cost_list.append(item)
                compute_cost_list.append(price)
        if compute_cost_list[1] == 'G':
            discounted_price = float(compute_cost_list[5]) * float(compute_cost_list[2])
            compute_cost_list.append(discounted_price)
        else:
            discounted_price = float(0)
            compute_cost_list.append(discounted_price)
        if quantity > 0 and type(quantity) == int:
            total_cost = float(compute_cost_list[5]) * float(quantity)
            compute_cost_list.append(quantity)
            compute_cost_list.append(total_cost)
        #print(compute_cost_list[8], compute_cost_list[3], compute_cost_list[7])
        return compute_cost_list


# Creating class for Records
class Records:
    """
    This class is used to handle all the records.
    """

    customer_list = []
    found_customers = []
    id_customer_dict = {}
    customer_discount_dict = {}
    found_items = []
    id_item_dict = {}
    id_price_dict = {}
    item_price_dict = {}
    item_type_dict = {}
    components_dict = {}
    items_list = []
    customer_orders_list = []
    id_value = 0
    customer_names_list = []
    input_order_filename = ""
    item_type_list = []
    customer_count_list = []
    cname = []

    def add_customer_to_list(self, customer_id, customer_type, customer_name):
        """
        This function is used to add customer details to a list of type class GoldCustomer or SilverCustomer or BronzeCustomer.
        """
        if customer_type == 'G':
            cus_lis = GoldCustomer(customer_id, customer_type, customer_name)
        elif customer_type == 'S':
            cus_lis = SilverCustomer(customer_id, customer_type, customer_name)
        else:
            cus_lis = BronzeCustomer(customer_id, customer_type, customer_name)
        self.customer_list.append(cus_lis)

    def add_items_to_list(self, item_id, item_type, item_name, item_price):
        """
        This function is used to add item details to a list of type class FoodDish or Drink.
        """
        #item_list = Items(item_id, item_type, item_name, item_price)
        if item_type == 'F':
            item_list = FoodDish(item_id, item_type, item_name, item_price)
        elif item_type == 'D':
            item_list = Drink(item_id, item_type, item_name, item_price)
        self.items_list.append(item_list)

    def add_items_banquets_to_list(self, item_id, item_type, item_name,item_price, item_components):
        """
        This function is used to add item details to a list of type class Banquet.
        """
        item_list = Banquet(item_id, item_type, item_name, item_price, item_components)
        self.items_list.append(item_list)

    def add_orders_to_list(self, cust_name, item_name, quantity):
        """
        This function is used to add order details to a list of type class Order.
        """
        cus_order_list = Orders(cust_name, item_name, quantity)
        self.customer_orders_list.append(cus_order_list)

    # Add new customers to customers.txt
    def append_customers(self, customer_filename, inputs_to_append):
        """
        This function is used to append values to the customer.txt file.
        """
        try:
            with open(customer_filename, "a+") as input_customers_file:
                appending = False
                # Move read cursor to the start of file.
                input_customers_file.seek(0)
                # Check if file is not empty
                line_from_input_customers_file = input_customers_file.read()
                if len(line_from_input_customers_file) > 0:
                    appending = True
                # If file is not empty then append '\n' before first line for
                # other lines always append '\n' before appending line
                if appending is True:
                    input_customers_file.write("\n")
                else:
                    appending = True
                # Iterate over each string in the list
                for line in inputs_to_append:
                    # Append element at the end of file
                    input_customers_file.write(line)
        except FileNotFoundError:
            print("No file found!")

    # Reading the customer.txt file
    def read_customers(self, customer_filename):
        """
        This function is used to read the customer.txt file, and get the details of the available customers in the restaurant.
        """
        try:
            input_customers_file = open(customer_filename, 'r')
            line_from_input_customers_file = input_customers_file.readline()
            while line_from_input_customers_file:
                line = line_from_input_customers_file.strip().split(",")
                cust_list = []
                for k in line:
                    line_split = k.split(":")
                    cust_list.append(line_split[1].strip())
                if len(cust_list) > 3:
                    customer_id = cust_list[0]
                    customer_type = cust_list[1]
                    customer_name = cust_list[2]
                    discount_rate = float(cust_list[3])
                else:
                    customer_id = cust_list[0]
                    customer_type = cust_list[1]
                    customer_name = cust_list[2]
                if customer_type == 'G':
                    gold_cust = GoldCustomer(customer_id, customer_type, customer_name, discount_rate)
                    self.customer_list.append(gold_cust)
                    self.customer_discount_dict[customer_name] = discount_rate
                    # self.customer_type_list.append(GoldCustomer(customer_id, customer_type, customer_name, float(discount_rate)))
                elif customer_type == 'S':
                    silver_cust = SilverCustomer(customer_id, customer_type, customer_name)
                    self.customer_list.append(silver_cust)
                else:
                    bronze_cust = BronzeCustomer(customer_id, customer_type, customer_name)
                    self.customer_list.append(bronze_cust)

                # customer_id = cust_list[0]
                # customer_type = cust_list[1]
                # customer_name = cust_list[2:]
                # if len(customer_name) == 2:
                #     self.customer_discount_dict[customer_name] = discount_rate
                # if customer_type == 'G':
                #     self.customer_type_list.append(GoldCustomer(customer_id, customer_type, customer_name, float(discount_rate)))
                # elif customer_type == 'S':
                #     self.customer_type_list.append(SilverCustomer(customer_id, customer_type, customer_name))
                # else:
                #     self.customer_type_list.append(BronzeCustomer(customer_id, customer_type, customer_name))
                # self.add_customer_to_list(customer_id, customer_name, customer_type)
                self.id_customer_dict[customer_id] = customer_name
                operations.all_cust_list.append(customer_name)
                line_from_input_customers_file = input_customers_file.readline()
            input_customers_file.close()
        except FileNotFoundError:
            print(f"Exiting the program as the mentioned file {operations.customer_filename} is missing!!")

    # Find a particular customer
    def find_customers(self, search_value):
        """
        This function is used to find and get the details of the available customer in the restaurant, which is passed as input.
        """
        for i in range(len(self.customer_list)):
            if search_value == self.customer_list[i].cust_name or search_value == self.customer_list[i].cust_id:
                return self.customer_list[i]
            elif search_value != self.customer_list[i].cust_name or search_value != self.customer_list[i].cust_id:
                if i == len(self.customer_list) - 1:
                    return None

    # Option 2:
    # Display Customer Information
    def display_customers(self):
        """
        This function is used to display the details of the existing customers in the restaurant.
        """
        print("Below are the details of existing customers at RMIT Restaurant")
        records.read_customers(operations.customer_filename)
        for i in self.customer_list:
            if isinstance(i, GoldCustomer):
                print(
                    f'ID: {i.cust_id}, Type: {i.cust_type}, Name: {i.cust_name}, Service Fee Rate: {str(0)}, Discount: {i.discount_rate}')
            else:
                print(f'ID: {i.cust_id}, Type: {i.cust_type}, Name: {i.cust_name}')

    # Reading the items.txt file
    def read_items(self, items_filename):
        """
        This function is used to read the items.txt file, and get the details of the available items in the restaurant.
        """
        try:
            input_items_file = open(items_filename, 'r')
            line_from_input_items_file = input_items_file.readline()
            while line_from_input_items_file:
                line = line_from_input_items_file.strip().split(",")
                it_list = []
                for k in line:
                    line_split = k.split(":")
                    it_list.append(line_split[1].strip())
                item_id = it_list[0]
                item_type = it_list[1]
                item_name = it_list[2]
                if item_type == "B":
                    components = it_list[3].split(" ")
                    components = list(components)
                    item_price = 0
                    for i in components:
                        if i in self.id_item_dict.keys():
                            component = self.id_item_dict[i]
                        else:
                            component = i
                        if self.item_type_dict[component] != 'D':
                            cost = self.item_price_dict[component]
                            item_price += float(cost)
                    self.components_dict[item_name] = components
                    self.item_type_dict[item_name] = item_type
                    comp_list = []
                    for x in range(0, len(components)):
                        food_type = operations.find_items(components[x])
                        if isinstance(food_type, (FoodDish, Drink)):
                            a = food_type.item_type
                            comp_list.append(a)
                        else:
                            b = food_type.item_type
                            comp_list.append(b)
                    d_count = comp_list.count('D')
                    f_count = comp_list.count('F')
                    if f_count == 0 or d_count == 0:
                        print(f"\nBanquet {item_id} is not valid! Each banquet needs to have atleast 1 food dish and 1 drink!")
                    self.add_items_banquets_to_list(item_id, item_type, item_name, item_price, components)
                else:
                    item_price = it_list[3]
                    self.add_items_to_list(item_id, item_type, item_name, item_price)
                self.item_price_dict[item_name] = item_price
                self.id_price_dict[item_id] = item_price
                self.item_type_dict[item_name] = item_type
                self.id_item_dict[item_id] = item_name

                line_from_input_items_file = input_items_file.readline()
            input_items_file.close()
        except FileNotFoundError:
            print(f"Exiting the program as the mentioned file: {operations.items_filename} is missing!!")

    # Find a particular item
    def find_items(self, search_value):
        """
        This function is used to fetch the details about the item passed as an input which is available in the restaurant.
        """
        for i in range(len(self.items_list)):
            if search_value == self.items_list[i].item_name or search_value == self.items_list[i].item_id:
                return self.items_list[i]
            elif search_value != self.items_list[i].item_name or search_value != self.items_list[i].item_id:
                if i == len(self.items_list) - 1:
                    return None

    # Option 3:
    # Display Items Information
    def display_items(self):
        """
        This function is used to display the details of the all the items available in the restaurant menu.
        """
        print("Below are the details of existing items at RMIT Restaurant")
        records.read_items(operations.items_filename)
        for i in range(0, len(self.items_list)):
            if self.items_list[i].item_type == 'B':
                print(f'ID: {self.items_list[i].item_id}, Type: {self.items_list[i].item_type}, Name: {self.items_list[i].item_name}, Components: {self.items_list[i].item_components}, Price: ${self.items_list[i].item_price}')
            else:
                print(f'ID: {self.items_list[i].item_id}, Type: {self.items_list[i].item_type}, Name: {self.items_list[i].item_name}, Price: ${self.items_list[i].item_price}')

    # Reading orders.txt file
    def read_orders_file(self, order_filename):
        """
        This function is used to read the orders.txt file, and get the order details made by the customers in the restaurant.
        """
        read = True
        try:
            input_orders_file = open(order_filename, "r")
            line_from_input_orders_file = input_orders_file.readline()
            while line_from_input_orders_file:
                line = line_from_input_orders_file.split(",")
                orders_list = []
                for i in line:
                    line_split = i.split(":")
                    orders_list.append(line_split[1].strip())
                if orders_list[0] in self.id_customer_dict.keys():
                    cust_name = self.id_customer_dict[orders_list[0]]
                else:
                    cust_name = orders_list[0]
                orders = orders_list[1].split(" ")
                if orders[0] in self.id_item_dict.keys():
                    item_name = self.id_item_dict[orders[0]]
                else:
                    item_name = orders[0]
                quantity = orders[1]
                self.add_orders_to_list(cust_name, item_name, quantity)
                line_from_input_orders_file = input_orders_file.readline()
            input_orders_file.close()
            return read
        except FileNotFoundError:
            print("Cannot load the order file. Go back to the main menu")

    # Option 7:
    # Display Orders Information
    def display_orders(self):
        """
        This function is used to display the order details made by the customers in the restaurant.
        """
        read_value = records.read_orders_file(operations.orders_filename)
        if read_value:
            print("Display all existing orders")
            for i in range(0, len(self.customer_orders_list)):
                print(f'{self.customer_orders_list[i].cust_name}, {self.customer_orders_list[i].item_name}, {self.customer_orders_list[i].quantity}')


# Creating class for performing operations
class Operations(Records):
    """
    This class is used to manage all the functionalities of the restaurant.
    """
    # customer_filename = "E:/Programming Fundamentals/Assignment 2/Draft_Ass2/Assignment_2_files/credit_level/customers.txt"
    # items_filename = "E:/Programming Fundamentals/Assignment 2/Draft_Ass2/Assignment_2_files/credit_level/items.txt"
    customer_filename = "customers.txt"
    items_filename = "items.txt"
    orders_filename = ""
    # orders_filename = "E:/Programming Fundamentals/Assignment 2/Draft_Ass2/Assignment_2_files/di_level/orders.txt"
    enrolled_cust_dict = {}
    all_cust_list = []
    cust_history_dict = {}
    sold_dishes = [None, None, None]
    sold_input_list = []
    sold_input_dict = {}
    ordered_dish_dict = {}
    total_cost_list = []
    quantity_list = []

    def __init__(self):
        """
        This is the constructor function for the class Operations.
        """
        self.run = True

    @staticmethod
    def get_str(prompt):
        """
        This function is used get input values from customer.
        """
        sys.stdout.write(prompt)
        sys.stdout.flush()
        value = sys.stdin.readline().strip()
        while len(value) == 0:
            sys.stdout.write("Input cannot be blank. Re-enter: \n")
            sys.stdout.flush()
            value = sys.stdin.readline().strip()
        return value

    def get_float(self, prompt):
        """
        This function is used to get input values from the customer.
        """
        value = None
        while value == None:
            try:
                value = float(self.get_str(prompt))
            except:
                prompt = "Input must be a positive number. Re-enter: \n"
        return value

    def get_positive_float(self, prompt):
        """
        This function is used to get input values from the customer.
        """
        value = self.get_float(prompt)
        while value < 0:
            value = self.get_float("Input must be a positive number. Re-enter: \n")
        return value

    def get_item_name(self):
        """
        This function is used to get and check the item name available in the restaurant, passed as input.
        """
        b = True
        while b:
            try:
                # item = input(
                #     "Enter the name or ID of the item [enter a valid item only, e.g. hamburger (ID: 1), coke (ID: 5), pizza (ID: 2)]: \n").strip()
                item = self.get_str("Enter the name or ID of the item [enter a valid item only, e.g. hamburger (ID: 1), coke (ID: 5), pizza (ID: 2)]: \n").strip()
                if item not in self.sold_input_dict.keys() and item not in self.sold_input_dict.values():
                    if item not in self.id_item_dict.keys() and item not in self.id_item_dict.values():
                        b = True
                        raise ItemNameError("Item is invalid. Please enter a valid item!")
                    elif item in self.id_item_dict.keys():
                        b = False
                        item_name = self.id_item_dict[item]
                    else:
                        item_name = item
                    return item_name
                raise ItemNameError(f"Sorry! {item.title()} is out of stock. Please select other dish or go back to main menu to cancel ordering!")
            except ItemNameError as e:
                print(e)

    def get_quantity(self):
        """
        This function is used to get and check the quantity value passed as an input.
        """
        c = True
        while c:
            try:
                # quantity = input("Enter the item quantity [enter a positive integer only, e.g. 1, 2, 3]: \n")
                quantity = self.get_str("Enter the item quantity [enter a positive integer only, e.g. 1, 2, 3]: \n")
                if quantity <= '0':
                    c = True
                    raise ValueError("Invalid value, enter only positive integer > 0!!")
                elif not quantity.isdigit():
                    c = True
                    raise ValueError("Invalid value, enter only positive integer > 0!!")
                else:
                    c = False
                    quantity = int(quantity)
                    return quantity
            except ValueError as e:
                print(e)

    def order_more(self):
        """
        This function is used to check if the customer wants to order more than one item or not.
        """
        d = True
        while d:
            try:
                order_more_assert = self.get_str("Do you wish to order more? \n").strip()
                if order_more_assert == 'y' or order_more_assert == 'n':
                    d = False
                else:
                    d = True
                    raise ValueError("Invalid value, enter only 'y' for 'Yes' and 'n' for 'No'!")
                return order_more_assert
            except ValueError as e:
                print(e)

    def get_item_price(self):
        """
        This function is used to fetch the price of the item entered
        """
        for item, quant in self.ordered_dish_dict.items():
            if item in self.id_price_dict.keys():
                price = self.id_price_dict[item]
            elif self.item_type_dict[item] == 'B':
                price = 0
                components = self.components_dict[item]
                for i in components:
                    if i in self.id_item_dict.keys():
                        component = self.id_item_dict[i]
                    else:
                        component = i
                    if self.item_type_dict[component] != 'D':
                        cost = self.item_price_dict[component]
                        price += float(cost)
                    # self.item_price_dict[item_name].append(price)
                    self.item_price_dict[item] = [price]
            else:
                price = self.item_price_dict[item]
            # self.enrolled_cust_dict[user_name].append(price)
            self.ordered_dish_dict[item].append(price)

    # Option 1:
    def order_meal(self, user_name, item_name, quantity):
        """
        This function is used to order meals in the restaurant.
        """
        # Get the price and quantity of the order
        self.get_item_price()
        # Calculate total cost of the order
        flag = True
        while flag:
            for key, value in self.ordered_dish_dict.items():
                total_cost = int(value[0]) * float(value[1])
                self.total_cost_list.append(total_cost)
            flag = False
        # Check for username
        a = True
        if user_name not in self.id_customer_dict.values() and user_name not in self.id_customer_dict.keys():
            customer = "New"
            # Getting ID value
            for i in range(0, len(self.customer_list)):
                self.id_value = int(self.customer_list[i].cust_id) + 1

            # Enrollment for Rewards program
            while a:
                try:
                    register_rewards_program = input("This is a new customer. Does the customer want to join the rewards program [enter y or n]? \n").strip()
                    if register_rewards_program == 'y':
                        z = True
                        while z:
                            try:
                                rewards_program_type = input("What type of rewards program the customer wants? \n").strip()
                                if rewards_program_type == 'S':
                                    z = False
                                    a = False
                                    random_cust_id = self.id_value
                                    cust_type = "S"
                                    registration_fee = 100.0
                                    discount = 0.0
                                    service_fee = 0.0
                                    records.append_customers(self.customer_filename, ["id: ", str(random_cust_id), ", type: ", cust_type, ", name: ", user_name])
                                    self.enrolled_cust_dict[user_name] = [cust_type, registration_fee, service_fee, discount]
                                elif rewards_program_type == 'G':
                                    z = False
                                    a = False
                                    random_cust_id = self.id_value
                                    cust_type = "G"
                                    registration_fee = 300.0
                                    # cost = self.item_price_dict[item_name]
                                    cost = sum(self.total_cost_list)
                                    discount_rate = goldCustomer.discount_rate
                                    discount = goldCustomer.get_discount(float(cost))
                                    service_fee = 0.0
                                    records.append_customers(self.customer_filename, ["id: ", str(random_cust_id), ", type: ", cust_type, ", name: ", user_name, ", discount: ", str(discount_rate)])
                                    self.enrolled_cust_dict[user_name] = [cust_type, registration_fee, service_fee, discount]
                                else:
                                    z = True
                                    raise RewardsProgramError("Invalid value, enter only G or S!!")
                            except RewardsProgramError as e:
                                print(e)

                    elif register_rewards_program == 'n':
                        random_cust_id = self.id_value
                        a = False
                        cust_type = "B"
                        # cost = self.item_price_dict[item_name]
                        cost = sum(self.total_cost_list)
                        service_fee = bronzeCustomer.get_service_fee(float(cost))
                        discount = 0.0
                        registration_fee = 0.0
                        records.append_customers(self.customer_filename, ["id: ", str(random_cust_id), ", type: ", cust_type, ", name: ", user_name])
                        self.enrolled_cust_dict[user_name] = [cust_type, registration_fee, service_fee, discount]
                    else:
                        a = True
                        raise RewardsRegistrationError("Invalid value, enter only y or n!!")
                except RewardsRegistrationError as e:
                    print(e)

            # # Fetching the price of the item entered
            # if self.item_type_dict[item_name] == 'B':
            #     price = 0
            #     components = self.components_dict[item_name]
            #     for i in components:
            #         if i in self.id_item_dict.keys():
            #             component = self.id_item_dict[i]
            #         else:
            #             component = i
            #         if self.item_type_dict[component] != 'D':
            #             cost = self.item_price_dict[component]
            #             price += float(cost)
            #        # self.item_price_dict[item_name].append(price)
            #         self.item_price_dict[item_name] = [price]
            # else:
            #     price = self.item_price_dict[item_name]
            # #self.enrolled_cust_dict[user_name].append(price)
            self.enrolled_cust_dict[user_name].append(customer)
        else:
            if user_name in self.id_customer_dict.keys():
                user_name = self.id_customer_dict[user_name]
            # else:
            #     user_name = user_name
            customer = "Old"
            for i in self.customer_list:
                if user_name in i.cust_name:
                    cust_name = i.cust_name
                    cust_type = i.cust_type
                    cust_id = i.cust_id
                    self.enrolled_cust_dict[user_name] = [cust_type]
            for v in self.enrolled_cust_dict.values():
                if v[0] == 'G':
                    registration_fee = 0.0
                    discount_rate = self.customer_discount_dict[user_name]
                    cost = sum(self.total_cost_list)
                    discount = float(cost) * float(discount_rate)
                    service_fee = 0.0
                elif v[0] == 'S':
                    registration_fee = 0.0
                    discount = 0.0
                    service_fee = 0.0
                else:
                    registration_fee = 0.0
                    discount = 0.0
                    # cost = self.item_price_dict[item_name]
                    cost = sum(self.total_cost_list)
                    service_fee = bronzeCustomer.get_service_fee(float(cost))

                self.enrolled_cust_dict[user_name].append(str(registration_fee))
                self.enrolled_cust_dict[user_name].append(str(service_fee))
                self.enrolled_cust_dict[user_name].append(str(discount))

            # # Fetching the price of the item entered
            # for item, quant in self.ordered_dish_dict.items():
            #     if item in self.id_price_dict.keys():
            #         price = self.id_price_dict[item]
            #     elif self.item_type_dict[item] == 'B':
            #         price = 0
            #         components = self.components_dict[item]
            #         for i in components:
            #             if i in self.id_item_dict.keys():
            #                 component = self.id_item_dict[i]
            #             else:
            #                 component = i
            #             if self.item_type_dict[component] != 'D':
            #                 cost = self.item_price_dict[component]
            #                 price += float(cost)
            #             # self.item_price_dict[item_name].append(price)
            #             self.item_price_dict[item] = [price]
            #     else:
            #         price = self.item_price_dict[item]
            #     #self.enrolled_cust_dict[user_name].append(price)
            #     self.ordered_dish_dict[item].append(price)
            # print("Ordered dish dict: ", self.ordered_dish_dict)
            self.enrolled_cust_dict[user_name].append(customer)

        # bd = True
        # while bd:
        #     for key, value in self.ordered_dish_dict.items():
        #         total_cost = int(value[0]) * float(value[1])
        #         print(total_cost)
        #         self.total_cost_list.append(total_cost)
        #     print(self.total_cost_list)
        #     bd = False

        # Printing the receipt for the customer's order
        print("**" * 30)
        print(f"Receipt of Customer {user_name}")
        print("**" * 30)
        food_desc = ""
        history = ""
        order_dict = zip(self.ordered_dish_dict, self.quantity_list)
        some = True
        while some:
            for key, value in self.enrolled_cust_dict.items():
                # Receipt for old customers
                if self.enrolled_cust_dict[user_name][4] == "Old":
                    old_customer_total = str(round(((sum(self.total_cost_list) + float(value[2])) - float(value[3])), 2))
                    for k, v in order_dict:
                        print(f"{str(k).ljust(9)}: {str(self.ordered_dish_dict[k][1]).rjust(23)} (AUD) x {str(v)}")
                        food_desc += str(v) + " x " + str(k) + " "
                    print(f"Service fee:  {str((value[2])).rjust(25)} (AUD)")
                    #food_desc += str(quantity) + " x " + str(item_name) + " "
                    some = False
                    if self.enrolled_cust_dict[user_name][0] == "G":
                        print(f"Discount:  {str(self.enrolled_cust_dict[user_name][3]).rjust(28)} (AUD)")
                    # print(f"Total cost: {str(((float(value[4]) * int(quantity)) + float(value[2])) - (float(value[3]))):>27} (AUD)\n")
                    print(f"Total cost: {old_customer_total:>27} (AUD)\n")
                    print("**" * 30)
                    history = {"Dishes": food_desc, "Total Cost": old_customer_total}

                # Receipt for new customers
                elif self.enrolled_cust_dict[user_name][4] == "New":
                    new_customer_total = str(round(((sum(self.total_cost_list) + float(value[1]) + float(value[2])) - (float(value[3]))), 2))
                    for k, v in order_dict:
                        print(f"{str(k).ljust(9)}: {str(self.ordered_dish_dict[k][1]).rjust(23)} (AUD) x {str(v)}")
                        food_desc += str(v) + " x " + str(k) + " "
                    # print(f"{str(item_name).ljust(9)}: {str(value[4]).rjust(23)} (AUD) x {str(quantity)}")
                    print(f"Service fee:  {str(value[2]).rjust(25)} (AUD)")
                    # food_desc += str(quantity) + " x " + str(item_name) + " "
                    some = False
                    if self.enrolled_cust_dict[user_name][0] == "G" or self.enrolled_cust_dict[user_name][0] == "S":
                        print(f"Registration fee:  {str(self.enrolled_cust_dict[user_name][1]).rjust(20)} (AUD)")
                    if self.enrolled_cust_dict[user_name][0] == "G":
                        print(f"Discount:  {str(self.enrolled_cust_dict[user_name][3]).rjust(28)} (AUD)")
                    # print(f"Total cost: {str(((float(value[4]) * int(quantity)) + float(value[1]) + float(value[2])) - (float(value[3]))):>27} (AUD)\n")
                    print(f"Total cost: {new_customer_total:>27} (AUD)\n")
                    print("**" * 30)
                    history = {"Dishes": food_desc, "Total Cost": new_customer_total}

                # Fetching user's history of order
                if user_name not in self.cust_history_dict.keys():
                    self.cust_history_dict[user_name] = []
                self.cust_history_dict[user_name].append(history)
                operations.all_cust_list.append(user_name)

    def get_input_for_set_discount(self):
        """
        This function is used to get and check the input to set the discount value for the particular Gold customer.
        """
        m = True
        while m:
            try:
                input_id = input("Enter the customer ID to change the discount value: \n")
                customer_finder = self.find_customers(input_id)
                if customer_finder is None:
                    print("No results found!")
                else:
                    if customer_finder.cust_type == 'G':
                        # if input_id in operations.id_customer_dict.keys() or input_id in operations.id_customer_dict.values():
                        m = False
                    else:
                        m = True
                        raise ValueError("Customer Name/ID not found in the list!")
                return input_id
            except ValueError as e:
                print(e)

    # Option 4:
    @staticmethod
    def order_meals_via_file():
        """
        This function is used to order meals via file in the restaurant.
        """
        p = True
        while p:
            try:
                filename = input("Please enter the filename to place the order (e.g. orders.txt): \n")
                a = os.path.exists(filename)
                # if filename == 'orders.txt':
                if os.path.exists(filename):
                    p = False
                    print("Successfully placed the orders")
                else:
                    p = True
                    raise ValueError("Incorrect filename. Please re-enter correctly!")
                return filename
            except ValueError as e:
                print(e)

    # Option 8
    def sold_out_dishes(self):
        """
        This function is used to get details on the sold out dishes.
        """
        b = True
        while b:
            try:
                sold_input = input("Enter the dishes that are sold out: \n").strip()
                if sold_input not in self.id_item_dict.keys() and sold_input not in self.id_item_dict.values():
                    b = True
                    raise ItemNameError("Item is invalid. Please enter a valid item!")
                elif sold_input in self.id_item_dict.keys():
                    b = False
                    self.sold_input_dict[sold_input] = self.id_item_dict[sold_input]
                else:
                    b = False
                    for soldid, soldname in self.id_item_dict.items():
                        if soldname == sold_input:
                            self.sold_input_dict[soldid] = soldname
                self.sold_input_list = [i.strip() for i in self.sold_input_dict.values()]
                for i, obj in enumerate(self.sold_input_list):
                    if obj in self.item_price_dict.keys():
                        self.sold_dishes[i] = obj
                    else:
                        raise ItemNameError("The entered dishes are invalid and they will not be added")
            except ItemNameError as e:
                print(e)

    # Option 9:
    # Find frequent customers
    def freq_cust(self):
        """
        This function is used to get the details of the most frequent customer to the restaurant.
        """
        freq_customer = max(self.all_cust_list, key=self.all_cust_list.count)
        order_count = self.all_cust_list.count(freq_customer)
        print(f"{freq_customer} has the maximum number of orders equal to {order_count}!")

    # Option 10:
    def cust_order_hist(self, user_name):
        """
        This function is used to retrieve the order history of a particular customer.
        """
        print(f"This is the order history of {user_name}.")
        print("Items".rjust(35), "Total Cost".rjust(35))
        ctr = 1
        for k in self.cust_history_dict[user_name]:
            print("Order", str(ctr).ljust(10), str(k['Dishes']).rjust(20), str(k['Total Cost']).rjust(28))
            ctr += 1

    # Option 0:
    def exit_program(self):
        """
        This function is used to exit the program.
        """
        print("System exiting...!!!!")
        self.run = False

    def start(self):
        """
        This function is the start of the restaurant menu ordering system.
        """
        self.run = True
        self.customer_list.clear()
        self.items_list.clear()
        self.customer_orders_list.clear()
        # self.all_cust_list.clear()
        records.read_customers(self.customer_filename)
        records.read_items(self.items_filename)
        while self.run:
            # self.customer_list.clear()
            # self.items_list.clear()
            # self.customer_orders_list.clear()
            # #self.all_cust_list.clear()
            # records.read_customers(self.customer_filename)
            # records.read_items(self.items_filename)
            # records.read_orders_file(self.orders_filename)
            # for i in range(len(self.items_list)):
            #     if self.items_list[i].item_type == 'D':
            #         self.drinks_list.append(self.items_list[i].item_name)
            #     elif self.items_list[i].item_type == 'F':
            #         self.food_list.append(self.items_list[i].item_name)

            print("\nWelcome to the RMIT restaurant ordering system!\n")
            print("##" * 30)
            print("You can choose from the following options: \n"
                  "1: Order a meal\n"
                  "2: Display existing customers information\n"
                  "3: Display existing items information\n"
                  "4: Order meals via a file\n"
                  "5: Adjust the service fee rate for all the bronze customers\n"
                  "6: Adjust the discount rate of a gold customer\n"
                  "7: Display all orders\n"
                  "8: Add sold-out items\n"
                  "9: Display the most frequent customer\n"
                  "10: Display a customer order history\n"
                  "0: Exit the program")
            print("##" * 30, "\n")
            # choose_option = int(input("Choose one option:\n"))
            choose_option = self.get_str("Choose one option:\n")

            # Functions created for the options available to select on the home screen
            try:
                # Order a meal
                if choose_option == '1':
                    start = False
                    self.enrolled_cust_dict.clear()
                    self.ordered_dish_dict.clear()
                    self.total_cost_list.clear()
                    self.quantity_list.clear()
                    user_name = self.get_str("Enter the name or ID of the customer [e.g. Huong]: \n").strip()
                    # user_name = input("Enter the name or ID of the customer [e.g. Huong]: \n").strip()
                    item_name = self.get_item_name()
                    quantity = self.get_quantity()
                    self.quantity_list.append(quantity)
                    self.ordered_dish_dict[item_name] = [quantity]
                    c = True
                    while c:
                        order_more = self.order_more()
                        if order_more != "n":
                            item_name = self.get_item_name()
                            quantity = self.get_quantity()
                            self.ordered_dish_dict[item_name] = [quantity]
                            self.quantity_list.append(quantity)
                            c = True
                        else:
                            c = False
                            operations.order_meal(user_name, item_name, quantity)

                # Display existing customer information
                elif choose_option == '2':
                    self.customer_list.clear()
                    records.display_customers()

                # Display existing items information
                elif choose_option == '3':
                    self.items_list.clear()
                    records.display_items()

                # Order meals via file
                elif choose_option == '4':
                    input_filename = operations.order_meals_via_file()
                    self.orders_filename = input_filename
                    # self.orders_filename = os.path.join('E:/Programming Fundamentals/Assignment 2/Draft_Ass2/Assignment_2_files/di_level/', input_filename)

                # Adjust service fee rate of all Bronze customers
                elif choose_option == '5':
                    BronzeCustomer.set_service_fee_rate()

                # Adjust discount rate of a Gold customer
                elif choose_option == '6':
                    input_id = operations.get_input_for_set_discount()
                    discount_value = operations.get_positive_float("Enter the discount value for the mentioned customer ID: \n")
                    goldCustomer.set_discount(input_id, discount_value)

                # Display all orders
                elif choose_option == '7':
                    records.display_orders()

                # Add Sold-out items
                elif choose_option == '8':
                    operations.sold_out_dishes()

                # Display the most frequent customer
                elif choose_option == '9':
                    operations.freq_cust()
                # elif choose_option == 10:
                #     customer_name = operations.get_customer_name()
                #     index = 0
                #     if customer_name.cust_type == 'G':
                #         print(f'{index+1}, {customer_name.cust_name}')
                #     else:
                #         print(f'{index+1}, {customer_name.cust_name}')
                #     print(customer_name)

                # Display a customer's order history
                elif choose_option == '10':
                    a = True
                    while a:
                        try:
                            user_name = self.get_str("Enter the name or ID of the customer [e.g. Huong]: \n").strip()
                            find_cust = records.find_customers(user_name)
                            if find_cust is None:
                                a = True
                                raise ValueError(
                                    "Invalid customer detail. Re-enter correct details to fetch the order history!")
                            else:
                                a = False
                                user_name = find_cust.cust_name
                                if self.cust_history_dict == {}:
                                    raise ValueError(f"No order history yet for the mentioned customer: {user_name}")
                                else:
                                    operations.cust_order_hist(user_name)
                        except ValueError as e:
                            print(e)

                # Exit the program
                elif choose_option == '0':
                    operations.exit_program()
                #
                # # Other methods results test
                # elif choose_option == '11':
                #     item_result = records.find_items("RiceBanquet")
                #     if item_result is None:
                #         print("Item not found in the list!")
                #     else:
                #         if item_result.item_type == 'B':
                #             print(f'ID: {item_result.item_id}, Type: {item_result.item_type}, Name: {item_result.item_name}, Components: {item_result.item_components}')
                #         else:
                #             print(f'ID: {item_result.item_id}, Type: {item_result.item_type}, Name: {item_result.item_name}, Price: ${item_result.item_price}')
                #
                # elif choose_option == '12':
                #     silverCustomer.display_info()
                # elif choose_option == '13':
                #     goldCustomer.display_info()
                # elif choose_option == '14':
                #     items.display_info()
                # elif choose_option == '15':
                #     foodDish.display_info()
                # elif choose_option == '16':
                #     drink.display_info()
                # elif choose_option == '17':
                #     result = orders.compute_cost("Tom", "pizza", 2)
                #     if result is None:
                #         print("None")
                #     else:
                #         print(f'{int(result[8])}, {int(result[3])}, {int(result[7])}')
                # elif choose_option == '18':
                #     customer_result = records.find_customers("3")
                #     if customer_result is None:
                #         print("Customer not found in the list")
                #     else:
                #         if customer_result.cust_type == "G":
                #             print(
                #                 f'ID: {customer_result.cust_id}, Type: {customer_result.cust_type}, Name: {customer_result.cust_name}, Discount: {customer_result.discount_rate}')
                #         else:
                #             print(
                #                 f'ID: {customer_result.cust_id}, Type: {customer_result.cust_type}, Name: {customer_result.cust_name}')
                else:
                    raise ValueError("Invalid option selection. Re-enter correct option!!")
            except ValueError as e:
                print(e)


# Command line arguments
if len(sys.argv) == 3:
    result = sys.argv[0].endswith(".py")
    result_cust = sys.argv[1].startswith("customers")
    result_item = sys.argv[2].startswith("items")
    if result == result_cust == result_item:
        pass
        # print(sys.argv[0], sys.argv[1], sys.argv[2])
    elif result_cust != result_item:
        raise ValueError("Order of filenames is not correct. First file should be customers, second is items!")
    else:
        raise ValueError("Order of files invalid. First is .py, second is customers, finally the items!")
elif len(sys.argv) == 1:
    sys.argv.append("customers.txt")
    sys.argv.append("items.txt")
    # print(sys.argv)
else:
    raise ValueError("Invalid number of arguments!")

# Creating objects
customer = Customer()
bronzeCustomer = BronzeCustomer()
silverCustomer = SilverCustomer()
goldCustomer = GoldCustomer()
items = Items()
foodDish = FoodDish()
drink = Drink()
banquet = Banquet()
orders = Orders()
records = Records()
operations = Operations()
operations.start()
# operations.cmd()

# Find Item
# item_result = records.find_items("RiceBanquet")
# if item_result is None:
#     print("Item not found in the list!")
# else:
#     if item_result.item_type == 'B':
#         print(
#         f'ID: {item_result.item_id}, Type: {item_result.item_type}, Name: {item_result.item_name}, Components: {item_result.item_components}')
#     else:
#         print(
#         f'ID: {item_result.item_id}, Type: {item_result.item_type}, Name: {item_result.item_name}, Price: ${item_result.item_price}')

# # Find Customer
# customer_result = records.find_customers("Tom")
# if customer_result is None:
#     print("Customer not found in the list")
# else:
#     if customer_result.cust_type == "G":
#         print(
#         f'ID: {customer_result.cust_id}, Type: {customer_result.cust_type}, Name: {customer_result.cust_name}, Discount: {customer_result.discount_rate}')
#     else:
#         print(
#         f'ID: {customer_result.cust_id}, Type: {customer_result.cust_type}, Name: {customer_result.cust_name}')

# Compute cost
# result = orders.compute_cost("Tom", "pizza", 2)
#                 if result is None:
#                     print("None")
#                 else:
#                     print(f'{int(result[8])}, {int(result[3])}, {int(result[7])}')
