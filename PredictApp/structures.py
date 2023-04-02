class Characteristics:
    def __init__(self):
        ...

    # --Проверка на целостность--
    def CheckNone(self):
        ...

class Operation:
    def __init__(self):
        ...

class Address:
    def __init__(self):
        ...

class MovePoint:
    def __init__(self):
        ...

class Product:
    def __init__(self):
        self.name = "DEFAULT_NAME" # наименование товара
        self.description = "DEFAULT_DESCRIPTION" # описание товара
        self.chars = Characteristics() # список характеристик
        self.producer = "DEFAULT_PRODUCER" # производитель

    def __eq__(self, other):
        return self.name == other.name and self.producer == other.producer

    # --Проверка на целостность--
    def CheckNone(self):
        return self.name is None\
                or self.description is None\
                or self.producer is None\
                or self.chars.CheckNone()

class Sale:
    def __init__(self):
        self.product = Product() # товар в акте продажи
        self.orderAddress = Address() # конечный адрес доставки (до улицы)
        self.orderDatetime = "01.01.1970 00:00:00" # дата и время формирования акта продажи
        self.moveChain = [] # данные о движении товара
        self.operationChain = []  # массив класса Operation
        self.priceChain = []  # массив вещественных чисел - цен на каждом этапе товарной цепи

    def __eq__(self, other):
        return self.orderDatetime == other.orderDatetime\
               and self.orderAddress == other.orderAddress\
               and self.product == self.product