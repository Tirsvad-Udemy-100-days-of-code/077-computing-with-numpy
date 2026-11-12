**English** · [Dansk](Step-3-Broadcasting-and-matmul-da) · [Bahasa Malaysia](Step-3-Broadcasting-and-matmul-ms)

# Step 3: Broadcasting and matrix multiplication

Code: `computing_with_numpy.domain.linear_algebra`.

## Vector arithmetic

Adding two vectors adds element by element: `[4, 5, 2, 7] + [2, 1, 3, 3]` is `[6, 6, 5, 10]`; multiplying gives `[8, 5, 6, 21]`.

![Linear algebra with vectors](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/12-vector-math.png)

## Lists versus arrays

Adding two Python lists concatenates them, and multiplying two lists is an error. NumPy arrays do what a mathematician expects.

![Lists versus arrays](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/13-lists-vs-arrays.png)

## Broadcasting a scalar

To multiply every value by 2, NumPy stretches the single number (the scalar) to the shape of the array. This is broadcasting, and it works in 1, 2 or more dimensions.

![Broadcasting a scalar](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/14-broadcasting.png)

## Matrix multiplication challenge

`matrix_product(a1, b1)` multiplies a 4x2 matrix by a 2x3 matrix with `@`; the result is 4x3. By hand: c12 = 1*1 + 3*8 = 25 and c33 = 6*3 + 2*5 = 28.

![Matrix multiplication challenge](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/15-matrix-product.png)

## What you gain

- Whole-array arithmetic replaces loops.
- Broadcasting lets a scalar and an array work together without copying the scalar.
- `@` (or `np.matmul`) follows the rules of linear algebra: the inner sizes must match.
