import math
import random_number
import statistics as st
from scipy.stats import chi2

class ChiSquare:

    def __init__(self, number_list):
        self.number_list = number_list
        self.intervals_number = int(math.sqrt(len(number_list)))
        self.min_value = min(number_list)
        self.max_value = max(number_list)
        self.range_value = (self.max_value - self.min_value)/self.intervals_number
        self.intervals = {}
        self.squ_chi = 0
        self.squ_chi_critic = chi2.ppf(0.95, self.intervals_number - 1)

    def create_intervals(self):
        expected_freq = len(self.number_list) / self.intervals_number
        for i in range(self.intervals_number):
            min_value = self.min_value + i * self.range_value if i > 0 else self.min_value
            max_value = min_value + self.range_value
            self.intervals[(min_value, max_value)] = {"freq_o": 0, "freq_e": expected_freq, "square_chi": 0}
    
    def calculate_frequence(self):
        for number in self.number_list:
            for (min,max) in self.intervals:
                if min <= number < max or (max == self.max_value and number == max):
                    self.intervals[(min, max)]["freq_o"] += 1
                    break

    def calculate_squ_chi(self):
        for freqs in self.intervals.values():
            freqs["square_chi"] = pow(freqs["freq_o"] - freqs["freq_e"], 2)/freqs["freq_e"]
            self.squ_chi += freqs["square_chi"]

    def show_intervals(self):
        for interval, frequency in self.intervals.items():
            print(f"Intervalo {interval}: {frequency}")
        print(f"{self.squ_chi}    critico {self.squ_chi_critic}"  )

if __name__ == "__main__":
    alg = random_number.LCG(5, 7, 991, 3, 4, 19)
    alg.calculate_seed(30)
    alg.print_xi()
    pm = ChiSquare(alg.ri_list)
    pm.create_intervals()
    pm.calculate_frequence()
    pm.calculate_squ_chi()
    pm.show_intervals()

class MiddleProof:
    def __init__(self, number_list):
        self.number_list = number_list
        self.average = 0
        self.inf_lim = 0
        self.sup_lim = 0
        self.variance = 0

    def calculate_average(self):
        self.average = sum(self.number_list) / len(self.number_list)

    def calculate_limits(self):
        temp = 1.96 / math.sqrt(12 * len(self.number_list))
        self.inf_lim = 0.5 - temp
        self.sup_lim = 0.5 + temp

    def calculate_variance(self):
        self.variance = st.variance(self.number_list)

    def calculate_proof(self):
        self.calculate_average()
        self.calculate_limits()
        self.calculate_variance()
        if self.inf_lim <= self.average <= self.sup_lim:
            print("Como el valor promedio se encuentra entre los límites superior e inferior, "
                  "que son los límites de aceptación, se concluye que el método ha pasado la prueba de medias.")
        else:
            print("El método NO ha pasado la prueba de medias.")

        print(f"inf: {self.inf_lim}  prom: {self.average}  sup: {self.sup_lim}  var: {self.variance}")


"""
if __name__ == "__main__":
    import random_number

    alg = random_number.LCG(5, 7, 991, 3, 4, 19)
    alg.calculate_seed(30)
    alg.print_xi()
    
    pm = MiddleProof(alg.ri_list)
    pm.calculate_proof()
"""
class KS:

    def __init__(self, number_list):
        self.number_list = number_list
        self.intervals_number = int(math.sqrt(len(number_list)))
        self.min_value = min(number_list)
        self.max_value = max(number_list)
        self.range_value = (self.max_value - self.min_value)/self.intervals_number
        self.intervals = {}
        self.dm_calculated = 0
        self.dm_critic = 1.36/(math.sqrt(len(self.number_list)))

    def create_intervals(self):
        expected_freq = len(self.number_list) / self.intervals_number
        for i in range(self.intervals_number):
            min_value = self.min_value + i * self.range_value if i > 0 else self.min_value
            max_value = min_value + self.range_value
            self.intervals[(min_value, max_value)] = {"freq_o": 0, "freq_o_a": 0, "prob_o_a": 0,"freq_e_a": expected_freq*(i + 1), "prob_e_a":(expected_freq*(i +1))/len(self.number_list), "abs_diff": 0}
    
    def calculate_frequence_obtained(self):
        for number in self.number_list:
            for (min,max) in self.intervals:
                if min <= number < max or (max == self.max_value and number == max):
                    self.intervals[(min, max)]["freq_o"] += 1
                    break
    

    def calculate_frequence_obtained_acumulated(self):
        size_list = len(self.number_list)
        temp = 0
        for frequency in self.intervals.values():
            frequency["freq_o_a"] += frequency["freq_o"] + temp
            temp += frequency["freq_o"]
            frequency["prob_o_a"] = frequency["freq_o_a"] / size_list

    def calculate_dm(self):
        for frequency in self.intervals.values():
            frequency["abs_diff"] = abs(frequency["prob_o_a"] - frequency["prob_e_a"])
            if frequency["abs_diff"] >= self.dm_calculated:
                self.dm_calculated = frequency["abs_diff"]
        self.calculate_proof()



    def calculate_proof(self):
        if self.dm_calculated < self.dm_critic:
            print(f"La lista de números aleatorios sigue una distribución uniforme (DM = {self.dm_calculated:.6f}, DM crítico = {self.dm_critic:.6f})")
        else:
            print(f"La lista de números aleatorios NO sigue una distribución uniforme (DM = {self.dm_calculated:.6f}, DM crítico = {self.dm_critic:.6f})")

    def show_intervals(self):
        for interval, frequency in self.intervals.items():
            print(f"Intervalo {interval}: {frequency}")

"""
if __name__ == "__main__":
    alg = random_number.LCG(5, 7, 991, 3, 4, 19)
    alg.calculate_seed(60)
    alg.print_xi()
    pm = KS(alg.ri_list)
    pm.create_intervals()
    pm.calculate_frequence_obtained()
    pm.calculate_frequence_obtained_acumulated()
    pm.calculate_dm()
    pm.show_intervals()

"""
    