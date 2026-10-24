
# TASK 2: Stock Portfolio Tracker

# Dictionary containing stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420
}

portfolio = {}
total_investment = 0

print("===== Stock Portfolio Tracker =====")
print("Available Stocks:", list(stock_prices.keys()))

while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available!")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero!")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity

    except ValueError:
        print("Please enter a valid whole number!")

print("\n===== Portfolio Summary =====")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment

    print(f"{stock}: {quantity} shares x ${price} = ${investment}")

print(f"\nTotal Investment Value: ${total_investment}")

# Optional file handling
save = input("Save result to file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")

        for stock, quantity in portfolio.items():
            investment = stock_prices[stock] * quantity
            file.write(
                f"{stock}: {quantity} shares = ${investment}\n"
            )

        file.write(f"Total Investment: ${total_investment}\n")

    print("Result saved to portfolio.txt")
