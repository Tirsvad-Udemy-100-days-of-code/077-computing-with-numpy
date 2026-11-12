[English](Step-2-Generating-ndarrays) · **Dansk** · [Bahasa Malaysia](Step-2-Generating-ndarrays-ms)

# Trin 2: Generering og manipulation af ndarrays

Otte små udfordringer viser de funktioner, du oftest møder. Kode: `computing_with_numpy.domain.generating`.

## Udfordring 1: arange

`create_range_vector()` er `np.arange(10, 30)`: værdierne 10 til 29.

![Udfordring 1: arange](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/04-arange.png)

## Udfordring 2: slicing

`last_three`, `fourth_to_sixth`, `all_except_first_twelve` og `every_second` er `a[-3:]`, `a[3:6]`, `a[12:]` og `a[::2]`.

![Udfordring 2: slicing](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/05-slicing.png)

## Udfordring 3: vend om

`reverse_array` bruger `a[::-1]`, `reverse_array_with_flip` bruger `np.flip(a)`; resultatet er det samme.

![Udfordring 3: vend om](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/06-reverse.png)

## Udfordring 4: indeks for værdier forskellige fra nul

`nonzero_indices` returnerer en tuple af indeksarrays: for `[6, 0, 9, 0, 0, 5, 0]` indeksene 0, 2 og 5.

![Udfordring 4: indeks for værdier forskellige fra nul](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/07-nonzero.png)

## Udfordring 5: tilfældige tal

`random_cube` giver et 3x3x3-array af tilfældige tal; et seed gør det gentageligt.

![Udfordring 5: tilfældige tal](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/08-random.png)

## Udfordring 6: linspace

`linspace_x` er `np.linspace(0, 100, num=9)`: ni jævnt fordelte værdier, begge endepunkter inkluderet.

![Udfordring 6: linspace x](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/09-linspace-x.png)

## Udfordring 7: linspace og et liniediagram

`linspace_y` er `np.linspace(-3, 3, num=9)`. En almindelig brug af `linspace` er at generere punkterne til et diagram.

![Udfordring 7: linspace y og liniediagrammet](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/10-linspace-plot.png)

## Udfordring 8: et støjbillede

`noise_image` er et 128x128x3-array af tilfældige tal; `imshow` læser den sidste akse som rød, grøn og blå.

![Udfordring 8: støjbilledet](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/11-noise-image.png)

## Det får du ud af det

- Færdige generatorer (`arange`, `linspace`, `random`) i stedet for at skrive værdier ind.
- Slicing med start, stop og trin samt vending uden løkke.
- Tanken om, at et array af tal kan være et billede.
