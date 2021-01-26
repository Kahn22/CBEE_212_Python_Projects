# Andrew Hudson
# Written Homework 2 Question 3
# 01 / 15 / 2021

# 3)
# A sealed container contains both vapor and liquid water in equilibrium at 150 kPa .
# If the average internal energy of all the water in the container is 1,900 [kJ/kg],
# what fraction of the total mass is in the vapor phase?
# (Hint: Combine a material balance and an energy balance equation.  Assume a basis for the total mass of water.)

from scipy.optimize import fsolve

average_u = 1900
sat_water_u = 466.97
sat_vapor_u = 2519.2


def calc_fraction_vapor(p):
    y = p
    return (y * sat_vapor_u) + (1 - y) * sat_water_u - average_u


y = fsolve(calc_fraction_vapor, 0.5)[0]
x = 1 - y