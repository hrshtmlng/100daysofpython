come to Math Facts Game!")
print()
print("How well do you know your math facts? Pick a number & I will give you 10 math facts to solve")
print()


multipleOf = int(input("Name your multiples: "))
print()

counter = 0
for i in range(1, 11):
  correctAnswer = i*multipleOf
  print(i, "x", multipleOf)
  answer = int(input("> "))
  if answer == correctAnswer:
    print("You got it right!!")
    counter +=1
  else:
    print("That's not correct. It should have been", correctAnswer)

if counter == 10:
  print("Wow!! A perfect score!!🥳")
else:
  print("You got", counter,"out of 10 correct")
