MENU =[("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]


def get_order():
    current_order = []
    while True:
        print(" Add a new book to your order! NOTE **** please enter the book title or the last name of the author ****")
        order = input()
        if order not in MENU:
            current_order.append(order)
        else:
            print("I'm sorry,this book is not available to order online. The book is in stock at the local bookstore and available for pickup....")
            continue
        if is_order_complete():
            return current_order


def is_order_complete():
    print("Do you need to add any other details about the book to your order? eg: author last name*** Type yes or no")
    choice = input()
    if choice == "no":
        return True
    elif choice == "yes":
        return False
    else:
        raise Exception("invalid input")


def output_order(order_list):
    print("Okay, thanks for your bookstore order. Today you ordered,")
    for order in order_list:
        print(order)


def main():
    order = get_order()
    output_order(order)
    print("Your order is complete and will be arriving to your address soon. Please allow at least 3 business days for shipping")


if __name__ == "__main__":
    main()
