import json
import datetime


#file managment-------------------------------------------------------------------
def data_reading(file_dir):
    with open(f"{file_dir}","r") as file:
        data=json.load(file)
    return data

def data_saving(data,file_dir):
    with open(f"{file_dir}","w") as file:
        json.dump(data,file)
        
        
#changing by cmnd------------------------------------------------------------------------------------
def save_order(cmd,money):
    data=data_reading("data/data.json")
    log = data_reading("log/last_log.json")
    log[str(datetime.datetime.now())]=[[data[cmd][0],data[cmd][1]],[money,money-data[cmd][1]]]
    data_saving(log,"log/last_log.json")

def product_redusing(cmd):
    data=data_reading("data/data.json")
    data[cmd][2]-=1
    data_saving(data,"data/data.json")
    
    
#maintenance-------------------------------------------------------------------------
def daily_win(file_dir):
    b=0
    for i in data_reading(file_dir):
        b+=data_reading(file_dir)[i][0][1]
    return b

def daily_data(file_dir):
    print(f"There was {len(data_reading(file_dir))} order")
    print(f"your day sells {daily_win(file_dir)} DA")
    
def vide_cash():
    with open(f"log/{str(datetime.date.today())}.txt" , "w") as log_file:
        log_file.write(str(data_reading("log/last_log.json")))
    data_saving({},"log/last_log.json")
    
def past_data_recover():
    date=input("what day you wanna recover")
    try:
        with open(f"log/{date}.txt" , "r") as log:
            data=log.read()
        with open("log/tmp.json","w") as tmp_file:
            tmp_file.write(data)
        daily_data("log/tmp.json")
        data_saving({},"log/tmp.json")
    except:
        print("Wrong date or not existed date")