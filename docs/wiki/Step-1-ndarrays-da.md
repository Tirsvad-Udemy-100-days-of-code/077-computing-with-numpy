[English](Step-1-ndarrays) · **Dansk** · [Bahasa Malaysia](Step-1-ndarrays-ms)

# Trin 1: NumPys ndarray

Ndarray'et er et homogent, n-dimensionalt array: alle elementer har samme type, og antallet af dimensioner kan være én, to eller mange. Kode: `computing_with_numpy.domain.ndarray_basics`.

## 1 dimension: en vektor

`create_vector()` bygger `[1.1, 9.2, 8.1, 4.7]`. Dens `shape` er `(4,)`, dens `ndim` er 1, og `vector_element(my_array, 2)` læser elementet med indeks 2 (8.1).

![1 dimension: en vektor](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/01-vector.png)

## 2 dimensioner: en matrix

`create_matrix()` har 2 rækker og 4 kolonner. En værdi kræver ét indeks pr. akse: `array_2d[1, 2]` er 7. Operatoren `:` tager en hel akse: `array_2d[0, :]` er den første række.

![2 dimensioner: en matrix](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/02-matrix.png)

## N dimensioner: udfordringen med det mystiske array

Det mystiske array har shape `(3, 2, 4)`: tre elementer på akse 0, to på akse 1 og fire på akse 2. Værdien 18 står på `[2, 1, 3]`, vektoren `[97, 0, 27, 18]` er `[2, 1, :]`, og `(3, 2)`-matrixen af første elementer er `[:, :, 0]`.

![N dimensioner: udfordringen med det mystiske array](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/03-mystery-array.png)

## Det får du ud af det

- `shape` og `ndim` fortæller dig, hvordan et array er bygget, før du rører ved dets værdier.
- Ét indeks pr. akse, `:` for en hel akse: den samme regel virker i enhver dimension.
- Homogene arrays er det, der gør NumPy hurtigt og forudsigeligt.
