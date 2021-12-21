def FruitsShop():
      while True:
            try:
                  FruitType = str(input("What fruits will you buy?\n1) Coconut\n2) Apple\n3) Durian\n4) Dragon Fruit\n5) Banana\n Your Choose 1/2/3/4/5: "))
            except ValueError:
                  print("Option Anvailable,please try again!")
                  continue
            else:
                  coconut = 15
                  apple = 10
                  Durian  = 24
                  dragonFruit = 18
                  banana = 16

                  if FruitType =="1":
                              sumFruits = int(input("\nHow much Coconut do you want to buy? : "))
                              Total = sumFruits * coconut
                              Result = f"You buy {sumFruits} Coconut and you must paid ${Total}"
                              output = [Result]
               
                  elif FruitType =="2":
                              sumFruits = int(input("\nHow much Apple do you want to buy? : "))
                              Total = sumFruits * apple
                              Result = f"You buy {sumFruits} Apple and you must paid ${Total}"
                              output = [Result]
              
                  elif FruitType =="3":
                              sumFruits = int(input("\nHow much Durian do you want to buy? : "))
                              Total = sumFruits * Durian
                              Result = f"You buy {sumFruits} Durian and you must paid ${Total}"
                              output = [Result]
                  elif FruitType =="4":
                              sumFruits = int(input("\nHow much Dragon Fruit do you want to buy? : "))
                              Total = sumFruits * dragonFruit
                              Result = f"You buy {sumFruits} Dragon Fruit and you must paid ${Total}"
                              output = [Result]
                  elif FruitType =="5":
                              sumFruits = int(input("\nHow much Banana do you want to buy? : "))
                              Total = sumFruits * banana
                              Result = f"You buy {sumFruits} Durian and you must paid ${Total}"
                              output = [Result]

                  else:
                        print("Option Not Available!,please try again!")                  
                        cuy = input("Mau lagi? Yes or No : ")
                        if cuy =="Yes":
                               continue
                        elif cuy =="No":
                               break
                        else:
                               print("Invalid option!")
                               break     

            break
      return output   