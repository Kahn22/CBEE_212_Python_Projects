# Andrew Hudson
# Written Homework 2 Question 1
# 01/ 15/ 2021

# 1)
# Steam is produced in a boiler using liquid water as the feed.  The boiler operates at 100 kPa.
# The temperature of the inlet water is 40C .
# If the outlet steam has a temperature of 130C,
# how much heat does it take to produce 3 kg/s of the steam?

from CBEE_212_Functions import *

inlet_temp = 40  # C
outlet_temp = 130  # C
boiler_pressure = 100  # kPa
mfr = 3  # kg/s
vaporization_temp = 99.61  # C

# Enthalpy path:
# path_1 = heat to saturated
# path_2 = vaporization enthalpy
# path_3 = heat to superheated

# path_1 = find_enthalpy_change(7.540 * 10**-2, 0, 0, 0, inlet_temp, vaporization_temp)
path_1 = 417.50 - 167.62
path_2 = 2674.9 - 417.50
path_3_end = interpolate_single_yip(100, 150, 2675.8, 2776.6, 130)
path_3 = path_3_end - 2674.9

enthalpy_change = path_1 + path_2 + path_3

q = enthalpy_change * mfr  # kJ/s

print(q)