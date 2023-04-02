import numpy as np
import pandas as pd

import data_handler
from FuzzySets import *
from FuzzyHandler import *
from Predict import *
from StaticData import *
from Product import *
from Sale import *
from data_handler import *
import matplotlib.pyplot as plt


#p = Predict()
#print(p.PairsInRange(p.CreateMatrix([212, 312, 335, 465, 766, 886, 953]), 3))

StaticData.ReadProductCatalog('products.csv')
StaticData.ReadProductAdmission('in.csv')
StaticData.ReadProductSales('out1.csv')



f = open('valid-gtin.txt', 'r')
bc = 0
gtins = []
for line in f:
    gtins.append(line[:-1])
    if bc == 39:
        break
    bc += 1

print(gtins)




for gtin in gtins:
    pr = StaticData.data_product_catalog.loc[StaticData.data_product_catalog['gtin'] == gtin]
    for index, row in pr.iterrows():
        t_p = Product(row['gtin'], row['product_name'], row['brand'])

        sl = StaticData.data_product_sales.loc[StaticData.data_product_sales['gtin'] == gtin]

        for index, row in sl.iterrows():
            t_s = Sale(row['price'], row['cnt'], row['dt'])
            t_p.sales.append(t_s)

        StaticData.products.append(t_p)
        break


print(len(StaticData.products[20].sales))
print(len(StaticData.products[21].sales))
print(len(StaticData.products[22].sales))
print(len(StaticData.products[23].sales))
print(len(StaticData.products[24].sales))
print(len(StaticData.products[25].sales))
print(len(StaticData.products[26].sales))
print(len(StaticData.products[27].sales))
print(len(StaticData.products[28].sales))
print(len(StaticData.products[29].sales))
print(len(StaticData.products[30].sales))
print(len(StaticData.products[31].sales))
print(len(StaticData.products[32].sales))
print(len(StaticData.products[33].sales))
print(len(StaticData.products[34].sales))
print(len(StaticData.products[35].sales))
print(len(StaticData.products[36].sales))
print(len(StaticData.products[37].sales))
print(len(StaticData.products[38].sales))
print(len(StaticData.products[39].sales))

'''
data = []
date = []
for sale in StaticData.products[12].sales:
    data.append(sale.price / sale.cnt)
    date.append(sale.dt)

#data = data_handler.DataRejection.GetConfidenceInterval(data, CharNames.PRICE)
print(len(data))
print(len(date))

res = data_handler.DataRejection.GetConfidenceInterval(data, "Price", date)
data = res[0]
date = res[1]

plt.subplot(2, 2, 1)
plt.plot(date[:50], data[:50])
'''


data1 = []
date1 = []
for sale in StaticData.products[20].sales:
    data1.append(sale.price / sale.cnt)
    date1.append(sale.dt)

#data = data_handler.DataRejection.GetConfidenceInterval(data, CharNames.PRICE)
print(len(data1))
print(len(date1))

res1 = data_handler.DataRejection.GetConfidenceInterval(data1, "Price", date1)
data1 = res1[0]
date1 = res1[1]

plt.subplot(2, 2, 1)
plt.plot(date1[:50], data1[:50])



data2 = []
date2 = []
for sale in StaticData.products[17].sales:
    data2.append(sale.price / sale.cnt)
    date2.append(sale.dt)

#data = data_handler.DataRejection.GetConfidenceInterval(data, CharNames.PRICE)
print(len(data1))
print(len(date1))

res1 = data_handler.DataRejection.GetConfidenceInterval(data1, "Price", date1)
data1 = res1[0]
date1 = res1[1]

plt.subplot(2, 2, 2)
plt.plot(date1[:15], data1[:15])
plt.fill_between([date1[15], date1[25]], [16000, 17000], [16000, 15500], color="red")

plt.subplot(2, 2, 3)
plt.plot(date1[:25], data1[:25])
plt.fill_between([date1[25], date1[35]], [20000, 23000], [20000, 19000], color="red")

plt.subplot(2, 2, 4)
plt.plot(date1[:44], data1[:44])
plt.fill_between([date1[35], date1[44]], [22000, 23000], [22000, 21000], color="red")
plt.show()



'''

it = 0
for index, row in StaticData.data_product_catalog.iterrows():
    print(it)
    t_p = Product(row['gtin'], row['product_name'], row['brand'])
    t_p.LoadAdmission()
    StaticData.products.append(t_p)
    it += 1

file = open("valid-gtin.txt", "w")
for prod in StaticData.products:
    if len(prod.admission) > 0:
        file.write(prod.gtin + '\n')

file.close()

'''

'''

mainPred = Predict([10, 30, 25, 15, 22], ["22.03", "23.03", "24.03", "25.03", "26.03"])
mainPred.CreatePlot()

inp = ""
arr = []
print("Введите любое количество чисел. Для завершения введите 0")
while inp != "0":
    inp = input()
    if inp != "0":
        arr.append(int(inp))

r = Patterns.GetType(arr)

print(f"Ваш ряд: {arr}")

if r == Patterns.NONE:
    print("Тип ряда: Невозможно определить")
elif r == Patterns.UP:
    print("Тип ряда: Возрастающий")
elif r == Patterns.DOWN:
    print("Тип ряда: Убывающий")
elif r == Patterns.STABLE:
    print("Тип ряда: Стабильный")
else:
    print("Тип ряда: Нестабильный")

'''