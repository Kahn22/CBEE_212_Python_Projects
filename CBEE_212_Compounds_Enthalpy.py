from scipy.optimize import fsolve


class Compound:
    """Initiates a compound class"""

    def __init__(self):
        return

    def set_sub_factors(self, a, b, c, d):
        self.sub_factor_a = a
        self.sub_factor_b = b
        self.sub_factor_c = c
        self.sub_factor_d = d

    def set_super_factors(self, a, b, c, d):
        self.super_factor_a = a
        self.super_factor_b = b
        self.super_factor_c = c
        self.super_factor_d = d

    def set_vaporization_temp(self, temp):
        self.vaporization_temp = temp

    def set_vaporization_enthalpy(self, enthalpy):
        self.vaporization_enthalpy = enthalpy

    def calc_sub_enthalpy_change(self, t1, t2):
        x = self.sub_factor_a * t1 + self.sub_factor_b * t1 ** 2 / 2 + self.sub_factor_c * t1 ** 3 / 3 + self.sub_factor_d * t1 ** 4 / 4  # kJ/mol
        y = self.sub_factor_a * t2 + self.sub_factor_b * t2 ** 2 / 2 + self.sub_factor_c * t2 ** 3 / 3 + self.sub_factor_d * t2 ** 4 / 4  # kJ/mol
        return y - x

    def calc_super_enthalpy_change(self, t1, t2):
        x = self.super_factor_a * t1 + self.super_factor_b * t1 ** 2 / 2 + self.super_factor_c * t1 ** 3 / 3 + self.super_factor_d * t1 ** 4 / 4  # kJ/mol
        y = self.super_factor_a * t2 + self.super_factor_b * t2 ** 2 / 2 + self.super_factor_c * t2 ** 3 / 3 + self.super_factor_d * t2 ** 4 / 4  # kJ/mol
        return y - x

    def calc_total_enthalpy_change(self, t1, t2, phase_change):
        """Calculates total enthalpy change in kJ/mol"""
        negative = False
        if t2 < t1:
            holder = t2
            t2 = t1
            t1 = holder
            negative = True
        if t1 < self.vaporization_temp < t2:
            phase_change = True
        if t1 < self.vaporization_temp and t2 <= self.vaporization_temp:
            path = self.calc_sub_enthalpy_change(t1, t2)
            if phase_change == True:
                path += self.vaporization_enthalpy
        if t1 > self.vaporization_temp and t2 >= self.vaporization_temp:
            path = self.calc_super_enthalpy_change(t1, t2)
            if phase_change == True:
                path += self.vaporization_enthalpy
        if t1 < self.vaporization_temp and t2 > self.vaporization_temp:
            path_1 = self.calc_sub_enthalpy_change(t1, self.vaporization_temp)
            path_2 = self.vaporization_enthalpy
            path_3 = self.calc_super_enthalpy_change(self.vaporization_temp, t2)
            path = path_1 + path_2 + path_3
        if negative == True:
            path *= -1
        return path

    def calc_heat_capacity(self, temp):
        if temp < self.vaporization_temp:
            return self.sub_factor_a + self.sub_factor_b * temp + self.sub_factor_c * temp ** 2 + self.sub_factor_d * temp ** 3
        if temp > self.vaporization_temp:
            return self.super_factor_a + self.super_factor_b * temp + self.super_factor_c * temp ** 2 + self.super_factor_d * temp ** 3

    def calc_temp_from_cp(self, cp, is_vapor_phase):
        if is_vapor_phase == True:
            a = self.super_factor_a
            b = self.super_factor_b
            c = self.super_factor_c
            d = self.super_factor_d
        if is_vapor_phase == False:
            a = self.sub_factor_a
            b = self.sub_factor_b
            c = self.sub_factor_c
            d = self.sub_factor_d

        guess = self.vaporization_temp / 2

        def solve_vpf(p):
            temp = p
            return cp - a - b * temp - c * temp ** 2 - d * temp ** 3

        temp = fsolve(solve_vpf, (guess))[0]

        while temp < -273:
            guess += 10
            temp = fsolve(solve_vpf, (guess))[0]
        if is_vapor_phase == True:
            while temp < self.vaporization_temp:
                guess += 10
                temp = fsolve(solve_vpf, (guess))[0]
        return temp

    def predict_final_vapor_temp(self, t1, change_q, moles):
        t1cp = self.super_factor_a * t1 + self.super_factor_b * t1 ** 2 / 2 + self.super_factor_c * t1 ** 3 / 3 + \
               self.super_factor_d * t1 ** 4 / 4  # C

        def solve_final_vapor_temp(p):
            t2 = p
            return self.super_factor_a * t2 + self.super_factor_b * t2 ** 2 / 2 + self.super_factor_c * t2 ** 3 / 3 + \
                   self.super_factor_d * t2 ** 4 / 4 - t1cp - change_q / moles  # C

        t2 = fsolve(solve_final_vapor_temp, self.vaporization_temp)  # C
        return t2


