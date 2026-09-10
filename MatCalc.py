from random import randint

# -----   Matrix Sample   ----- #
sample_matrix = [[1, 2, 3], 
                 [4, 5, 6], 
                 [7, 8, 9]]
bad_sample_matrix = [[1, 2,], 
                 [4, 5, 6], 
                 [7, 8, 9]]

# print(matrix_sample)

# -----   User Validations   ----- #
def is_valid_num(num: int | float | list) -> bool: 
  """Takes in a value or a list of values and returns a single boolean stating whether or not the value or the list of values is a valid integer or float — number."""
  if type(num) == list: 
    validity_set = set()
    for x in num:
      validity_set.add(is_valid_num(x))
    if len(validity_set) == 1 and list(validity_set)[0] == True: 
      return  True
    else: return False
  return type(num) in [int, float]


# -----   Utilities and Checks   ----- #
def is_valid_matrix(m: list[list[int | float]]) -> bool:
  """Takes a two dimensional list of numbers to represent a matrix and returns a single boolean confirming or denying that it is a valid matrix. It checks for consistent column count and validates that all entries are numbers. It also prints out the matrix and a message stating the error."""
  if m == None: 
    return False
  elif not type(m) == list:
    print(f'{m} is an invalid input.')
    return False
  else:
    columns = set()
    for row in m: 
      columns.add(len(row))  
      for i in row:
        if not is_valid_num(i): 
          print(f'{m} is contains an invalid number')
          return False
    if len(columns) == 1: 
      return True
    elif len(columns) != 1: 
      print(f'{m} has inconsitent column entries.')
      return False

def get_order(m: list[list[int | float]]) -> tuple[int, int]: 
  """It takes in a two dimensional list of numbers, verifies it's a valid matrix and returns the order as a tuple. The first value is the number of rows, the m, and the second value the number of columns or items per row, the n."""
  if is_valid_matrix(m): 
    m_rows = len(m)
    n_cols = len(m[0])
    return (m_rows, n_cols)

def has_same_order(m1: list[list[int | float]], m2: list[list[int | float]]) -> bool: 
  """Takes in two two dimensional list of numbers and returns a boolean showing whether they were of the same order — had the same number of rows and columns, or not."""
  return get_order(m1) == get_order(m2)

def is_square_matrix(m: list[list[int | float]]) -> bool: 
  """Takes in a two dimensional list of numbers and returns a boolean stating whether or not the columns of the matrix have the same count as the rows."""
  rows = len(m)
  columns = set()
  for row in m: 
    columns.add(len(row))  
  if is_valid_matrix(m) and rows == sorted(columns)[0]: 
    return True
  elif rows != sorted(columns)[0]: 
    return False

def can_multiply(m1: list[list[int | float]], m2: list[list[int | float]]) -> bool: 
  """Takes in two lists of lists and returns a boolean whether or not the column count, m, of the first matrix is the same as the row count, n of the second matrix."""
  m1_col_count = get_order(m1)[1]
  m2_row_count = get_order(m2)[0]
  return m1_col_count == m2_row_count

def generate_identity_matrix(square_size: int) -> list[list[int]]: 
  """It generates aa matrix — a two dimensional list of numbers — with its leading diagonal being 1 and all other values being zero."""
  if type(square_size) == int:
    print('Invalid whole number for the square size of the identity matrix.')
    return None
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

def gen_rand(m_row: int, n_col: int, x_range: int) -> list[list[int | float]]: 
  """"Takes in three values. The first being the number of rows you want to generate, the second being the number of columns and the third being the max value that could possibly occure. It preoccupies the matrix with random variables between zero and the max value specified."""

  # TODO: ensure that the m_row and n_col are valid integers
  # TODO: make option for a lower bound and upper bound
  # TODO: make the range able to accept a float and return floats 

  vals = [m_row, n_col, x_range]
  if not is_valid_num(vals):
    print('Invalid number as input for random matrix generation.')
    return None
  m = []
  for i in range(m_row): 
    row = []
    for j in range(n_col): 
      row.append(randint(0, x_range))    
    m.append(row)
  return m

