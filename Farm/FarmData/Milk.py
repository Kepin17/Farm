
def Milk():
      while True:
            try:
                  Milk = str(input("What milk do you want?\n1) Cow\n2) Goat\n Your Choose :"))

            except ValueError:
                        
                  print("Option Anvailable,please try again!")
                  continue
            else:
                  Cow = 15
                  Goat = 17
                  if Milk =="1":
                        liters = int(input("\nHow much liter do you want to buy?  : "))
                        Total = Cow * liters
                        Result = f"\nYou buy {liters} L Cow Milk and you must paid ${Total}"
                        output = [Result]
                 
                  elif Milk =="2":
                        liters = int(input("How much liter do you want to buy?  : "))
                        Total = Goat * liters
                        Result = f"\nYou buy {liters} L Goat Milk and you must paid ${Total}"
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
                        
