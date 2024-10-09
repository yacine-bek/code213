import data_mng
import printing

stay=1
while(stay==1):
    print("---------------------------------------------------------------")
    printing.menu_printing()
    choice=input("enter your choice : ")
    if choice=="1200":
        print("1.Editing")
        print("2.See daily data")
        print("3.vide cash")
        print("4.see past day orders and data")
        chwa=input()
        if chwa=="1":
            printing.data_editing()
        elif chwa=="2":
            data_mng.daily_data("log/last_log.json")
        elif chwa=="3":
            data_mng.vide_cash()
        elif chwa=="4":
            data_mng.past_data_recover()
    elif choice in data_mng.data_reading("data/data.json"):
        printing.taking_cmd(choice)
    elif choice=="1212":
        stay=0
    else:
        print("this choice doese not exist")
print("machine stoped...")