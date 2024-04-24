
# Lab 2C - Currency Converter

#Display available currency options
print("Available Currencies: A)USD B)CAD C)YEN")

# Prompt for currency amount, type, and type to convert to
amount = float(input("Enter transaction amount: "))
cType = input("Transaction currency: ")
convertTo = input("Currency to convert to:")

# Determine currency type to display
if convertTo =="A":
    currency = "USD"
if convertTo =="B":
    currency = "CAD"
if convertTo =="C":
    currency = "YEN"

# Convert to USD
if cType == "B":
    amount /= 1.24
if cType == "C":
    amount /= 108.59

#Convert to desired currency
if convertTo == "B":
    amount *= 1.24
if convertTo == "C":
    amount *= 108.59

#Display results
if cType == convertTo:
    print("Conversion not needed...")
else:
    print(f"Converted value: {round(amount, 2)} {currency}")