import Fruit_manager_Moduel as fm
from Fruit_manager_Moduel import *

fruit_list = {}
F_name_list = []
F_buy_price_list = []
F_sell_price_list = []
F_quantity_list =[]




while True:
  
  print("........Welcome to Fruit Market........ ")
  print("""
      
      Select Option .........
      
        1). Fruit Manager
        
        2). Customer 
        
        3). Exit
      
      """)
  Choice = int(input("Enter Your Choice As Above (1/2)"))

    
  if Choice == 1:
        print("""
              
              ........Welcome Fruit Manger.........
              
            """)

  while True:
    
        print("""
              
              ....Which Operation You Want to do ?... 
              
              1). Add Fruit  stock
              
              2). View Fruit Stock
              
              3). Update Fruit Stock 
              
              4). Exit
              
              """)
    
        select = int(input("Select Option As Above(1/2/3) & 4 For Exit"))
        print(select)


        if select == 1:

              inputs = int(input("Enter How many Fruites You Want to Add"))
              print(inputs)
              for i in range (inputs):
                F_name = input("Enter Fruit name")
                F_name_list.append(F_name)
                print(F_name)
                F_Buy_price = int(input(f"Enter {F_name} Buying Price"))
                F_buy_price_list.append(F_Buy_price)
                print(F_Buy_price)
                F_sell_Price = int(input(f"Enter {F_name} Selling Price"))
                F_sell_price_list.append(F_sell_Price)
                print(F_sell_Price)
                F_Quantity = int(input(f"Enter How many {F_name} Quantities Is:"))
                F_quantity_list.append(F_Quantity)
                print(F_Quantity)
                fruit_list[F_name] = {"Buying":F_Buy_price,"Selling":F_sell_Price,"Quantity":F_Quantity}
                print(fruit_list)
                fm.add_fruit(F_name,F_Buy_price,F_sell_Price,F_Quantity,fruit_list)

        elif select == 2:

            print("......View Fruit Stock .......") 
            if F_name in fruit_list:
              fruit_list[F_name] = {"Buying":F_Buy_price,"Selling":F_sell_Price,"Quantity":F_Quantity}
              print(fruit_list)
            else:
              print("Fruit Not Added Yet")
              fm.View_Fruit_stock(fruit_list) 

        elif select == 3:

            print("..... Update Fruit Stock .....")
            F_name = input("Enter WHich Fruit You want to Update ")
            if F_name in F_name_list and F_name in fruit_list:
                print(fruit_list)
              
                F_Buy_price = int(input(f"Enter new Buying Price for {F_name}"))
                F_sell_Price = int(input(f"Enter new Selling Price for {F_name}"))
                F_Quantity = int(input(f"Enter new Quantity for {F_name}"))
                fruit_list[F_name] = {"Buying": F_Buy_price, "Selling": F_sell_Price, "Quantity": F_Quantity}
                print(fruit_list)

            else:
              print("Fruit Not In Stock")              
              fm.update_fruit(F_name, F_Buy_price, F_sell_Price, F_Quantity, fruit_list)
  
      