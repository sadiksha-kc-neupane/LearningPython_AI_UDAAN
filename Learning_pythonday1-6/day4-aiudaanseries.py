#conditional statement

# if condition/scenario:
#     statement/block of code to be executed

# age = 20 
# if age > 18:
#     print("you can vote ")
# else:
#     print("you cannot vote ")


# password = "nepal123"
# if password == "nepal123":
#     print ("login success, password matched")
# else:
#     print("login failed, password didn't matched")

# marks = 90


# if marks >= 90
#     print("A+ ayoo")
# elif marks>=80:
#     print("A ayo")


#Login system --> email, password 
#email, password -- both correct xa vaney , Login ,else failed

email = "hell o@gmail.com"

password = "hello123"

# if email == "hello@gmail.com":
#     if password == "hello123":
#         print("login successful")

# if email=="hello@gmail.com" and password=="hello123":
#     print("login successful")
# else:
#     print("email or password maybe incorrect...Try againnnn")


# if email=="hello@gmail.com" or password=="hello123":
#     print("login successful")
# else:
#     print("email or password maybe incorrect...Try againnnn")   

# logged_in = False

# if not logged_in:
#     print("please login")


# for i in range(5):
#     print(i)

# for i in range(5,10):
#     print(i)

# for i in range(10,0,-2):
#     print(i)

# countries =["nepal", "china", "india" , "USA"]

# for country in countries:
#     print(country)

# prediction_score = [10, 80 , 40 , 88, 54]

# for prediction in prediction_score:
#     if prediction > 80:
#         print("good score")
#     else:
#         print("not good")


email_list = [
    "There is a discount",
    "free tickets congrats",
    "what is the update for the project",
    "congratulation you won rolex watch"
]


for email in email_list :
    if "congrats" in email or "congratulation " in email or "disccount" in email :
        print("its a spam" , email)
    else:
        print("Not spam" , email)