[English](Step-2-Generating-ndarrays) · [Dansk](Step-2-Generating-ndarrays-da) · **Bahasa Malaysia**

# Langkah 2: Menjana dan memanipulasi ndarray

Lapan cabaran kecil menunjukkan fungsi yang paling kerap anda temui. Kod: `computing_with_numpy.domain.generating`.

## Cabaran 1: arange

`create_range_vector()` ialah `np.arange(10, 30)`: nilai 10 hingga 29.

![Cabaran 1: arange](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/04-arange.png)

## Cabaran 2: slicing

`last_three`, `fourth_to_sixth`, `all_except_first_twelve` dan `every_second` ialah `a[-3:]`, `a[3:6]`, `a[12:]` dan `a[::2]`.

![Cabaran 2: slicing](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/05-slicing.png)

## Cabaran 3: pembalikan

`reverse_array` menggunakan `a[::-1]`, `reverse_array_with_flip` menggunakan `np.flip(a)`; hasilnya sama.

![Cabaran 3: pembalikan](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/06-reverse.png)

## Cabaran 4: indeks bukan sifar

`nonzero_indices` mengembalikan tuple array indeks: bagi `[6, 0, 9, 0, 0, 5, 0]` indeksnya ialah 0, 2 dan 5.

![Cabaran 4: indeks bukan sifar](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/07-nonzero.png)

## Cabaran 5: nombor rawak

`random_cube` memberikan array 3x3x3 yang berisi nombor rawak; seed menjadikannya boleh diulang.

![Cabaran 5: rawak](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/08-random.png)

## Cabaran 6: linspace

`linspace_x` ialah `np.linspace(0, 100, num=9)`: sembilan nilai berjarak sama, kedua-dua hujung disertakan.

![Cabaran 6: linspace x](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/09-linspace-x.png)

## Cabaran 7: linspace dan carta garis

`linspace_y` ialah `np.linspace(-3, 3, num=9)`. Kegunaan biasa `linspace` ialah menjana titik untuk sesuatu carta.

![Cabaran 7: linspace y dan carta garis](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/10-linspace-plot.png)

## Cabaran 8: imej hingar

`noise_image` ialah array 128x128x3 yang berisi nombor rawak; `imshow` membaca axis terakhir sebagai merah, hijau dan biru.

![Cabaran 8: imej hingar](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/11-noise-image.png)

## Apa yang anda peroleh

- Penjana siap sedia (`arange`, `linspace`, `random`) dan bukannya menaip nilai satu persatu.
- Slicing dengan start, stop dan step, serta pembalikan tanpa gelung.
- Idea bahawa array nombor boleh menjadi gambar.
