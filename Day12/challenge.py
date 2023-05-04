print("100 Days of code QUIZ")
print()
ans1 = input("How many can you answer correctly?  ")
if ans1 == "Python":
  print("Correct🥳🥳")
else:
  print("Nope🙈")
ans2 = int(input("Which lesson number is this?  "))
if (ans2 > 12):
  print("We're not quite that far yet")
elif(ans2==12):
  print("That's right!!")
else:
  print("We've gone well past that!!")
