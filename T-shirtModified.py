import datetime


def main():
    only_color = ["Blue", "Yellow", "Red", "Grey", "Black", "Orange", "Violet", "YellowGreen"]
    only_size = ["Small", "Medium", "Large", "XL", "XXL"]

    while True:
        # Get valid color
        color = ""
        while color not in only_color:
            color = input(
                "Choose your color (Blue, Yellow, Red, Grey, Orange, Black, Violet, YellowGreen): ").strip().title()
            if color not in only_color:
                print("Invalid color. Please choose a valid color from the list.")

        # Get valid size
        size = ""
        while size.title() not in only_size:
            size = input("Choose your size (Small, Medium, Large, XL, XXL): ").strip().title()
            if size.title() not in only_size:
                print("Invalid size. Please try again.")

        # Get price
        while True:
            try:
                price = float(input("Enter the price of the t-shirt: "))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value for price.")

        # Get payment
        while True:
            try:
                amount = float(input("Enter the amount paid: "))
                if amount >= price:
                    change = amount - price
                    break
                else:
                    print("Payment not accepted. The amount is less than the price.")
            except ValueError:
                print("Invalid input. Please enter a numeric value for payment.")


        # Generate receipt
        now = datetime.datetime.now()
        receipt_line = (
            "=== T-SHIRT RECEIPT ===\n"
            f"Date & Time : {now.strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"Color       : {color}\n"
            f"Size        : {size}\n"
            f"Price       : {price}\n"
            f"Amount Paid : {amount}\n"
            f"Change      : {change}\n"
            "-------------------------------\n"
        )

        try:
            with open("Receipt.txt", "a") as file:
                file.write(receipt_line)
            print("Receipt generated and saved as 'Receipt.txt'.")
        except Exception as e:
            print("Error writing to file:", e)

        # Ask to buy again
        buy_again = input("Do you want to buy another t-shirt? (y/n): ").strip().lower()
        if buy_again != 'y':
            break

    print("Thank you for shopping!")


if __name__ == "__main__":
    main()
