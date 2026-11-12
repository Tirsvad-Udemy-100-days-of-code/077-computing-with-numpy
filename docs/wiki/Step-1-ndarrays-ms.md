[English](Step-1-ndarrays) · [Dansk](Step-1-ndarrays-da) · **Bahasa Malaysia**

# Langkah 1: ndarray NumPy

ndarray ialah array n-dimensi yang homogen: setiap elemen mempunyai jenis yang sama, dan bilangan dimensi boleh satu, dua atau banyak. Kod: `computing_with_numpy.domain.ndarray_basics`.

## 1 dimensi: vektor

`create_vector()` membina `[1.1, 9.2, 8.1, 4.7]`. Nilai `shape` ialah `(4,)`, `ndim` ialah 1, dan `vector_element(my_array, 2)` membaca elemen pada indeks 2 (8.1).

![1 dimensi: vektor](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/01-vector.png)

## 2 dimensi: matrix

`create_matrix()` mempunyai 2 baris dan 4 lajur. Satu nilai memerlukan satu indeks bagi setiap axis: `array_2d[1, 2]` ialah 7. Operator `:` mengambil keseluruhan axis: `array_2d[0, :]` ialah baris pertama.

![2 dimensi: matrix](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/02-matrix.png)

## N dimensi: cabaran array misteri

Array misteri mempunyai shape `(3, 2, 4)`: tiga elemen pada axis 0, dua pada axis 1 dan empat pada axis 2. Nilai 18 berada pada `[2, 1, 3]`, vektor `[97, 0, 27, 18]` ialah `[2, 1, :]`, dan matrix `(3, 2)` bagi elemen pertama ialah `[:, :, 0]`.

![N dimensi: cabaran array misteri](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/03-mystery-array.png)

## Apa yang anda peroleh

- `shape` dan `ndim` memberitahu anda bagaimana sesuatu array dibina sebelum anda menyentuh nilainya.
- Satu indeks bagi setiap axis, `:` untuk keseluruhan axis: peraturan yang sama berfungsi dalam sebarang dimensi.
- Array homogen menjadikan NumPy pantas dan boleh diramal.
