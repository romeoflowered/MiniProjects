print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill?"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))

tip_as_percent = tip / 100
total_tip_amount = total_bill * tip_as_percent
final_amount = (total_bill + total_tip_amount) / people
print("Each person should pay: ", round(final_amount, 2))






