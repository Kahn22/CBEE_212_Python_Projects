# Andrew Hudson
# CBEE 212 Written HW 3
# A chemical polishing process requires acetone vapor at T = 95 [C].
# The inlet stream to the vaporization unit is at T = 30 [C].
# The entire process occurs at P = 1 atm.
# If the process requires 3 [kg/hr] of acetone vapor,
# find the heat required to generate the vapor, as well as the flow rate of saturated steam required to supply the heat.
# Assume that the inlet steam is saturated at P = 1 atm and the outlet is a liquid/vapor mixture at
# P = 1 atm with 80% of the mass in the liquid phase.

from CBEE_212_Compounds_Enthalpy import *
from scipy.optimize import fsolve

# Entire process occurs at P = 1 atm
pressure = 1  # atm

# Stream 1: Acetone
stream_1_temp = 30  # C
m1a = 3  # kg/hr acetone
acetone_enth_change = acetone.calc_total_enthalpy_change(stream_1_temp, 95, True)  # kJ/mol
acetone_molar_mass = 58.08  # g/mol
acetone_molar_mass /= 1000  # kg/mol
stream_1_molar_flow = m1a / acetone_molar_mass  # mol/hr
enthalpy_needed = acetone_enth_change * stream_1_molar_flow  # kJ/hr
print('kilowatts = ', enthalpy_needed)
print('total paths = ', acetone_enth_change, 'kj/mol')
# Stream 2: Steam
print('path 1 = ', acetone.calc_sub_enthalpy_change(stream_1_temp, acetone.vaporization_temp))

# Now divide water by the enthalpy needed kJ/hr by vaporization enthalpy kJ/mol
steam_condensed = enthalpy_needed / water.vaporization_enthalpy  # mol/hr
total_steam_moles = steam_condensed * (100/80)  # mol/hr
water_molar_mass = 18.016  # g/mol
water_molar_mass /= 1000  # kg/mol
total_steam = water_molar_mass * total_steam_moles  # kg/hr
print('total steam=', total_steam)

print(2256.5 * 18.016 / 1000)