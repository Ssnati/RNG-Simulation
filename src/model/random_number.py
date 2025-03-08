import math, random
class LCG:
    def __init__(self, a, x0, m, c, min_val, max_val):
        self.a = a
        self.x0 = x0
        self.m = m
        self.c = c
        self.min = min_val
        self.max = max_val
        self.xi_list = []
        self.ri_list = []
        self.ni_list = []

    def calculate_seed(self, i):
        for _ in range(i):
            if not self.xi_list:
                xi = ((self.a * self.x0) + self.c) % self.m
            else:
                xi = (self.a * self.xi_list[-1] + self.c) % self.m
            
            self.xi_list.append(xi)
            self.calculate_ri(xi)

    def print_xi(self):
        for index, (xi, ri, ni) in enumerate(zip(self.xi_list, self.ri_list, self.ni_list), start=1):
            print(f"{ri}")

    def calculate_ri(self, xi):
        ri = xi / (self.m)
        self.calculate_ni(ri)
        self.ri_list.append(ri)

    def calculate_ni(self, ri):
        ni = self.min + ((self.max - self.min) * ri)
        self.ni_list.append(ni)

"""
if __name__ == "__main__":
    alg = LCG(5, 7, 16, 3, 4, 19)
    alg.calculate_seed(100)
    alg.print_xi() 
    
if __name__ == "__main__":
    cm = MiddleSquare(2573, 3)
    cm.print_list()    

if __name__ == "__main__":
    alg = MLCG(5, 7, 16, 4, 19)
    alg.calculate_seed(100)
    alg.print_xi()
if __name__ == "__main__":
    exp_gen = ExponentialGenerator(1.5)
    exp_gen.generate(100)
    exp_gen.print_values()

if __name__ == "__main__":
    pm = ProductoMedio(5015, 5734, 4)
    pm.print_list()
"""


class MiddleSquare:
    def __init__(self, number, digits):
        self.list = []
        self.number = number
        self.digits = digits
        self.calculate()

    def calculate(self):
        for _ in range(20):
            if not self.list:
                self.list.append(self.take_central_digits(self.number))
            else:
                self.list.append(self.take_central_digits(self.list[-1]))

    def take_central_digits(self, number):
        n = number * number
        str_n = str(n)
        digits_to_del = len(str_n) - self.digits
        num_to_del = digits_to_del // 2
        fin = num_to_del + self.digits
        return int(str_n[num_to_del:fin])

    def print_list(self):
        for num in self.list:
            print(num)



class MLCG:
    def __init__(self, a, x0, m, min_val, max_val):
        self.a = a
        self.x0 = x0
        self.m = m
        self.min = min_val
        self.max = max_val
        self.xi_list = []
        self.ri_list = []
        self.ni_list = []

    def calculate_seed(self, i):
        for _ in range(i):
            if not self.xi_list:
                xi = (self.a * self.x0) % self.m
            else:
                xi = (self.a * self.xi_list[-1]) % self.m
            
            self.xi_list.append(xi)
            self.calculate_ri(xi)

    def print_xi(self):
        for index, (xi, ri, ni) in enumerate(zip(self.xi_list, self.ri_list, self.ni_list), start=1):
            print(f"{index}:  {xi}, {ri}, {ni}")

    def calculate_ri(self, xi):
        ri = xi / (self.m)
        self.calculate_ni(ri)
        self.ri_list.append(ri)

    def calculate_ni(self, ri):
        ni = self.min + ((self.max - self.min) * ri)
        self.ni_list.append(ni)


class ExponentialGenerator:
    def __init__(self, lambda_val):
        self.lambda_val = lambda_val
        self.exponential_list = []
    
    def generate(self, n):
        for _ in range(0, n):
            self.exponential_list.append((-math.log(1 - random.random()) / self.lambda_val))
            #self.exponential_list.append(int((-math.log(1 - random.random()) / self.lambda_val)*1000))
    
    def print_values(self):
        for index, value in enumerate(self.exponential_list, start=1):
            print(f"{index}: {value}")


class ProductoMedio:
    def __init__(self, number1, number2, digits):
        self.list = []
        self.number1 = number1
        self.number2 = number2
        self.digits = digits
        self.calculate()
    
    def calculate(self):
        temp = 0
        for _ in range(20):
            temp = self.take_central_digits(self.number1 * self.number2)
            self.list.append(temp)
            self.number1 = self.number2
            self.number2 = temp
    
    def take_central_digits(self, number):
        str_n = str(number).zfill(self.digits * 2) 
        digitstodel = len(str_n) - self.digits
        numtodel = digitstodel // 2
        fin = numtodel + self.digits
        return int(str_n[numtodel:fin])
    
    def print_list(self):
        for value in self.list:
            print(value)

