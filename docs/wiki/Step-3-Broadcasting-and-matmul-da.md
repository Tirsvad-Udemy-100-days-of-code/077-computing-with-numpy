[English](Step-3-Broadcasting-and-matmul) · **Dansk** · [Bahasa Malaysia](Step-3-Broadcasting-and-matmul-ms)

# Trin 3: Broadcasting og matrixmultiplikation

Kode: `computing_with_numpy.domain.linear_algebra`.

## Vektoraritmetik

Lægger man to vektorer sammen, lægges element for element sammen: `[4, 5, 2, 7] + [2, 1, 3, 3]` er `[6, 6, 5, 10]`; multiplikation giver `[8, 5, 6, 21]`.

![Lineær algebra med vektorer](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/12-vector-math.png)

## Lister mod arrays

Lægger man to Python-lister sammen, sættes de efter hinanden, og at multiplicere to lister er en fejl. NumPy-arrays gør, hvad en matematiker forventer.

![Lister mod arrays](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/13-lists-vs-arrays.png)

## Broadcasting af en skalar

For at gange hver værdi med 2 strækker NumPy det enkelte tal (skalaren) ud til arrayets shape. Det er broadcasting, og det virker i 1, 2 eller flere dimensioner.

![Broadcasting af en skalar](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/14-broadcasting.png)

## Udfordring med matrixmultiplikation

`matrix_product(a1, b1)` multiplicerer en 4x2-matrix med en 2x3-matrix med `@`; resultatet er 4x3. I hånden: c12 = 1*1 + 3*8 = 25 og c33 = 6*3 + 2*5 = 28.

![Udfordring med matrixmultiplikation](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/15-matrix-product.png)

## Det får du ud af det

- Aritmetik på hele arrays erstatter løkker.
- Broadcasting lader en skalar og et array arbejde sammen uden at kopiere skalaren.
- `@` (eller `np.matmul`) følger den lineære algebras regler: de indre størrelser skal passe sammen.
