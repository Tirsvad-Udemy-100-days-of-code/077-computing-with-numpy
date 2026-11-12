[English](Step-4-Images) · [Dansk](Step-4-Images-da) · **Bahasa Malaysia**

# Langkah 4: Imej sebagai ndarray

Imej ialah koleksi piksel, dan piksel ialah gabungan merah, hijau dan biru. Jadi imej berwarna ialah array 3 dimensi: baris, lajur dan 3 saluran. Kod: `computing_with_numpy.domain.images`.

Gambar rakun dalam kuliah datang daripada `scipy.misc.face()`, yang sudah tidak wujud. Projek ini menjana gambar yang sama saiz (768 x 1024 x 3) sebagai gantinya; lihat rekod keputusan ADR-0001 dalam repositori. `load_image(path)` membuka sebarang gambar 3 saluran milik anda sendiri.

## Jenis, shape dan resolusi

Gambar itu ialah `numpy.ndarray` berjenis `uint8` dengan shape `(768, 1024, 3)`: 3 dimensi, resolusi 1024 x 768.

![Imej ialah ndarray](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/16-image-info.png)
![Paparkan imej](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/17-image-show.png)

## Tukar kepada skala kelabu

Bahagikan dengan 255 untuk mendapatkan nilai sRGB antara 0 dan 1 (broadcasting), kemudian darabkan dengan `[0.2126, 0.7152, 0.0722]` menggunakan pendaraban matrix. Hasilnya ialah array 2 dimensi; `cmap='gray'` memberitahu Matplotlib bahawa ia hitam putih.

![Tukar imej kepada skala kelabu](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/18-grayscale.png)

## Balikkan, putar dan songsangkan

`np.flip` menterbalikkan imej skala kelabu, `np.rot90` memutar imej berwarna, dan `255 - img` menyongsangkannya (solarize).

![Balikkan imej skala kelabu](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/19-flip-gray.png)
![Putar imej berwarna](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/20-rotate.png)
![Songsangkan imej berwarna](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/21-invert.png)

## Gunakan imej anda sendiri

Buka gambar dengan Pillow dan jadikannya array. Ia memerlukan 3 saluran (PNG 4 saluran memerlukan langkah tambahan).

![Gunakan imej anda sendiri](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/22-own-image.png)

## Apa yang anda peroleh

- Gambar ialah nombor, jadi setiap alat array berfungsi padanya.
- Broadcasting dan pendaraban matrix menyelesaikan tugas sebenar: skala kelabu dalam dua baris.
- Balikkan, putar dan songsangkan ialah satu baris kod pada array.
