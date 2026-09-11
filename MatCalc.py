from random import randint, uniform

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

def get_order(m: list[list[int | float]]) -> tuple[int, int] | None: 
  """It takes in a two dimensional list of numbers, verifies it's a valid matrix and returns the order as a tuple. The first value is the number of rows, the m, and the second value the number of columns or items per row, the n. Returns None if matrix is invalid."""
  if is_valid_matrix(m): 
    m_rows = len(m)
    n_cols = len(m[0])
    return (m_rows, n_cols)
  return None

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

def generate_identity_matrix(square_size: int) -> list[list[int]] | None: 
  """It generates aa matrix — a two dimensional list of numbers — with its leading diagonal being 1 and all other values being zero. Returns None if square_size argument is invalid."""
  if not type(square_size) == int:
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

def gen_rand(m_row: int, n_col: int, low_b: int | float = 0, up_b: int | float = 10) -> list[list[int | float]] | None: 

  """Takes in two values and two more optional ones. The first two values **accept integers** specifying the number of rows and columns, respectively, the generated matrix should have. The next two optional arguments specify the lower and upper bounds, respectively, which come with default values of 0 and 10 respectively. 
  
  You may choose to omit the second or both of the optional arguments but peradventure you want to omit the first and specify the second only, you would compulsorily do so in this format: *`up_b = <number>`*. It returns None and the error message if an error occurs."""

  vals = {'m_row': m_row, 'n_col': n_col} 
  invalid_vals = {}
  for key, value in vals.items():
    if not type(value) == int:
      invalid_vals[key] = value
  if len(invalid_vals) > 0:
    print(f'Invalid whole number arguments for gen_rand(). {invalid_vals=}')
    return None
  
  if not is_valid_num([low_b, up_b]): 
    print('Invalid numbers for gen_rand. Examine the low_b and up_b arguments.')
    return None
  if low_b >= up_b: 
    print('Invalid numbers for gen_rand. Lower bound is greater than upper bound.')
    return None
  
  if type(low_b) == float or type(up_b) == float: 
    int_or_float = 'float'
  else: int_or_float = 'int'

  m = []
  for _ in range(m_row): 
    row = []
    for _ in range(n_col): 
      if int_or_float == 'float':
        row.append(round(uniform(low_b, up_b), 2))
      else: row.append(randint(low_b, up_b))
    m.append(row)
  return m

# -----   Basic Operations   ----- #
def add_matrices(m1: list[list[int | float]], m2: list[list[int | float]])-> list[list[int | float]] | None: 
  """It verifies that the matrices — two dimensional list of lists — is valid and then returns a matrix having the entities at each row by column (m x n) position summed up. It works for two matrices at a time. Returns None when an error occurs."""
  if has_same_order(m1, m2): 
    result = []
    for i in zip(m1, m2): 
      row = []
      for j in range(len(i[0])): 
        row.append(i[0][j] + i[1][j])
      result.append(row)
    return result
  else: 
    print('An error occurred in the matrix addition. Please examine', m1, 'and', m2)
    return None


def subtract_matrices(m1: list[list[int | float]], m2: list[list[int | float]]) -> list[list[int | float]] | None: 
  """It verifies that the matrices — two dimensional list of lists — is valid and then returns a matrix having the entities of the second matrix subtracted from the first at each row by column (m x n) position. It works for two matrices at a time. Returns None when an error occurs."""
  if has_same_order(m1, m2): 
    result = []
    for i in zip(m1, m2): 
      row = []
      for j in range(len(i[0])): 
        row.append(i[0][j] - i[1][j])
      result.append(row)
    return result
  else: 
    print('An error occurred in the matrix subtration. Please examine', m1, 'and', m2)
    return None

def multiply(m1_or_scalar: int | float | list[list[int | float]], m2: list[list[int | float]])-> list[list[int | float]] | None: 
  """It takes in two values. The first either being a scalar single digit, or being a two dimensional list of numbers like the second value. If the first value is a scalar, it multiplies all the entries of the other matrix with that value. 
  
  If the first value were to be a matrix, it gives the sum-product for each entry moving through the rows for the first matrix and the columns of the second matrix. Returns None when an error occurs."""

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
    else: 
      print(f'An error occurred in the scalar multiplication of {m2}. Please examine arguments.')
      return None
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
  else: 
    print(f'An error occurred in the matrix multiplication of {m1=} and {m2=}. Please examine arguments.')
    return None

# -----   Matrix Functions   ----- #
def transpose(m: list[list[int | float]]) -> list[list[int | float]] | None: 
  """It takes the rows of the matrixs and returns a new matrix with those rows as columns. It's anchor is the first entry — it takes the first row and makes it the first column while making the first entry the same."""
  if is_valid_matrix(m):
    m_new = []
    for i in range(len(m)): 
      row = []
      for j in range(len(m[i])): 
        row.append(m[j][i])
      m_new.append(row)
    return m_new
  else: 
    print(f'An error occurred when transposing {m}.')
    return None

def minor(m_row: int, n_column: int, matrix: list[list[int | float]]) -> list[list[int | float]] |None: 
  """It takes in a zero-indexed row and column number and returns a two dimensional list of numbers excluding that row and column entirely."""

  if type(m_row) != int or type(n_column) != int: 
    print(f'Invalid whole numbers for as coordinate arguments for {matrix}. Examine m_row and n_column.')
    return None
  
  if is_valid_matrix(matrix): 
    matrix_order = get_order(matrix)
    if m_row > matrix_order[0] or n_column > matrix_order[1]: 
      print(f'Invalid coordinate arguments for {matrix}. Coordinates, m_row or/and n_column is/are out of bound.')
      return None
  
    minor_matrix = []
    for i in range(len(matrix)): 
      row = []
      for j in range(len(matrix[i])): 
        if i != m_row and j != n_column:
          row.append(matrix[i][j])
      if row: 
        minor_matrix.append(row)
    return minor_matrix
  else: 
    print(f'An error occurred while trying to return the minor of matrix {matrix}.')
    return None
  
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

def determinant(m: list[list[int | float]]) -> list[list[int | float]] | None:
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
    print(f"An error occured. Either {m} isn't a square matrix, or the values of the matrix are invalid. Please examine the matrix again.")
    return None

def adjunt(m: list[list[int | float]]) -> list[list[int | float]] | None: 
  """Returns the transpose of the cofactor of the accepted matrix"""
  if is_valid_matrix(m): return transpose(cofactor(m))
  else: 
    print(f'Error occurred while finding the adjunt of {m}.')
    return None

def inverse(m: list[list[int | float]]) -> list[list[int | float]] | None: 
  """Returns the product of the inverse of the determinant and the transponse of the cofactor — adjunt — of the accepted matrix"""
  if is_valid_matrix(m): return multiply(determinant(m) ** (-1), adjunt(m))
  else: 
    print(f'Error occurred while finding the inverse of {m}.')
    return None
  

# -----   Custom Calculation Functions   ----- #
def solve_linear_system(A: list[list[int | float]], P: list[list[int | float]]) -> list[list[int | float]] | None: 
  """Takes in the matrix of the coefficients of the unknowns at the left-hand-side of a simultaneous linear equation as the first argument and takes in the answers to the equations as a matrix as the second argument and returns the solution to the system of linear equations.."""
   
  if is_valid_matrix(A) and is_valid_matrix(P): return multiply(inverse(A), P)
  else: 
    print(f'Error occurred while finding the solution to the system of linear equations using {A} and {P} as arguments.')
    return None