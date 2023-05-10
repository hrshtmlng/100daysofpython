print("Welcome to Guess the Nuber....")
print()
print("Guess a number between 1 and 1,000,000 and I will tell you if are too low, too high, or get it correct..")
print()
print("Let's play!!")

correctNumber = 2300
attempt = 1

while True:
  userGuess = int(input("Pick a numberbetween 1 and 1,000,000: "))
  if userGuess < 0:
    print("Now we'll never know what the answer is ....")
    exit()
  if userGuess < correctNumber:
    print("That number is too low. Try again!")
    attempt += 1
  elif userGuess > correctNumber:
    print("That number is too high. Try again!!")
    attempt += 1
    continue
  elif userGuess == correctNumber:
    print("You are a winner!🥳🥳")
      break
  else:
    print("That is not a number I recongize")
  print("It took you", attempt, "attempt(s) to get the correct answer.")
    
