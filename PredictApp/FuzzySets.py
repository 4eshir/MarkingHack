import random


class Price:
    VERY_CHEAP = 0
    CHEAP = 1
    NORMAL = 2
    EXPENSIVE = 3
    VERY_EXPENSIVE = 4

    price_very_cheap1 = 0
    price_very_cheap2 = 200
    price_very_cheap3 = 300

    price_cheap1 = 200
    price_cheap2 = 300
    price_cheap3 = 500
    price_cheap4 = 600

    price_normal1 = 500
    price_normal2 = 600
    price_normal3 = 800
    price_normal4 = 900

    price_expensive1 = 800
    price_expensive2 = 900
    price_expensive3 = 1100
    price_expensive4 = 1200

    price_very_expensive1 = 1100
    price_very_expensive2 = 1200
    price_very_expensive3 = 10000

    sets = [
        [price_very_cheap1, price_very_cheap2, price_very_cheap3], # Очень дешево
        [price_cheap1, price_cheap2, price_cheap3, price_cheap4], # Дешево
        [price_normal1, price_normal2, price_normal3, price_normal4], # Нормально
        [price_expensive1, price_expensive2, price_expensive3, price_expensive4], # Дорого
        [price_very_expensive1, price_very_expensive2, price_very_expensive3] # Очень дорого
    ]

    @staticmethod
    def fuzzy_random(percent):
        r = random.randrange(1, 100)
        return r >= percent

    @staticmethod
    def belonging(value):
        for i in range(len(Price.sets)):
            if value > Price.sets[i][len(Price.sets[i]) - 1]:
                continue
            else:
                if i == 0:
                    # в зоне "очень дешево"
                    if value <= Price.price_very_cheap2:
                        return Price.VERY_CHEAP
                    else:
                        res = Price.fuzzy_random(round((Price.price_very_cheap3 - value) / (Price.price_very_cheap3 - Price.price_very_cheap2) * 100))
                        if res:
                            return Price.CHEAP
                        else:
                            return Price.VERY_CHEAP
                    # ---------------------
                elif i == len(Price.sets) - 1:
                    # в зоне "очень дорого"
                    if value >= Price.price_very_expensive2:
                        return Price.VERY_EXPENSIVE
                    else:
                        res = Price.fuzzy_random(round((Price.price_very_expensive2 - value) / (Price.price_very_expensive2 - Price.price_very_expensive1) * 100))
                        if res:
                            return Price.EXPENSIVE
                        else:
                            return Price.VERY_EXPENSIVE
                    # ---------------------
                else:
                    # в остальных зонах
                    if value >= Price.sets[i][1] and value <= Price.sets[i][2]:
                        return i
                    elif value < Price.sets[i][1]:
                        res = Price.fuzzy_random(round((Price.sets[i][1] - value) / (Price.sets[i][1] - Price.sets[i][0]) * 100))
                        if res:
                            return i - 1
                        else:
                            return i
                    else:
                        res = Price.fuzzy_random(round((Price.sets[i][3] - value) / (Price.sets[i][3] - Price.sets[i][2]) * 100))
                        if res:
                            return i + 1
                        else:
                            return i
                    # -----------------


class Address:
    CLOSE = 0
    NORMAL = 1
    FAR = 2

    address_close1 = 0
    address_close2 = 1
    address_close3 = 1.5

    address_normal1 = 1
    address_normal2 = 1.5
    address_normal3 = 2.5
    address_normal4 = 3

    address_far1 = 2.5
    address_far2 = 3
    address_far3 = 1000000

    sets = [
        [address_close1, address_close2, address_close3], # Близко
        [address_normal1, address_normal2, address_normal3, address_normal4], # Нормально
        [address_far1, address_far2, address_far3], # Далеко
    ]

    @staticmethod
    def fuzzy_random(percent):
        r = random.randrange(1, 100)
        return r >= percent

    @staticmethod
    def belonging(value):
        for i in range(len(Address.sets)):
            if value > Address.sets[i][len(Address.sets[i]) - 1]:
                continue
            else:
                if i == 0:
                    # в зоне "близко"
                    if value <= Address.address_close2:
                        return Address.CLOSE
                    else:
                        res = Address.fuzzy_random(round((Address.address_close3 - value) / (Address.address_close3 - Address.address_close2) * 100))
                        if res:
                            return Address.NORMAL
                        else:
                            return Address.CLOSE
                    # ---------------------
                elif i == len(Address.sets) - 1:
                    # в зоне "далеко"
                    if value >= Address.address_far2:
                        return Address.FAR
                    else:
                        res = Address.fuzzy_random(round((Address.address_far2 - value) / (Address.address_far2 - Address.address_far1) * 100))
                        if res:
                            return Address.NORMAL
                        else:
                            return Address.FAR
                    # ---------------------
                else:
                    # в остальных зонах
                    if value >= Address.sets[i][1] and value <= Address.sets[i][2]:
                        return i
                    elif value < Address.sets[i][1]:
                        res = Address.fuzzy_random(round((Address.sets[i][1] - value) / (Address.sets[i][1] - Address.sets[i][0]) * 100))
                        if res:
                            return i - 1
                        else:
                            return i
                    else:
                        res = Address.fuzzy_random(round((Address.sets[i][3] - value) / (Address.sets[i][3] - Address.sets[i][2]) * 100))
                        if res:
                            return i + 1
                        else:
                            return i
                    # -----------------


