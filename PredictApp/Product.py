import numpy as np
import pandas as pd

from Admis import *
from StaticData import *


class Product:

    def __init__(self, t_gtin, t_product_name, t_brand):
        self.gtin = t_gtin
        self.product_name = t_product_name
        self.brand = t_brand

        self.admission = []
        self.sales = []

    def LoadAdmission(self):
        target = StaticData.data_product_admission.loc[StaticData.data_product_admission['gtin'] == self.gtin]
        if not target.empty:
            for index, row in target.iterrows():
                t_admis = Admis(row['dt'], row['inn'], row['cnt'])
                self.admission.append(t_admis)