
def Eggs():
      while True:
            try:
                  Eggs = int(input("How much eggs will you buy? :"))

            except ValueError:
                        
                  print("Option Anvailable,please try again!")
                  continue
            else:
                  prize = 10
                  Total = f"\nYou buy {Eggs} Eggs and you must pay ${prize * Eggs}"
                  output = [Total]          

            break
      return output            
                        
