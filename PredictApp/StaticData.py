import numpy as np
import pandas as pd


class StaticData:
    data_product_catalog = None
    data_product_admission = None
    data_product_sales = None
    data_product_move = None

    products = []

    @staticmethod
    def ReadProductCatalog(filename):
        data = pd.read_csv(filename, delimiter=',')
        StaticData.data_product_catalog = data[['gtin', 'inn', 'product_name', 'brand', 'country']]

    @staticmethod
    def ReadProductAdmission(filename):
        data = pd.read_csv(filename, delimiter=',')
        StaticData.data_product_admission = data[['dt', 'inn', 'gtin', 'cnt']]

    @staticmethod
    def ReadProductSales(filename):
        data = pd.read_csv(filename, delimiter=',')
        StaticData.data_product_sales = data[['dt', 'gtin', 'inn', 'price', 'cnt']]
        StaticData.data_product_sales = StaticData.data_product_sales.sort_values(by=['dt', 'gtin'])


    @staticmethod
    def ReadProductMove(filename):
        ...

