from FarmData import MeatShop , FruitsShop , Milk , Eggs

cuy = "Yes"
while cuy =="Yes":
  print(10*"=","Welcome to Kevien Farm","="*10)
  point = str(input("What do you want :\n1) Purchise\n2) Ceck Stock\n Choose : "))
  if point =="2":
      print("Stock Always Ready!!!")
  elif point =="1":  
    ShopList = str(input("\nWhat do you want to buy :\n1) Meats\n2) Fruits\n3) Milk\n4) Egg\nPilihanmu : "))
    
    if ShopList =="1":
        output = MeatShop()    
        print("{}".format(output[0])) 
    elif ShopList =="2":
        output = FruitsShop()    
        print("{}".format(output[0])) 
    elif ShopList =="3":
        output = Milk()    
        print("{}".format(output[0])) 
    elif ShopList =="4":
        output = Eggs()    
        print("{}".format(output[0])) 
    else:
        print(
            """
            Yang bener napa,Gelud lah kita!
            """
            )    

  cuy = input("\nThere's something else to buy? Yes or No : ")
  if cuy =="Yes":
      continue
  elif cuy =="No":
      break
  else:
      print("Invalid option!")
      break        
else:
    print("Please try again!")
print("Akhir pemograman")        