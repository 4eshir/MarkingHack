class Patterns:
    NONE = 0
    UP = 1
    DOWN = 2
    STABLE = 3
    UNSTABLE = 4

    TOLERANCE_PERCENT = 3

    @staticmethod
    def Tolerance(v):
        segment = []
        segment.append(v - v * (Patterns.TOLERANCE_PERCENT / 100))
        segment.append(v + v * (Patterns.TOLERANCE_PERCENT / 100))
        return segment

    @staticmethod
    def Equal(v1, v2):
        seg = Patterns.Tolerance(v1)
        return seg[0] <= v2 <= seg[1]

    @staticmethod
    def More(v1, v2):
        seg = Patterns.Tolerance(v1)
        return v2 >= seg[1] and v2 > v1

    @staticmethod
    def Under(v1, v2):
        seg = Patterns.Tolerance(v1)
        return v2 <= seg[0] and v2 < v1

    @staticmethod
    def GetType(values):
        # Для малых отрезков
        if len(values) < 2:
            return Patterns.NONE
        elif len(values) == 2:
            if Patterns.More(values[0], values[1]):
                return Patterns.DOWN
            elif Patterns.Under(values[0], values[1]):
                return Patterns.UP
            else:
                return Patterns.STABLE
        elif len(values) == 3:
            if Patterns.More(Patterns.More(values[0], values[1]), values[2]):
                return Patterns.DOWN
            elif Patterns.Under(Patterns.Under(values[0], values[1]), values[2]):
                return Patterns.UP
            elif Patterns.Equal(Patterns.Equal(values[0], values[1]), values[2]):
                return Patterns.STABLE
            else:
                return Patterns.UNSTABLE

        # ------------------
        # Для больших отрезков
        else:
            up_mistakes = len(values) // 4
            down_mistakes = len(values) // 4
            stable_mistakes = len(values) // 4
            up_sign = 1
            down_sign = 1
            stable_sign = 1
            for i in range(len(values) - 1):
                if Patterns.More(values[i], values[i + 1]):
                    if up_mistakes > 0:
                        up_mistakes -= 1
                    else:
                        up_sign = 0

                if Patterns.Under(values[i], values[i + 1]):
                    if down_mistakes > 0:
                        down_mistakes -= 1
                    else:
                        down_sign = 0

                if Patterns.Equal(values[i], values[i + 1]):
                    if up_mistakes > 0:
                        up_mistakes -= 1
                    else:
                        up_sign = 0

                    if down_mistakes > 0:
                        down_mistakes -= 1
                    else:
                        down_sign = 0

            i = 0
            while i < len(values) - 1:
                if not Patterns.Equal(values[i], values[i + 1]):
                    if stable_mistakes > 0:
                        stable_mistakes -= 1
                        i += 1
                    else:
                        stable_sign = 0
                i += 1

            if up_sign + down_sign + stable_sign != 1:
                return Patterns.UNSTABLE
            elif up_sign == 1:
                return Patterns.UP
            elif down_sign == 1:
                return Patterns.DOWN
            else:
                return Patterns.STABLE
        # --------------------