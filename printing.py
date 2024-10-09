import data_mng

#menu---------------------------------------------------------------------------------------------------
def menu_printing():
    data=data_mng.data_reading("data/data.json")
    k=0
    for i in data:
        print(f"{i}. {data[i][0]} : {data[i][1]} DA")
        
def all_data_printing():
    data=data_mng.data_reading("data/data.json")
    k=0
    for i in data:
        k+=1
        print(f"{k}. {data[i][0]} : {data[i][1]} DA   ({data[i][2]})")


#every order------------------------------------------------------------------------------------------------------------------
def taking_cmd(cmd):
    if data_mng.data_reading("data/data.json")[cmd][2]==0:
        print("The product is finished.")
    else:
        money=int(input(f"it cost you {data_mng.data_reading('data/data.json')[cmd][1]} DA : "))
        if money<data_mng.data_reading("data/data.json")[cmd][1] : 
            print("----------------------------------------")
            print(f"Invalide operation!!\nYou still need {data_mng.data_reading('data/data.json')[cmd][1]-money} DA")
            print("----------------------------------------")
        else:
            print("----------------------------------------")
            if (money-data_mng.data_reading("data/data.json")[cmd][1]==0):
                print(f"You can take your {data_mng.data_reading('data/data.json')[cmd][0]}")
            else:
                print(f"You can take your {data_mng.data_reading('data/data.json')[cmd][0]}\nand this is your change: {money- data_mng.data_reading('data/data.json')[cmd][1]} DA")
            data_mng.save_order(cmd,money)
            data_mng.product_redusing(cmd)
            
            
#maintenance screen--------------------------------------------------------------------------------------------------------------------
def data_editing():
    all_data_printing()
    mn_choice=input("what you wanna modify : ")
    if mn_choice in data_mng.data_reading("data/data.json"):
        data=data_mng.data_reading("data/data.json")
        choice=input(f"what did you wanna edit in {data[mn_choice][0]} : \n1. Price\n2. Quantity\n0. Cancel operation")
        if choice=="1":
            data[mn_choice][int(choice)]=int(input(f"enter the new price of the {data[mn_choice][0]} : "))
            data_mng.data_saving(data,"data/data.json")
            print("edited successfully")
        elif choice=="2":
            data[mn_choice][int(choice)]=int(input(f"enter the new Quantity of the {data[mn_choice][0]} : "))
            data_mng.data_saving(data,"data/data.json")
            print("edited successfully")
        elif choice=="0":
            return
        else:
            print("wrong choice")