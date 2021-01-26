def interpolate_single_yip(x1, x2, y1, y2, xip):
    return y1 + ((y2 - y1) / (x2 - x1)) * (xip - x1)


def find_enthalpy_change(a, b, c, d, t1, t2):
    x = a * t1 + b * t1**2 / 2 + c * t1**3 / 3 + d * t1**4 / 4  # kJ/mol
    y = a * t2 + b * t2**2 / 2 + c * t2**3 / 3 + d * t2**4 / 4  # kJ/mol
    return y - x
