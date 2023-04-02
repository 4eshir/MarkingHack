from constants import *
import re

class DataCleaner:
    @staticmethod
    def CheckInvalidValuePrice(value):
        return value.isnumeric() and value >= Price.MIN and value <= Price.MAX

    @staticmethod
    def CheckInvalidValueName(value):
        if not re.fullmatch(r'[a-zA-Zа-яА-Я]*', value):
            value = re.sub(r'[^a-zA-Zа-яА-Я]*', '', value)
        return value

    # --Основной метод проверки данных на валидность--
    @staticmethod
    def CheckInvalidValue(charType, value):
        if charType == CharNames.PRICE:
            return DataCleaner.CheckInvalidValuePrice(value)
        elif charType == CharNames.NAME:
            return DataCleaner.CheckInvalidValueName(value)
    # -------------------------------------------------

    # --Основной метод проверки данных на нарушение логических связей--
    @staticmethod
    def CheckLogicConnections(product):
        ...
    # -----------------------------------------------------------------

    # --Основной метод проверки данных на уникальность--
    @staticmethod
    def CheckUnique(sales):
        for i in range(len(sales)):
            for j in range(i, len(sales)):
                if sales[i] == sales[j]:
                    sales.pop(j)
        return sales
    # ---------------------------------------------------

    # --Основной метод проверки данных на целостность--
    @staticmethod
    def CheckIntegrity(sales):
        for i in range(len(sales)):
            if sales[i].orderAddress is None\
                or sales[i].orderDatetime is None\
                or sales[i].moveChain is None\
                or sales[i].operationChain is None\
                or sales[i].priceChain is None\
                or sales[i].orderAddress.CheckNone():
                sales.pop(i)
        return sales
    # -------------------------------------------------


class DataRejection:

    # --Метод вычисления доверительного интервала--
    @staticmethod
    def GetConfidenceInterval(sales, valueType, dates=None):
        # --Среднее арифметическое итоговых цен--
        sumPrice = 0
        for sale in sales:
            if valueType == CharNames.PRICE:
                sumPrice += sale

        if valueType == CharNames.PRICE:
            sumPrice /= len(sales)
        # ---------------------------------------

        # --Медиана ряда--
        mIndex = len(sales) // 2 if len(sales) % 2 == 0 else len(sales) // 2 + 1
        median = sales[mIndex]
        # ----------------

        # --Минимальная и максимальная стоимость--
        minPrice = sales[0]
        maxPrice = sales[0]
        sigma = 0

        for sale in sales:
            sigma += sale
            if sale > maxPrice:
                maxPrice = sale
            if sale < minPrice:
                minPrice = sale
        # ------------------------------------------

        # --Размах, дисперсия, среднекв. отклонение, коэффициенты--
        r = maxPrice - minPrice

        dispersion = (1 / (len(sales) - 1)) * sigma
        standardDev = dispersion ** (0.5)
        variationCoeff = (standardDev / sumPrice) * 100
        oscillationCoeff = (r / sumPrice) * 100

        confInterval = [0, 0]
        #confInterval[0] = median - standardDev
        #confInterval[1] = median + standardDev
        confInterval[0] = median - median * 0.5
        confInterval[1] = median + median * 0.5
        # ---------------------------------------------------------

        # --Отбор данных, попадающих в доверительный интервал--
        newSales = []
        newDates = []

        for i in range(len(sales)):
            if sales[i] >= confInterval[0] and sales[i] <= confInterval[1]:
                newSales.append(sales[i])
                newDates.append(dates[i])
        # -----------------------------------------------------

        return [newSales, newDates]


    # ---------------------------------------------

