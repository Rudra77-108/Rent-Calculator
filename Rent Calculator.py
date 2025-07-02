rent= int(input("Enter flat rent = "))
food= int(input("Enter your total food expenses = "))
electricity_spend= int(input("Enter your total of electicity spend = "))
charge_per_unit = int(input("Enter the charge per unit = "))
people= int(input("Enter the number of people living in the room = "))

total_bill= electricity_spend * charge_per_unit

output = (food + rent + total_bill) /people

print("Each person will pay = ", output)
