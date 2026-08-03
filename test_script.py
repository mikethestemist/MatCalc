import MatCalc as mc

# A * X = P
# X = inv(A) * P

A = [[2, 3], [4, 5]]
P = [[5], [9]]

print(mc.determinant(A))
print(mc.cofactor(A))
print(mc.transpose(mc.cofactor(A)))

print('-' * 40)

print(mc.adjunt(A))
print(mc.multiply(1/mc.determinant(A), mc.adjunt(A)))
print(mc.inverse(A))

print('-' * 40)

print(mc.multiply(mc.inverse(A), P))
print(mc.solve_linear_system(A, P))

print('-' * 40)

print(mc.sample_matrix, mc.generate_identity_matrix(mc.get_order(mc.sample_matrix)[0]))
print(mc.multiply(mc.sample_matrix, mc.generate_identity_matrix(mc.get_order(mc.sample_matrix)[0])))

# X = mc.multiply(mc.inverse(A), P)
# print(X)
