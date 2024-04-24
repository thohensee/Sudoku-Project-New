
# Lab 2B - Utility Charge Calculator

# Prompt for total water usage
water = float(input("Enter your water usage in gallons:"))

# Apply three-tiered charges based on water usage quantity
cost = 0
if water > 20000:
    cost = cost + (5999/1000)*2.35 + (14001/1000)*3.75
    water = water - 20000
    cost = cost + 6*(water/1000)
elif water >= 6000:
    cost = cost + (5999/1000)*2.35
    water = water - 5999
    cost = cost + 3.75*(water/1000)
else:
    cost = (water/1000)*2.35

# Display water costs
print(f"Money owed: ${round(cost, 2)}")