class Entering:
    VERY_FAST = 0
    FAST = 1
    NORMAL = 2
    LONG = 3

    entering_very_fast1 = 0
    entering_very_fast2 = 200
    entering_very_fast3 = 300

    entering_fast1 = 200
    entering_fast2 = 300
    entering_fast3 = 500
    entering_fast4 = 600

    entering_normal1 = 500
    entering_normal2 = 600
    entering_normal3 = 800
    entering_normal4 = 900

    entering_long1 = 800
    entering_long2 = 900
    entering_long3 = 1000000

    sets = [
        [entering_very_fast1, entering_very_fast2, entering_very_fast3], # Очень быстро
        [entering_fast1, entering_fast2, entering_fast3, entering_fast4], # Быстро
        [entering_normal1, entering_normal2, entering_normal3, entering_normal4], # Нормально
        [entering_long1, entering_long2, entering_long3], # Долго
    ]

    @staticmethod
    def fuzzy_random(percent):
        r = random.randrange(1, 100)
        return r >= percent

    @staticmethod
    def belonging(value):
        for i in range(len(Entering.sets)):
            if value > Entering.sets[i][len(Entering.sets[i]) - 1]:
                continue
            else:
                if i == 0:
                    # в зоне "очень быстро"
                    if value <= Entering.entering_very_fast2:
                        return Entering.VERY_FAST
                    else:
                        res = Entering.fuzzy_random(round((Entering.entering_very_fast3 - value) / (Entering.entering_very_fast3 - Entering.entering_very_fast2) * 100))
                        if res:
                            return Entering.FAST
                        else:
                            return Entering.VERY_FAST
                    # ---------------------
                elif i == len(Entering.sets) - 1:
                    # в зоне "долго"
                    if value >= Entering.entering_long2:
                        return Entering.LONG
                    else:
                        res = Entering.fuzzy_random(round((Entering.entering_long2 - value) / (Entering.entering_long2 - Entering.entering_long1) * 100))
                        if res:
                            return Entering.NORMAL
                        else:
                            return Entering.LONG
                    # --------------
                else:
                    # в остальных зонах
                    if value >= Entering.sets[i][1] and value <= Entering.sets[i][2]:
                        return i
                    elif value < Entering.sets[i][1]:
                        res = Entering.fuzzy_random(round((Entering.sets[i][1] - value) / (Entering.sets[i][1] - Entering.sets[i][0]) * 100))
                        if res:
                            return i - 1
                        else:
                            return i
                    else:
                        res = Entering.fuzzy_random(round((Entering.sets[i][3] - value) / (Entering.sets[i][3] - Entering.sets[i][2]) * 100))
                        if res:
                            return i + 1
                        else:
                            return i
                    # -----------------


