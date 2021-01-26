# Andrew Hudson
# Written Homework 2 Question 2
# 01 / 15 / 2021

# 2)
# A steam turbine is used to turn a generator.
# The inlet steam is at 400 kPa and 175 ∘ C and the outlet stream is saturated liquid at 100 kPa.
# If the flow rate of the steam is 100 kg/min how much shaft work is produced by the turbine in units of Watts?
# How does the answer change if we assume a heat loss from the turbine of  90,000 [kJ/min]?

from CBEE_212_Functions import *

# Setting known variables
inlet_pressure = 400  # kPa
inlet_temp = 175  # C
outlet_pressure = 100  # kPa
mfr = 100  # kg/min
mfr /= 60  # kg/s
Q = 90000  # kJ/min
Q /= 60  # kJ/s

# Solve for h1 by interpolation of data for superheated vapor.
h1 = interpolate_single_yip(150, 200, 2752.8, 2860.9, 175)  # kJ/kg

# Enthalpy of saturated liquid at 100 kPa
h2 = 417.50  # kJ/kg

# m(H + KE + PE) = Q + W; Initially, Q = 0 and KE and PE are negligible, so we get m * H = W
first_prompt = mfr * (h2 - h1)  # kJ/s
first_prompt *= 1000  # Watts, positive sign indicates the work put into the turbine.

# For the second prompt, m * H = W - 90,000 kJ/s
second_prompt = mfr * (h2 - h1) + Q  # kJ/s
second_prompt *= 1000  # Watts