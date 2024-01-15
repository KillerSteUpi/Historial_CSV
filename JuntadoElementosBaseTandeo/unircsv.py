import os
import glob
import pandas as pd
   
os.chdir("C:/Users/SOPORTE XOTEPINGO/Desktop/Historial/ElementosBaseTandeo")
extension = 'csv'
todos_los_archivos = [i for i in glob.glob('*.{}'.format(extension))]
#combina todos los archivos de la lista
combinado_csv = pd.concat([pd.read_csv(f) for f in todos_los_archivos ])
#exporta a csv
combinado_csv.to_csv( "ElementosTandeoCaldera_csv.csv", index=False, encoding='utf-8-sig')
print("Combinado con exito ")

   

