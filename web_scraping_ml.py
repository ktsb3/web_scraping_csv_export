import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

if __name__ == '__main__':
    r1 = requests.get('https://listado.mercadolibre.com.mx/rtx-2080#D[A:rtx%202080]')
    soup1 = BeautifulSoup(r1.text, 'html.parser')
    nombre1 = soup1.find_all('span', attrs={'class':'main-title'})
    precio1 = soup1.find_all('span', attrs={'class':'price__fraction'})
    vendido1 = soup1.find_all('div', attrs={'class':'item__condition'})
    nombres = []
    precios = []
    vendidos = []
    for i in range(49):
        nombres.append(nombre1[i])
        precios.append(precio1[i])
        vendidos.append(vendido1[i])

    enlaces = []
    for link in soup1.find_all('a'):
        href = "" + str(link.get("href"))
        if(len(href)>37):
            if(href[37] == 'M'):
               enlaces.append(href)
    
    r2 = requests.get('https://computacion.mercadolibre.com.mx/tarjetas-video/tarjetas-video/pci-express/nvidia/rtx-2080_Desde_51')
    soup2 = BeautifulSoup(r2.text, 'html.parser')
    nombre2 = soup2.find_all('span', attrs={'class':'main-title'})
    precio2 = soup2.find_all('span', attrs={'class':'price__fraction'})
    vendido2 = soup2.find_all('div', attrs={'class':'item__condition'})
    for i in range(49):
        nombres.append(nombre2[i])
        precios.append(precio2[i])
        vendidos.append(vendido2[i])

    for link in soup2.find_all('a'):
        href = "" + str(link.get("href"))
        if(len(href)>37):
            if(href[37] == 'M'):
                enlaces.append(href)
               
    r3 = requests.get('https://computacion.mercadolibre.com.mx/tarjetas-video/tarjetas-video/pci-express/nvidia/rtx-2080_Desde_101')
    soup3 = BeautifulSoup(r3.text, 'html.parser')
    nombre3 = soup3.find_all('span', attrs={'class':'main-title'})
    precio3 = soup3.find_all('span', attrs={'class':'price__fraction'})
    vendido3 = soup3.find_all('div', attrs={'class':'item__condition'})
    for i in range(35):
        nombres.append(nombre3[i])
        precios.append(precio3[i])
        vendidos.append(vendido3[i])

    for link in soup3.find_all('a'):
        href = "" + str(link.get("href"))
        if(len(href)>37):
            if(href[37] == 'M'):
                enlaces.append(href)

    enlaces2 = enlaces[0:133]
    
    dic = {'nombre': nombres, 'precio':precios, 'vendido':vendidos, 'enlace':enlaces2}
    csv = pd.DataFrame(dic)
    csv.to_csv('lista_ml.csv')