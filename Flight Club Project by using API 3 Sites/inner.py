import requests

SHEETY_USERS_ENDPOINT = "https://api.sheety.co/c37bd13bdfe01b785fd07eddc4ec3498/flightDeals/users"

print("Welcome to Flight Club\nWe find the best flight deals and email you")
name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
email = input("What is your email?\n")
refresh = input("Type your email again?\n")

while email != refresh:
    print("That's not right, let's try again:")
    email = input("What is your email?\n")
    email_validation = input("Type your email again.\n")

user_data = {
    "user": {
        "firstName": name,
        "lastName": last_name,
        "email": email,
    }
}

response = requests.post(
    url=SHEETY_USERS_ENDPOINT,
    json=user_data,
)
# print(response.text)
if response.status_code == 200:
    print("Success! Your email has been added, look forwards to some amazing flight deals!")
else:
    print("There was an issue, please try again later.")
