import matrix_calculator as mc 

mc.generate_identity_matrix(4)

import matrix_calculator as mc

# A * X = P
# X = inv(A) * P

A = [[2, 3], [4, 5]]
P = [[5], [9]]

X = mc.multiply(mc.inverse(A), P)
