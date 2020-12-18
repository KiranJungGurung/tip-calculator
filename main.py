#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

# Print welcome to the tip calculator.
print("Welcome to the tip calculator.")

#Assign bill,tip and people as a variable name.
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give?10, 12, or 15?"))
people = int(input("How many people to split the bill? "))

# Calculate final_amount:
 # Calculate tip_as_percent by dividing tip by 100.
tip_as_percent = tip /100

# Multiply bill with tip_as_percent to get total_tip_amount.
total_tip_amount = bill * tip_as_percent

#Add bill and total_tip_amount to get total_bill.
total_bill = bill + total_tip_amount

#Divide total_bill by people to get bill_per_person.
bill_per_person = total_bill / people

# Round the final_amount to 2 decimal point.
final_amount = round(bill_per_person, 2)

#If the user put whole number as bill($150), to avoid the format error, use {:.2f}.format().
final_amount = "{:.2f}".format(bill_per_person)

#print each person should pay using f-string.
print(f"Each person should pay: $ {final_amount}")
