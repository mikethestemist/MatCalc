# MatCalc

This is a module built to perform simple operations on matrices. It is to be used in Python to make matrix related operations simpler and easier. It would be a personal study and clone of the fundamental features of MATLAB&copy; and was thought to be applied to complex problems like the product with the eigensen-vectors for STEM, specifically for Civil Engineering Structural Analysis.

This was made as a practice project during the holidays of my first-year semester break in my study of civil engineering in the university. It was an attempt to practice programming in application to engineering or mathematics.

The matrix calculator should be capable of finding the solutions to any imultaneous linear equation of n equations and thus, should be able to calculate the following:

Functionally (SLE-wise):

- determinant of a matrix
- cofactor of a matrix
- adjunct of a matrix
- inverse of a matrix

Additionally (Matrix-wise):

- the dot-product of two matrices
- the cross-product of two matrices
- generate an identity matrix
- check if matrix is idempotent, involutary, singular, and square or dimension of the matrix

## Usage

This script was intended to be used as a library or module in another file by being imported and invoked like done in the following:

```
simultaneous_equation_solver.py

import matrix_calculator as mc

# A * X = P
# X = inv(A) * P

A = [[2, 3], [4, 5]]
P = [[5], [9]]

X = mc.multiply(mc.inverse(A), P)
```
