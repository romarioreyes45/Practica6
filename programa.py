import pandas as pd
import xml.etree.ElementTree as ET
import os

#Ruta donde se encuentra el archivo CSV
ruta_archivo = r'sales_data.csv'

#Carga del archivo en un DataFrame
df = pd.read_csv(ruta_archivo, encoding='ISO-8859-1')

#Filtrar las filas donde 'STATE' no sea nulo
df_filtrado = df.dropna(subset=['STATE'])

#Definir la carpeta destino
ruta_destino = r"C:\Users\oscar\Desktop\ESCOM\Quinto Semestre\BDA\resultado6"
os.makedirs(ruta_destino, exist_ok=True)

#Crear el elemento raíz del XML
raiz = ET.Element("root")
for _, fila in df_filtrado.iterrows():
    item = ET.SubElement(raiz, "item")
    for columna in df_filtrado.columns:
        subelemento = ET.SubElement(item, columna)
        subelemento.text = str(fila[columna])

#Guardar el archivo XML en la carpeta de destino
ruta_xml = os.path.join(ruta_destino, 'sales_data.xml')
arbol = ET.ElementTree(raiz)
arbol.write(ruta_xml, encoding='utf-8', xml_declaration=True)

print(f"Archivo XML guardado en: {ruta_xml}")
