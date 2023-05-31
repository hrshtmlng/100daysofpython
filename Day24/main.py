def whichCake(ingredient, base, coating):
  if ingredient == "chocolate":
    print("Mmm, chocolate cake is amazing")
  elif ingredient == "broccoli":
    print("You what mate?!")
  else: 
    print("Yeah, that's great I suppose...")
  print("So you want a", ingredient, "cake on a", base, "base with", coating, "on top?")
  
userIngredient = input("Name an ingredient: ")
userBase = input("Name a type of base: ")
userCoating = input("Fave cake topping: ")

whichCake("carrot", "biscuit", "icing")
