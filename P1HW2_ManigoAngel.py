# Angel Manigo
# 9/29/24
# P1HW2
# Create and test program

print("This program calculates and displays travel expenses")
print("\n")
budget = int(input("Enter Budget: "))
print("\n")
td = (input("Enter travel destination: "))
print("\n")
gas = int(input("How much do you think you will spend on gas? "))
print("\n")
hotel = int(input("Approximately, how much will you need for accomodation/hotel? "))
print("\n")
fd = int(input("Last, how much do you need for food? "))
print("\n")
print("------------Travel Expenses------------")
print("Location:",td)
print("Initial Budget:",budget)
print("\n")
print("Fuel:",gas)
print("Accomodation:",hotel)
print("Food:",fd)
print("\n")
rb = int((budget) - (gas) - (hotel) - (fd))
print("Remaining Balance:", rb)
