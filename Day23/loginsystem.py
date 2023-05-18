
def login():
  while True:
    username = input("What is your username?: ")
    password = input("What is your password?: ")
    if username == "hrshtmlng" and password == "hey123":
      print("Welcome Harshit!!")
      break
    else:
      print("That is not the correct username or password. Try again!!")
      continue

print("LOGIN SYSTEM")
login()
