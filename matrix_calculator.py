# the matrix calculator should be capable of finding the solutions to any 
# simultaneous linear equation of n equations and thus, should be able to calculate the following: 

# Functionally (SLE-wise): 
#   * determinant of a matrix
#   * cofactor of a matrix
#   * adjunct of a matrix 
#   * inverse of a matrix

#  Additionally (Matrix-wise): 
#   * the dot-product of two matrices 
#   * the cross-product of two matrices
#   * generate an identity matrix
#   * check if matrix is idempotent, involutary, singular, 
#     and square or dimension of the matrix

# -----   Matrix Sample   ----- #
matrix_sample = [[1, 2, 3], 
                 [4, 5, 6], 
                 [7, 8, 9]]

print(matrix_sample)

# -----   Utilities and Checks   ----- #
def is_square_matrix(m1, m2): 
  pass 

def can_multiply(m1, m2): 
  pass 

# -----   Basic Operations   ----- #
def add_matrices(m1, m2): 
  pass

def subtract_matrices(m1, m2): 
  pass

def multiply_matrices(m1, m2): 
  pass

# -----   Matrix Functions   ----- #
def transpose(m): 
  pass 

def cofactor(m): 
  pass

def determinant(m): 
  pass

def adjunt(m): 
  return transpose(cofactor(m))

def inverse(m): 
  return adjunt(m) / determinant(m)