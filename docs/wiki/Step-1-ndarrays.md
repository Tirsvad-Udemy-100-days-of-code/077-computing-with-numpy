**English** · [Dansk](Step-1-ndarrays-da) · [Bahasa Malaysia](Step-1-ndarrays-ms)

# Step 1: NumPy's ndarray

The ndarray is a homogeneous, n-dimensional array: every element has the same type, and the number of dimensions can be one, two or many. Code: `computing_with_numpy.domain.ndarray_basics`.

## 1 dimension: a vector

`create_vector()` builds `[1.1, 9.2, 8.1, 4.7]`. Its `shape` is `(4,)`, its `ndim` is 1, and `vector_element(my_array, 2)` reads the element at index 2 (8.1).

![1 dimension: a vector](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/01-vector.png)

## 2 dimensions: a matrix

`create_matrix()` has 2 rows and 4 columns. A value needs one index per axis: `array_2d[1, 2]` is 7. The `:` operator takes a whole axis: `array_2d[0, :]` is the first row.

![2 dimensions: a matrix](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/02-matrix.png)

## N dimensions: the mystery array challenge

The mystery array has shape `(3, 2, 4)`: three elements on axis 0, two on axis 1 and four on axis 2. The value 18 is at `[2, 1, 3]`, the vector `[97, 0, 27, 18]` is `[2, 1, :]`, and the `(3, 2)` matrix of first elements is `[:, :, 0]`.

![N dimensions: the mystery array challenge](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/03-mystery-array.png)

## What you gain

- `shape` and `ndim` tell you how an array is built before you touch its values.
- One index per axis, `:` for a whole axis: the same rule works in any dimension.
- Homogeneous arrays are what makes NumPy fast and predictable.
