[English](Step-3-Broadcasting-and-matmul) · [Dansk](Step-3-Broadcasting-and-matmul-da) · **Bahasa Malaysia**

# Langkah 3: Broadcasting dan pendaraban matrix

Kod: `computing_with_numpy.domain.linear_algebra`.

## Aritmetik vektor

Menambah dua vektor menambah elemen demi elemen: `[4, 5, 2, 7] + [2, 1, 3, 3]` ialah `[6, 6, 5, 10]`; pendaraban memberikan `[8, 5, 6, 21]`.

![Algebra linear dengan vektor](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/12-vector-math.png)

## List berbanding array

Menambah dua list Python akan menyambungkannya, dan mendarab dua list menyebabkan ralat. Array NumPy melakukan apa yang dijangkakan oleh ahli matematik.

![List berbanding array](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/13-lists-vs-arrays.png)

## Broadcasting skalar

Untuk mendarab setiap nilai dengan 2, NumPy meregangkan nombor tunggal itu (skalar) kepada shape array. Inilah broadcasting, dan ia berfungsi dalam 1, 2 atau lebih dimensi.

![Broadcasting skalar](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/14-broadcasting.png)

## Cabaran pendaraban matrix

`matrix_product(a1, b1)` mendarab matrix 4x2 dengan matrix 2x3 menggunakan `@`; hasilnya 4x3. Secara manual: c12 = 1*1 + 3*8 = 25 dan c33 = 6*3 + 2*5 = 28.

![Cabaran pendaraban matrix](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/15-matrix-product.png)

## Apa yang anda peroleh

- Aritmetik pada keseluruhan array menggantikan gelung.
- Broadcasting membolehkan skalar dan array berfungsi bersama tanpa menyalin skalar itu.
- `@` (atau `np.matmul`) mengikut peraturan algebra linear: saiz dalaman mesti sepadan.
