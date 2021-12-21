def MeatShop():
      while True:
            try:
                  JenisToko = input("\nPlease choose :\n 1) Farm\n 2) FIshery\nYour Choose 1/2 :  ")
            except ValueError:
                  print("Invalid Option,please try again!") 
                  continue
            else: 
                  """
                  Farm Prize
                  """                  
                  chiekenPrize = 20  
                  CowPrize = 30  
                  RabbitPrize = 20  
                  PigPrize = 40  
                  GoatPrize = 35  
                  DuckPrize = 27  
                  """
                  Fishery Prize
                  """          
                  Bawal = 24
                  Kakap = 20
                  fishcat = 15
                  Salmon = 30


                  if JenisToko =="1":
                        print("\nWhat meat will you buy?\n 1) Chieken\n 2) Cow\n 3) Rabbit\n 4) Pig\n 5) Goat\n 6) Duck")
                        MeatChoose = str(input("Your Choose 1/2/3/4/5/6: "))
                        if MeatChoose =="1":
                                    Weight = int(input("How many Pounds of meat do you want to buy? : "))
                                    TotalPrize = f"""
                                    Meat Type         : Chieken
                                    Weight            : {Weight} Pounds
                                    Prize / pounds    : ${chiekenPrize}
                                    Total Prize       : ${chiekenPrize * Weight}
                                    
                                    """
                                    output = [TotalPrize]
                        elif MeatChoose =="2":
                                    Weight = int(input("How many Pounds of meat do you want to buy? : "))
                                    TotalPrize = f"""
                                    Meat Type         : Cow
                                    Weight            : {Weight} Pounds
                                    Prize / pounds    : ${CowPrize}
                                    Total Prize       : ${CowPrize * Weight}
                                   
                                    """
                                    output = [TotalPrize]
                        elif MeatChoose =="3":
                                    Weight = int(input("How many Pounds of meat do you want to buy? : "))
                                    TotalPrize = f"""
                                    Meat Type         : Rabbit
                                    Weight            : {Weight} Pounds
                                    Prize / pounds    : ${RabbitPrize}
                                    Total Prize       : ${RabbitPrize * Weight}
                                    
                                    """
                                    output = [TotalPrize]
                        elif MeatChoose =="4":
                                    Weight = int(input("How many Pounds of meat do you want to buy? : "))
                                    TotalPrize = f"""
                                    Meat Type         : Pig
                                    Weight            : {Weight} Pounds
                                    Prize / pounds    : ${PigPrize}
                                    Total Prize       : ${PigPrize * Weight}
                                     
                                     """
                                    output = [TotalPrize]
                        elif MeatChoose =="5":
                                    Weight = int(input("How many Pounds of meat do you want to buy? : "))
                                    TotalPrize = f"""
                                    Meat Type         : Goa
                                    nWeight           : {Weight} Pounds
                                    Prize / pounds    : ${GoatPrize}
                                    Total Prize       : ${GoatPrize * Weight}
                                     
                                     """
                                    output = [TotalPrize]
                        elif MeatChoose =="6":
                                    Weight = int(input("How many Pounds of meat do you want to buy? : "))
                                    TotalPrize = f"""
                                    Meat Type          : Duc
                                    nWeight            : {Weight} Pounds
                                    Prize / pounds     : ${DuckPrize}
                                    Total Prize        : ${DuckPrize * Weight}
                                    
                                    """
                                    output = [TotalPrize]

                        else :
                                    print("\nOption Aveilable,please try again!\n") 
                                    cuy = input("Mau lagi? Yes or No : ")
                                    if cuy =="Yes":
                                          continue
                                    elif cuy =="No":
                                          break
                                    else:
                                          print("Invalid option!")
                                          break     


                  elif JenisToko=="2":

                        print("\nWhat meat will you buy?\n 1) Bawal\n 2) Kakap\n 3) Lele\n 4) Salmon")
                        MeatChoose = str(input("Your Choose 1/2/3/4/5/6: "))
                        if MeatChoose =="1":
                                    Weight = int(input("How many Pounds of meat do you want to buy? : "))
                                    TotalPrize = f"""
                                    Meat Type         : Bawal
                                    Weight            : {Weight} Pounds
                                    Prize / pounds    : ${Bawal}
                                    Total Prize       : ${Bawal * Weight}
                                    """
                                    output = [TotalPrize]
                        elif MeatChoose =="2":
                                    Weight = int(input("How many Pounds of meat do you want to buy? : "))
                                    TotalPrize = f"""
                                    Meat Type         : Kakap
                                    Weight            : {Weight} Pounds
                                    Prize / pounds    : ${Kakap}
                                    Total Prize       : ${Kakap * Weight}
                                    """
                                    output = [TotalPrize]
                        elif MeatChoose =="3":
                                    Weight = int(input("How many Pounds of meat do you want to buy? : "))
                                    TotalPrize = f"""
                                    Meat Type         : Lele
                                    Weight            : {Weight} Pounds
                                    Prize / pounds    : ${fishcat}
                                    Total Prize       : ${fishcat * Weight}
                                    """
                                    output = [TotalPrize]
                        elif MeatChoose =="4":
                                    Weight = int(input("How many Pounds of meat do you want to buy? : "))
                                    TotalPrize = f"""
                                    Meat Type         : Salmon
                                    Weight            : {Weight} Pounds
                                    Prize / pounds    : ${Salmon}
                                    Total Prize       : ${Salmon * Weight}
                                    """
                                    output = [TotalPrize]

                        else :
                                    print("\nOption Aveilable,please try again!\n") 
                                    cuy = input("Mau lagi? Yes or No : ")
                                    if cuy =="Yes":
                                          continue
                                    elif cuy =="No":
                                          break
                                    else:
                                          print("Invalid option!")
                                          break     


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

# Fruits

