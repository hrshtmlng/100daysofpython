exit = "no"

while exit == "no":
  animalSound = input("What animal sound do you want to hear? ")

  if animalSound == "cow" or animalSound == "Cow":
    print("🐮 Moo")
  elif animalSound == "pig" or animalSound == "Pig":
    print("🐷 Oink")
  elif animalSound == "sheep" or animalSound == "Sheep":
    print("🐑 Baaa")
  elif animalSound == "duck" or animalSound == "Duck":
    print("🦆 Quack")
  elif animalSound == "dog" or animalSound == "Dog":
    print("🐶 Woof")
  elif animalSound == "cat" or animalSound == "Cat":
    print("🐱 Meow")
  else:
    print("I don't know that animal sound. Try again.")

  exit = input("Do you want to exit?: ")
