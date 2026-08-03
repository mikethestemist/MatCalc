import MatCalc as mc

# A * X = P
# X = inv(A) * P

A = [[2, 3], [4, 5]]
P = [[5], [9]]

X = mc.multiply(mc.inverse(A), P)
