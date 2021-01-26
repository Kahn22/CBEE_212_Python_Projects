import math

pipe_id = 8 # cm
pipe_ir = 4 # cm
pipe_area = math.pi * pipe_ir**2 / 100 / 100
pipe_vfr = 25 #L / min
pipe_vfr = pipe_vfr * 1/60 * 1/1000 # m**3 / second
tank_area = 10 # m**2
tank_drop = pipe_vfr / 10 # Rate at which top of tank lowers
pipe_v = pipe_vfr / pipe_area
density_water = 0.0010018 + ((0.0010078 - 0.0010018) / (40 - 20)) * (25-20) # **3 / kg
pipe_mfr = pipe_vfr /density_water # kg / s
work = (pipe_v ** 2) / 2 + (9.8 * -12)
work = work * pipe_mfr


print(pipe_area)
print(pipe_vfr)
print(tank_drop)
print(pipe_v)
print(density_water)
print(pipe_mfr)
print(work)