class DSales:
    VERY_LOWERED = 0
    LOWERED = 1
    NO_CHANGES = 2
    GROWED = 3
    VERY_GROWED = 4

    dsales_very_lowered1 = -150
    dsales_very_lowered2 = -100
    dsales_very_lowered3 = -75

    dsales_lowered1 = -100
    dsales_lowered2 = -75
    dsales_lowered3 = -25
    dsales_lowered4 = 0

    dsales_no_changes1 = -25
    dsales_no_changes2 = 0
    dsales_no_changes3 = 50
    dsales_no_changes4 = 75

    dsales_growed1 = 50
    dsales_growed2 = 75
    dsales_growed3 = 125
    dsales_growed4 = 150

    dsales_very_growed1 = 125
    dsales_very_growed2 = 150
    dsales_very_growed3 = 10000

    sets = [
        [dsales_very_lowered1, dsales_very_lowered2, dsales_very_lowered3], # Значительно упали
        [dsales_lowered1, dsales_lowered2, dsales_lowered3, dsales_lowered4], # Упали
        [dsales_no_changes1, dsales_no_changes2, dsales_no_changes3, dsales_no_changes4], # Практически не изменились
        [dsales_growed1, dsales_growed2, dsales_growed3, dsales_growed4], # Выросли
        [dsales_very_growed1, dsales_very_growed2, dsales_very_growed3] # Значительно выросли
    ]

    @staticmethod
    def fuzzy_random(percent):
        r = random.randrange(1, 100)
        return r >= percent

    @staticmethod
    def belonging(value):
        for i in range(len(DSales.sets)):
            if value > DSales.sets[i][len(DSales.sets[i]) - 1]:
                continue
            else:
                if i == 0:
                    # в зоне "значительно упали"
                    if value <= DSales.dsales_very_lowered2:
                        return DSales.VERY_LOWERED
                    else:
                        res = DSales.fuzzy_random(round((DSales.dsales_very_lowered3 - value) / (DSales.dsales_very_lowered3 - DSales.dsales_very_lowered2) * 100))
                        if res:
                            return DSales.LOWERED
                        else:
                            return DSales.VERY_LOWERED
                    # --------------------------
                elif i == len(DSales.sets) - 1:
                    # в зоне "очень дорого"
                    if value >= DSales.dsales_very_growed2:
                        return DSales.VERY_GROWED
                    else:
                        res = DSales.fuzzy_random(round((DSales.dsales_very_growed2 - value) / (DSales.dsales_very_growed2 - DSales.dsales_very_growed1) * 100))
                        if res:
                            return DSales.GROWED
                        else:
                            return DSales.VERY_GROWED
                    # ---------------------
                else:
                    # в остальных зонах
                    if value >= DSales.sets[i][1] and value <= DSales.sets[i][2]:
                        return i
                    elif value < DSales.sets[i][1]:
                        res = DSales.fuzzy_random(round((DSales.sets[i][1] - value) / (DSales.sets[i][1] - DSales.sets[i][0]) * 100))
                        if res:
                            return i - 1
                        else:
                            return i
                    else:
                        res = DSales.fuzzy_random(round((DSales.sets[i][3] - value) / (DSales.sets[i][3] - DSales.sets[i][2]) * 100))
                        if res:
                            return i + 1
                        else:
                            return i
                    # -----------------


class DPrice:
    VERY_LOWERED = 0
    NO_CHANGES = 1
    GROWED = 2
    VERY_GROWED = 3

    dprice_very_lowered1 = 0
    dprice_very_lowered2 = 200
    dprice_very_lowered3 = 300

    dprice_no_changes1 = 200
    dprice_no_changes2 = 300
    dprice_no_changes3 = 500
    dprice_no_changes4 = 600

    dprice_growed1 = 500
    dprice_growed2 = 600
    dprice_growed3 = 800
    dprice_growed4 = 900

    dprice_very_growed1 = 800
    dprice_very_growed2 = 900
    dprice_very_growed3 = 1000000

    sets = [
        [dprice_very_lowered1, dprice_very_lowered2, dprice_very_lowered3], # Значительно снизилась
        [dprice_no_changes1, dprice_no_changes2, dprice_no_changes3, dprice_no_changes4], # Практически не изменилась
        [dprice_growed1, dprice_growed2, dprice_growed3, dprice_growed4], # Незначительно выросла
        [dprice_very_growed1, dprice_very_growed2, dprice_very_growed3], # Значительно выросла
    ]

    @staticmethod
    def fuzzy_random(percent):
        r = random.randrange(1, 100)
        return r >= percent

    @staticmethod
    def belonging(value):
        for i in range(len(DPrice.sets)):
            if value > DPrice.sets[i][len(DPrice.sets[i]) - 1]:
                continue
            else:
                if i == 0:
                    # в зоне "значительо снизилась"
                    if value <= DPrice.dprice_very_lowered2:
                        return DPrice.VERY_LOWERED
                    else:
                        res = DPrice.fuzzy_random(round((DPrice.dprice_very_lowered3 - value) / (DPrice.dprice_very_lowered3 - DPrice.dprice_very_lowered2) * 100))
                        if res:
                            return DPrice.NO_CHANGES
                        else:
                            return DPrice.VERY_LOWERED
                    # -----------------------------
                elif i == len(DPrice.sets) - 1:
                    # в зоне "значительно выросла"
                    if value >= DPrice.dprice_very_growed2:
                        return DPrice.GROWED
                    else:
                        res = DPrice.fuzzy_random(round((DPrice.dprice_very_growed2 - value) / (DPrice.dprice_very_growed2 - DPrice.dprice_very_growed1) * 100))
                        if res:
                            return DPrice.GROWED
                        else:
                            return DPrice.VERY_GROWED
                    # ----------------------------
                else:
                    # в остальных зонах
                    if value >= DPrice.sets[i][1] and value <= DPrice.sets[i][2]:
                        return i
                    elif value < DPrice.sets[i][1]:
                        res = DPrice.fuzzy_random(round((DPrice.sets[i][1] - value) / (DPrice.sets[i][1] - DPrice.sets[i][0]) * 100))
                        if res:
                            return i - 1
                        else:
                            return i
                    else:
                        res = DPrice.fuzzy_random(round((DPrice.sets[i][3] - value) / (DPrice.sets[i][3] - DPrice.sets[i][2]) * 100))
                        if res:
                            return i + 1
                        else:
                            return i
                    # -----------------