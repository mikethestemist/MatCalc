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
bad_matrix_sample = [[1, 2,], 
                 [4, 5, 6], 
                 [7, 8, 9]]

# print(matrix_sample)

# -----   Utilities and Checks   ----- #
def column_count_is_uniform(m): 
  columns = set()
  for row in m: 
    columns.add(len(row))  
  if len(columns) == 1: 
    return True
  elif len(columns) != 1: 
    print(f'{m} has inconsitent column entries.')
    return False

def get_order(m): 
  if column_count_is_uniform(m): 
    m_columns = len(m[0])
    n_rows = len(m)
    return (m_columns, n_rows )

def has_same_order(m1, m2): 
  return get_order(m1) == get_order(m2)

def is_square_matrix(m): 
  rows = len(m)
  columns = set()
  for row in m: 
    columns.add(len(row))  
  if column_count_is_uniform(m) and rows == sorted(columns)[0]: 
    return True
  elif rows != sorted(columns)[0]: 
    return False

def can_multiply(m1, m2): 
  m1_row_count = len(m1[0])
  m2_column_count = len(m1)
  return m1_row_count == m2_column_count and column_count_is_uniform(m1) and column_count_is_uniform(m2)

def make_identity_matrix(square_size): 
  m = []
  for i in range(square_size): 
    row = []
    for j in range(square_size): 
      if i == j: 
        row.append(1)
      else: 
        row.append(0)
    m.append(row)
  return m

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