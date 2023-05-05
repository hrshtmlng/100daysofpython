print("Exam Grade Calculator")
print()
nameOfExam = input("Name of exam: ")
totalScore = int(input("Max. Possible Score: "))
yourScore = int(input("Your score: "))
print()


numberScore = float(yourScore / totalScore)

finalNumber = round(numberScore, 2)

finalPerc = round(float(yourScore / totalScore)*100,2)

print("You got", finalPerc, "%")

if finalNumber >= .90:
  print("Your letter score is an A+")
elif finalNumber >= .80 and finalNumber <= .89:
  print("Your letter grade is an A-.")
elif finalNumber >= .70 and finalNumber <=.79:
  print("Your letter score is a B")
elif finalNumber >= .60 and finalNumber <= .69:
  print("Your letter score is a C")
elif finalNumber >= .50 and finalNumber <= .59:
  print("Your letter score is a D")
elif finalNumber <= .49:
  print("Your letter grade is a U")
else:
  print("Try again!!")
