email = input("Enter your email address: ")

# find the index of the @ symbol
at_index = email.find("@")

# print the username and domain name
username = email[:at_index]
domain_name = email[at_index+1:]
print("Username:", username)
print("Domain Name:", domain_name)


# Enter your email address: codingwithkien@gmail.com
# Username: codingwithkien
# Domain Name: gmail.com
