class Calculation():
    
    def __init__(self, x):
        self.x = x
    def function_1(self):
        try:
            if self.x <= 2.099 or self.x >= 50.023:
                 return  self.x ** 4 * 2.226 + self.x ** 3 * 2.196 - self.x ** 2 * 7.083 + self.x * 3.724
        except TypeError:
            return "None"

    def function_2(self):
        try:
            if self.x <= 2.099 or self.x >= 50.023:
                return self.x ** 3 * 4.729 - self.x ** 2 * 2.429 + self.x * 2.897
        except TypeError:
            return "None"

    def function_3(self):
        try:
            if self.x <= 2.099 or self.x >= 50.023:
                return self.x ** 2 * 2.022 + self.x * 4.5627 
        except TypeError:
            return "None"

    def function_4(self):
        try:
            if self.x <= 2.099 or self.x >= 50.023:
                return self.x * 7.012
        except TypeError:
            return "None"

if __name__ == '__main__':
    try:
        x = float(input('Введіть число: '))
        Functions = Calculation(x)
        print('Результат 1 обрахування:',Functions.function_1())
        print('Результат 2 обрахування:',Functions.function_2())
        print('Результат 3 обрахування:',Functions.function_3())
        print('Результат 4 обрахування:',Functions.function_4())
    except:
        print("Введені некоректні дані!!!!!")
    