acetone = Compound()
acetone.set_sub_factors(1.230 * 10 ** -1, 1.860 * 10 ** -4, 0, 0)  # C
acetone.set_super_factors(7.196 * 10 ** -2, 2.010 * 10 ** -4, -1.278 * 10 ** -7, 3.476 * 10 ** -11)  # C
acetone.set_vaporization_temp(56)
acetone.set_vaporization_enthalpy(30.2)

benzene = Compound()
benzene.set_sub_factors(1.265 * 10 ** -1, 2.340 * 10 ** -4, 0, 0)
benzene.set_super_factors(7.406 * 10 ** -2, 3.295 * 10 ** -4, -2.520 * 10 ** -7, 7.757 * 10 ** -11)
benzene.set_vaporization_temp(80.1)
benzene.set_vaporization_enthalpy(30.765)

n_hexane = Compound()
n_hexane.set_sub_factors(2.163 * 10 ** -1, 0, 0, 0)
n_hexane.set_super_factors(1.374 * 10 ** -1, 4.085 * 10 ** -4, -2.392 * 10 ** -7, 5.766 * 10 ** -11)
n_hexane.set_vaporization_temp(68.74)
n_hexane.set_vaporization_enthalpy(28.85)

hydrogen_chloride = Compound()
hydrogen_chloride.set_super_factors(2.913 * 10 ** -2, -1.341 * 10 ** -6, 9.715 * 10 ** -9, -4.335 * 10 ** -12)
hydrogen_chloride.set_vaporization_temp(-85)
hydrogen_chloride.set_vaporization_enthalpy(16.36)

methanol = Compound()
methanol.set_sub_factors(7.586 * 10 ** -2, 1.683 * 10 ** -4, 0, 0)
methanol.set_super_factors(4.293 * 10 ** -2, 8.301 * 10 ** -5, -1.870 * 10 ** -8, -8.030 * 10 ** -12)
methanol.set_vaporization_temp(64.7)
methanol.set_vaporization_enthalpy(35.27)

n_pentane = Compound()
n_pentane.set_sub_factors(1.554 * 10 ** -1, 4.368 * 10 ** -4, 0, 0)
n_pentane.set_super_factors(1.148 * 10 ** -1, 3.409 * 10 ** -4, -1.899 * 10 ** -7, 4.226 * 10 ** -11)
n_pentane.set_vaporization_temp(36.07)
n_pentane.set_vaporization_enthalpy(25.77)

toluene = Compound()
toluene.set_sub_factors(1.488 * 10 ** -1, 3.240 * 10 ** -4, 0, 0)
toluene.set_super_factors(9.418 * 10 ** -2, 3.800 * 10 ** -4, -2.786 * 10 ** -7, 8.033 * 10 ** -11)
toluene.set_vaporization_temp(110.62)
toluene.set_vaporization_enthalpy(33.47)

water = Compound()
water.set_sub_factors(7.540 * 10 ** -2, 0, 0, 0)
water.set_super_factors(3.346 * 10 ** -2, 6.880 * 10 ** -6, 7.604 * 10 ** -9, -3.593 * 10 ** -12)
water.set_vaporization_temp(100)
water.set_vaporization_enthalpy(40.656)
