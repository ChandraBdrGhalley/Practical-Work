print("Newton's Second Law of Motion")
print("-----------------------------------------")

#Determine the missing value
print("Select the missing value:")
print("1. Mass (m)")
print("2. Acceleration (a)")
print("3. Force (F)")
missing_value_choice = input("Enter the option number for the missing")

#Prompt the user to enter the other two values
if missing_value_choice == "1":
    a = float(input("Enter acceleration (a): "))
    F = float(input("Enter force (F): "))
    m = F/a
    print(f"Mass (m) = {m}")

elif missing_value_choice == "2":
    F = float(input("Enter force (F): "))
    m = float(input("Enter mass (m): "))
    a = F/m
    print(f"Acceleration (a) = {a}")

elif missing_value_choice == "3":
    m = float(input("Enter mass (m): "))
    a = float(input("Enter acceleration (a)"))
    F = m * a

else:
    print("Invalid option seleced for the missing value.")
