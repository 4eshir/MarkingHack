import matplotlib.pyplot as plt

import data_handler


class Predict:

    def __init__(self, sales=None, dates=None, dpf=None, de=None, op=None, adr=None):
        # Данные для отображения на графике
        self.sales_array = sales
        self.dates_array = dates
        # ---------------------------------

        # Данные для предиктивной аналитики
        self.dprice_finish = dpf
        self.dentering = de
        self.overprice = op
        self.addresses_type = adr
        # ---------------------------------

    def CreatePlot(self):
        plt.plot(self.dates_array, self.sales_array)
        plt.plot([self.dates_array[-1]] + ["27.03"], [self.sales_array[-1]] + [27], linestyle='--', color="#FF0000")
        plt.plot([self.dates_array[-1]] + ["27.03"], [self.sales_array[-1]] + [20], linestyle='--', color="#FF0000")

        plt.fill_between([self.dates_array[-1]] + ["27.03"], [self.sales_array[-1]] + [27], [self.sales_array[-1]] + [20], color="#F08080")

        plt.show()

    def CreateMatrix(self, array):
        matrix = []
        i = 0
        while i < len(array) - 1:
            j = i + 1
            matrix.append([])
            while j < len(array):
                t = i
                matrix[-1].append([])
                while t <= j:
                    matrix[-1][-1].append(array[t])
                    t += 1
                j += 1
            i += 1

        return matrix

    def PairsInRange(self, matrix, p_range):
        res = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if len(matrix[i][j]) >= p_range:
                    res.append(matrix[i][j])

        return res


    def GetPredict(self, pred_size):
        matrixDprice = self.CreateMatrix(self.dprice_finish)
        matrixDentering = self.CreateMatrix(self.dentering)
        matrixOverprice = self.CreateMatrix(self.overprice)



    def Drop(self, data, date):
        res = data_handler.DataRejection.GetConfidenceInterval(data, "Price", date)
        return res