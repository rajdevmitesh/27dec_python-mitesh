
fruit_list = {}
F_name_list = []
F_buy_price_list = []
F_sell_price_list = []
F_quantity_list =[]

def add_fruit(F_name,F_Buy_price,F_sell_Price,F_Quantity,stock):
    fruit_list[F_name] = {"Buying":F_Buy_price,"Selling":F_sell_Price,"Quantity":F_Quantity}
    print("Fruit added successfully")
    print("New stock of Fruit is :",stock)
    
def View_Fruit_stock(F_list):
    x = add_fruit(F_list)
    print(x)
    
def update_fruit_stock(F_name):
    print("Your Id is: ",F_name)
    print("Fruit stock updated successfully")
        
    