# -----   Basic Operations   ----- #
def add_matrices(m1: list[list[int | float]], m2: list[list[int | float]])-> list[list[int | float]]: 
  """It verifies that the matrices — two dimensional list of lists — is valid and then returns a matrix having the entities at each row by column (m x n) position summed up. It works for two matrices at a time."""
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

def subtract_matrices(m1: list[list[int | float]], m2: list[list[int | float]]) -> list[list[int | float]]: 
  """It verifies that the matrices — two dimensional list of lists — is valid and then returns a matrix having the entities of the second matrix subtracted from the first at each row by column (m x n) position. It works for two matrices at a time."""
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

def multiply(m1_or_scalar: int | float | list[list[int | float]], m2: list[list[int | float]])-> list[list[int | float]]: 
  """It takes in two values. The first either being a scalar single digit, or being a two dimensional list of numbers like the second value. If the first value is a scalar, it multiplies all the entries of the other matrix with that value. If the first value were to be a matrix, it gives the sum-product for each entry moving through the rows for the first matrix and the columns of the second matrix."""

  # TODO: Debug multiply function
  if type(m1_or_scalar) in [int, float]: 
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
def transpose(m: list[list[int | float]]) -> list[list[int | float]]: 
  """It takes the rows of the matrixs and returns a new matrix with those rows as columns. It's anchor is the first entry — it takes the first row and makes it the first column while making the first entry the same."""
  if is_valid_matrix(m):
    m_new = []
    for i in range(len(m)): 
      row = []
      for j in range(len(m[i])): 
        row.append(m[j][i])
      m_new.append(row)
    return m_new

def minor(m_row: int, n_column: int, matrix: list[list[int | float]]) -> list[list[int | float]]: 
  """It takes in a zero-indexed row and column number and returns a two dimensional list of numbers excluding that row and column entirely."""
  # TODO: Do a number validation for m_row and n_column 
  # TODO: Ensure that the m_row and n_column are valid locations in the matrix 
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
  
def cofactor(m: list[list[int | float]]) -> list[list[int | float]]: 
  """It cycles through the matrix, takes the determinant of the minor of that entry and multiplies it with its respective sign, while not multiplying it with the entry itself, and returns the resulting matrix."""
  if is_square_matrix(m):
    matrix = []
    for i in range(len(m)): 
      row = []
      for j in range(len(m[i])): 
        row.append(((-1) ** (i + j)) * determinant(minor(i, j, m)))
      matrix.append(row)
    return matrix

def determinant(m: list[list[int | float]]) -> list[list[int | float]]:
  """It cycles through the matrix, takes the determinant of the minor of that entry, multiplies it with its respective sign and the entry itself, and returns the resulting matrix."""
  if is_square_matrix(m):
    if get_order(m) == (1, 1): 
      return m[0][0]
    elif get_order(m) == (2, 2): 
      return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    else: 
      result = 0
      for i in range(len(m[0])): 
        result += ((-1) ** i ) * m[0][i] * determinant(minor(0, i, m))
      return result
  else: 
    print(f"{m} isn't a square matrix, the determinant and cofactor of this matrix cannot be found.")

def adjunt(m: list[list[int | float]]) -> list[list[int | float]]: 
  """Returns the transpose of the cofactor of the accepted matrix"""
  return transpose(cofactor(m))

def inverse(m: list[list[int | float]]) -> list[list[int | float]]: 
  """Returns the product of the inverse of the determinant and the transponse of the cofactor — adjunt — of the accepted matrix"""
  return multiply(determinant(m) ** (-1), adjunt(m))

# -----   Custom Calculation Functions   ----- #
def solve_linear_system(A: list[list[int | float]], P: list[list[int | float]]) -> list[list[int | float]]: 
  """Takes in the matrix of the coefficients of the unknowns at the left-hand-side of a simultaneous linear equation as the first argument and takes in the answers to the equations as a matrix as the second argument and returns the solution to the system of linear equations.."""
  return multiply(inverse(A), P)