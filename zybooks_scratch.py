#
# m1w = 33700
# m1a = 924
# m1s = 3140
#
# m2s = m1s
# m2w = 0.116 * m1w
#
# m3w = m1w - m2w
# m3a = m1a
#
# x6a = 0.137
# m6a = m3a
# temp = 26
# water_p = 10 ** (8.05573 - (1723.64 / (temp + 233.076)))
# total_p = 479
# humidity = 0.279
# x6w = humidity / (total_p / water_p)
# x6n = 1 - x6w - x6a
# m6w = m6a * (x6w / x6a)
# m6n = m6a * (x6n / x6a)
# m6 = m6a + m6w + m6n
# print("m6 =", m6)
# m5 = m6n
# print("m5 =", m5)
# m4 = m3w - m6w
# print('m4 =', m4)

r = 8.314  # J / mol*k
t = 299  # K
p = 63860  # Pa
n5 = 4600
vtp = n5 * r * t / p * 1000
print(vtp)
vstp = n5 * 22.4 / 1000 / 60
print(vstp)