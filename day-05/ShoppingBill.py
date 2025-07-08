# Hello Eagles! 🦅
# *Day 5/50 - AI Python Challenge*
# *Shopping Bill* : Calculate total cost of 3 items including tax percentage.
# Use filename as *ShoppingBill.py*
# *Our Goal* : Use any AI tool to generate the script and execute the script without issue
# This is automated AI Message
# #FlyHighwithAI ✨

# Function to calculate total cost including tax
def calculate_total_cost(item1_price, item2_price, item3_price, tax_percentage):
    total_cost = item1_price + item2_price + item3_price
    tax_amount = (tax_percentage / 100) * total_cost
    total_cost_with_tax = total_cost + tax_amount
    return total_cost_with_tax

# Main function to execute the script
def main():
    # Prices of the items
    item1_price = float(input("Enter the price of item 1: "))
    item2_price = float(input("Enter the price of item 2: "))
    item3_price = float(input("Enter the price of item 3: "))
    
    # Tax percentage
    tax_percentage = float(input("Enter the tax percentage: "))
    
    # Calculate total cost
    total_cost = calculate_total_cost(item1_price, item2_price, item3_price, tax_percentage)
    
    # Display the total cost
    print(f"The total cost including tax is: ${total_cost:.2f}")

# Execute the main function
if __name__ == "__main__":
    main()

# Sample Input/Output

# Enter the price of item 1: 50
# Enter the price of item 2: 30
# Enter the price of item 3: 20
# Enter the tax percentage: 10
# The total cost including tax is: $110.00
