print("Press 1 to get Account Creation")
print("press 2 to Login Account")
print("press 3 to withdraw amount Account")
input_number = int(input("Enter A number with in 1 to 3 :"))
account_holder_name = input("Enter your name :")
account_holder_father_name = input("Enter your father name :")
account_holder_phone_number = int(input("Enter your phone number :"))
account_holder_username = input("Enter your username :")
account_holder_password = input("Enter your password :")
account_holder_deposit = int(input("Enter your initial deposit amount"))
account_holder_details =[account_holder_name,account_holder_father_name,account_holder_phone_number,account_holder_username,account_holder_password]
print(account_holder_details[0])
print(account_holder_details[1])
print(account_holder_details[2])
print(account_holder_details[3])
print(account_holder_details[4])


