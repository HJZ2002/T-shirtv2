def main():
    only_colors = ["Blue", "Yellow", "Red", "Grey", "Black", "Orange"]
    only_sizes = ["Small", "Medium", "Large", "XL", "XXL"]

    while True:
        # Color input
        while True:
            color = input("Choose your color (Blue, Yellow, Red, Grey, Orange, Black): ").strip()
            if color.capitalize() in only_colors:
                color = color.capitalize()
                break
            else:
                print("Invalid color. Please choose a valid color from the list.")

        # Size input
        while True:
            size = input("Choose your size (Small, Medium, Large, XL, XXL): ").strip()
            if size.capitalize() in only_sizes:
                size = size.capitalize()
                break
            else:
                print("Invalid size. Please try again.")

        # Price input
        while True:
            try:
                price = float(input("Enter the price of the t-shirt: "))
                if price >= 0:
                    break
                else:
                    print("Price cannot be negative.")
            except ValueError:
                print("Invalid input. Please enter a valid price.")

        # Payment input and validation
        while True:
            try:
                amount = float(input("Enter the amount paid: "))
                if amount >= price:
                    change = amount - price
                    print("------------------------------------------------------------")
                    print(f"Color: {color}")
                    print(f"Size: {size}")
                    print(f"Price: {price}")
                    print(f"Amount Paid: {amount}")
                    print(f"Here is your change: {change}")
                    print("------------------------------------------------------------")
                    break
                else:
                    print("Payment not accepted. The amount is less than the price.")
            except ValueError:
                print("Invalid input. Please enter a valid amount.")

        # Ask to buy again
        buy_again = input("Do you want to buy another t-shirt? (y/n): ").strip().lower()
        if buy_again != 'y':
            break

    print("Thank you for shopping!")

if __name__ == "__main__":
    main()
