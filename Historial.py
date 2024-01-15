import pandas as pd 
import time
import scheduler
import schedule
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
        #Tandeo Cldera
        file_name = now.strftime("%Y-%m-%d-%H-%M-%S") + ".csv"
        directory = 'C:/Users/SOPORTE XOTEPINGO/Desktop/Historial/ElementosBaseTandeo/'
        os.makedirs(directory, exist_ok=True)
        file_path = os.path.join(directory, file_name)
        data= pd.read_csv(
         'https://docs.google.com/spreadsheets/d/10UQVSnrkNrrMTzTuDUaqZjooTePD1VITM223lJr2Kh8/export?gid=2114092871&format=csv&range=A2:C50')
        df = pd.DataFrame(data)
        df.to_csv(file_path, index=False)
        print("Elementos Base Tandeo Caldera\t",now,"\n","\n")

        #Puntos Estrategicos
        file_name1 = now.strftime("%Y-%m-%d-%H-%M-%S") + ".csv"
        directory1 = 'C:/Users/SOPORTE XOTEPINGO/Desktop/Historial/ElementosHidraulicos/'
        os.makedirs(directory1, exist_ok=True)
        file_path1 = os.path.join(directory1, file_name1)
        data1= pd.read_csv(
         'https://docs.google.com/spreadsheets/d/10UQVSnrkNrrMTzTuDUaqZjooTePD1VITM223lJr2Kh8/export?gid=1915421642&format=csv&range=A2:C56')
        df1 = pd.DataFrame(data1)
        df1.to_csv(file_path1, index=False)
        print("Elementos Hidraulicos Puntos Estrategicos\t",now,"\n","\n")

        #Tanques
        file_name2 = now.strftime("%Y-%m-%d-%H-%M-%S") + ".csv"
        directory2 = 'C:/Users/SOPORTE XOTEPINGO/Desktop/Historial/ElementosHidraulicostnq/'
        os.makedirs(directory2, exist_ok=True)
        file_path2 = os.path.join(directory2, file_name2)
        data2= pd.read_csv(
         'https://docs.google.com/spreadsheets/d/10UQVSnrkNrrMTzTuDUaqZjooTePD1VITM223lJr2Kh8/export?gid=1131062070&format=csv&range=A2:C20')
        df2 = pd.DataFrame(data2)
        df2.to_csv(file_path2, index=False)
        print("Elementos Hidraulicos Puntos Estrategicos\t",now,"\n","\n")

        time.sleep(900)







#historial()


"""
#Tandeo Cldera
file_name = now.strftime("%Y-%m-%d-%H-%M-%S") + ".csv"
directory = 'C:/Users/SOPORTE XOTEPINGO/Desktop/Historial/ElementosBaseTandeo/'
os.makedirs(directory, exist_ok=True)
file_path = os.path.join(directory, file_name)
data= pd.read_csv(
 'https://docs.google.com/spreadsheets/d/10UQVSnrkNrrMTzTuDUaqZjooTePD1VITM223lJr2Kh8/export?gid=2114092871&format=csv&range=A2:C50')
df = pd.DataFrame(data)
df.to_csv(file_path, index=False)
print("Elementos Base Tandeo Caldera\t",now,"\n",data,"\n")"""

"""
now = datetime.now()
df= pd.read_csv(
    'https://docs.google.com/spreadsheets/d/10UQVSnrkNrrMTzTuDUaqZjooTePD1VITM223lJr2Kh8/export?gid=2114092871&format=csv&range=A2:B50')
print("Elementos Base Tandeo Caldera\n",df,"\n")
df.to_csv('C:/Users/SOPORTE XOTEPINGO/Desktop/Historial/ElementosBaseTandeo/elementostandeo.csv')

df1=pd.read_csv(
   'https://docs.google.com/spreadsheets/d/10UQVSnrkNrrMTzTuDUaqZjooTePD1VITM223lJr2Kh8/export?gid=1915421642&format=csv&range=A2:B56')
print("Elementos Hidraulicos Puntos Estrategicos\n",df1,"\n")
df1.to_csv('C:/Users/SOPORTE XOTEPINGO/Desktop/Historial/ElementosHidraulicos/puntosestrategicos.csv')

df2=pd.read_csv(
   'https://docs.google.com/spreadsheets/d/10UQVSnrkNrrMTzTuDUaqZjooTePD1VITM223lJr2Kh8/export?gid=1131062070&format=csv&range=A2:B20' )
print("Elementos Hidraulicos Tnq Rb Caldera\n",df2,"\n")
df2.to_csv('C:/Users/SOPORTE XOTEPINGO/Desktop/Historial/ElementosHidraulicostnq/tanques.csv')"""
