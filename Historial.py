import pandas as pd 
import time
import sched
import csv
import os
from datetime import datetime
#now = datetime.now()
#now1=time.now1();
#n=0
while True:
    now = datetime.now()
    if now.hour>=8 and now.hour<22:
        #Tandeo Tlalpan
        file_name = now.strftime("%Y-%m-%d-%H-%M-%S") + ".csv"
        directory = 'E:/python/Historial/ElementosHidraulicostnq' 
        os.makedirs(directory, exist_ok=True)
        file_path = os.path.join(directory, file_name)
        data= pd.read_csv(
         'https://docs.google.com/spreadsheets/d/1Kcbe_69XSzC8u-Wk8e-WOLN-PGra2dJPEuu7TQCH1_c/export?gid=438614075&format=csv&range=A2:C23')
        df = pd.DataFrame(data)
        df.to_csv(file_path, index=False)
        print("Elementos tanques tlalpan\t",now,"\n")

        #Puntos Estrategicos
        # file_name1 = now.strftime("%Y-%m-%d-%H-%M-%S") + ".csv"
        # directory1 = 'C:/Users/Administrator/Desktop/MonitoreoV2/Historial/ElementosHidraulicos/'
        # os.makedirs(directory1, exist_ok=True)
        # file_path1 = os.path.join(directory1, file_name1)
        # data1= pd.read_csv(
        #  'https://docs.google.com/spreadsheets/d/10UQVSnrkNrrMTzTuDUaqZjooTePD1VITM223lJr2Kh8/export?gid=1915421642&format=csv&range=A2:C56')
        # df1 = pd.DataFrame(data1)
        # df1.to_csv(file_path1, index=False)
        # print("Elementos Hidraulicos Puntos Estrategicos\t",now,"\n","\n")

        #Tanques
        # file_name2 = now.strftime("%Y-%m-%d-%H-%M-%S") + ".csv"
        # directory2 = 'C:/Users/Administrator/Desktop/MonitoreoV2/Historial/ElementosHidraulicostnq/'
        # os.makedirs(directory2, exist_ok=True)
        # file_path2 = os.path.join(directory2, file_name2)
        # data2= pd.read_csv(
        #  'https://docs.google.com/spreadsheets/d/10UQVSnrkNrrMTzTuDUaqZjooTePD1VITM223lJr2Kh8/export?gid=1131062070&format=csv&range=A2:C20')
        # df2 = pd.DataFrame(data2)
        # df2.to_csv(file_path2, index=False)
        # print("Elementos Hidraulicos Puntos Estrategicos\t",now,"\n","\n")

        time.sleep(900)
