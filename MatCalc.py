# -----   Matrix Sample   ----- #
sample_matrix = [[1, 2, 3], 
                 [4, 5, 6], 
                 [7, 8, 9]]
bad_sample_matrix = [[1, 2,], 
                 [4, 5, 6], 
                 [7, 8, 9]]

# print(matrix_sample)

# -----   Utilities and Checks   ----- #
def is_valid_matrix(m): 
  columns = set()
  for row in m: 
    columns.add(len(row))  
  if len(columns) == 1: 
    return True
  elif len(columns) != 1: 
    print(f'{m} has inconsitent column entries.')
    return False

def get_order(m): 
  if is_valid_matrix(m): 
    """m: rows, n: columns / entries per row"""
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
  if is_valid_matrix(m) and rows == sorted(columns)[0]: 
    return True
  elif rows != sorted(columns)[0]: 
    return False

def can_multiply(m1, m2): 
  m1_count = get_order(m1)
  m2_count = get_order(m2)
  return (m1_count[0] == m2_count[1] and m1_count[1] == m2_count[0] and 
          is_valid_matrix(m1) and is_valid_matrix(m2))

def generate_identity_matrix(square_size): 
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
  if has_same_order(m1, m2): 
    result = []
    for i in zip(m1, m2): 
      row = []
      for j in range(len(i[0])): 
        row.append(i[0][j] + i[1][j])
      result.append(row)
    return result
  else: 
    print(m1, 'and', m2, 'do not have the same order.')

def subtract_matrices(m1, m2): 
  if has_same_order(m1, m2): 
    result = []
    for i in zip(m1, m2): 
      row = []
      for j in range(len(i[0])): 
        row.append(i[0][j] - i[1][j])
      result.append(row)
    return result
  else: 
    print(m1, 'and', m2, 'do not have the same order.')

def multiply(m1_or_scalar, m2): 
  if type(m1_or_scalar) == int: 
    # TODO: add functionality for scaler multiplication 
    if is_valid_matrix(m2): 
      s = m1_or_scalar
      m = m2
      result = []
      for i in range(len(m)): 
        row = []
        for j in range(len(m[i])): 
          row.append(s * m[i][j])
        result.append(row)  
      return result
  elif can_multiply(m1_or_scalar, m2): 
    m1 = m1_or_scalar
    result = []
    for i in range(len(m1)): 
      row = []
      for j in range(len(m2[0])):
        total = 0
        for k in range(len(m1[0])):
          total += m1[i][k] * m2[k][j]
        row.append(total)
      result.append(row)
    return result
# print(multiply_matrices(matrix_sample, matrix_sample))
# print(matrix_sample, generate_identity_matrix(3))
# print(multiply_matrices(matrix_sample, [[j * 3 for j in i] for i in generate_identity_matrix(3)]))

# -----   Matrix Functions   ----- #
def transpose(m): 
  if is_valid_matrix(m):
    m_new = []
    for i in range(len(m)): 
      row = []
      for j in range(len(m[i])): 
        row.append(m[j][i])
      m_new.append(row)
    return m_new

def minor(m_row, n_column, matrix): 
  if is_valid_matrix(matrix): 
    minor_matrix = []
    for i in range(len(matrix)): 
      row = []
      for j in range(len(matrix[i])): 
        if i != m_row and j != n_column:
          row.append(matrix[i][j])
      if row: 
        minor_matrix.append(row)
    return minor_matrix
  
def cofactor(m): 
  pass

def determinant(m): 
  pass

def adjunt(m): 
  return transpose(cofactor(m))

def inverse(m): 
  return adjunt(m) / determinant(m)