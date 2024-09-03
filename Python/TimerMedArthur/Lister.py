#learning how to create lists in python
#making a function that adds customers to a list
def main():
    def add_customers(customers_list):
            print("Adding customers.")
            new_customer_amount = int(input("How many customers do you want to add? ")) # here we find out how many times we need to add customer and after this we can make the second loop.
            for i in range(new_customer_amount): #creating a for loop to add the amount of customers we want to add
                customer = input("Enter the name of the customer: ")
                if customer == "":
                    break
                customers_list.append(customer)
            else:
                print("Customers added.")
            return customers_list
    def sort_customers(customers_list):
        customers_list.sort()
        return customers_list
    def delete_customers(customers_list):
        print("Deleting customers.")
        customer_to_delete = input("Enter the name of the customer you want to delete: ")
        customers_list.remove(customer_to_delete)
        print("Customer", customer_to_delete, "deleted.")
        return customers_list
    def search_customers(customers_list):
        print("Searching list. ")
        customer_to_search = input("Enter the name of the customer you want to search for: ")
        if customer_to_search in customers_list:
            print("Customer", customer_to_search, "found.")
        else:
            print("Customer", customer_to_search, "not found.")
        return customers_list
    def print_customers(customers_list):
        number_of_customers = len(customers)
        print("Printing", number_of_customers, "customers. ")
        for number, _customer in enumerate(customers):
            print("Customer", number+1,":", _customer)
    def edit_customer(customer_list):
        customer_to_edit = input("Enter the name of the customer you want to edit: ")
        if customer_to_edit in customers:
            new_name = input("Enter the new name of the customer: ")
            customer_list[customer_list.index(customer_to_edit)] = new_name
            print("Customer", customer_to_edit, "edited to", new_name)
        else:
            print("Customer", customer_to_edit, "not found.")

    customers = [] # this is an empty list

    # we want to make a system where we can add, delete and edit customers to a list
    choice = 0 # we put this to make the while loop work. 
    while choice != 7: # while the choice is not 3, the loop will continue. 
        choice = int(input("1. Add customer. \n2. Delete customer. \n3. Search list. \n4. Sort list. \n5. Print list. \n6. Edit customer. \n7. Exit. \nChoose an option: "))
        # 1 for adding customers 2 for deleting list 3 for searching in list 4 for sorting list 5 for printing all items 6 for edit

        if choice == 1:
            #i have to call the function add_customers()
            customers = add_customers(customers)
        elif choice == 2:
            customers = delete_customers(customers)
        elif choice == 3:
            customers = search_customers(customers)
        elif choice == 4:
            customers = sort_customers(customers)
        elif choice == 5:
            print_customers(customers)
        elif choice == 6:
            edit_customer(customers)
        elif choice == 7:
            print("Exiting. ")
        else: 
            print("Invalid input")

if __name__ == "__main__":
    main()
