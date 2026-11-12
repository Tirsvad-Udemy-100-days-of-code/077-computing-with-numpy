**English** · [Dansk](Step-2-Generating-ndarrays-da) · [Bahasa Malaysia](Step-2-Generating-ndarrays-ms)

# Step 2: Generating and manipulating ndarrays

Eight small challenges show the functions you meet most often. Code: `computing_with_numpy.domain.generating`.

## Challenge 1: arange

`create_range_vector()` is `np.arange(10, 30)`: the values 10 to 29.

![Challenge 1: arange](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/04-arange.png)

## Challenge 2: slicing

`last_three`, `fourth_to_sixth`, `all_except_first_twelve` and `every_second` are `a[-3:]`, `a[3:6]`, `a[12:]` and `a[::2]`.

![Challenge 2: slicing](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/05-slicing.png)

## Challenge 3: reverse

`reverse_array` uses `a[::-1]`, `reverse_array_with_flip` uses `np.flip(a)`; the result is the same.

![Challenge 3: reverse](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/06-reverse.png)

## Challenge 4: non-zero indices

`nonzero_indices` returns a tuple of index arrays: for `[6, 0, 9, 0, 0, 5, 0]` the indices 0, 2 and 5.

![Challenge 4: non-zero indices](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/07-nonzero.png)

## Challenge 5: random numbers

`random_cube` gives a 3x3x3 array of random numbers; a seed makes it repeatable.

![Challenge 5: random](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/08-random.png)

## Challenge 6: linspace

`linspace_x` is `np.linspace(0, 100, num=9)`: nine evenly spaced values, both ends included.

![Challenge 6: linspace x](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/09-linspace-x.png)

## Challenge 7: linspace and a line chart

`linspace_y` is `np.linspace(-3, 3, num=9)`. A common use of `linspace` is to generate the points of a chart.

![Challenge 7: linspace y and the line chart](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/10-linspace-plot.png)

## Challenge 8: a noise image

`noise_image` is a 128x128x3 array of random numbers; `imshow` reads the last axis as red, green and blue.

![Challenge 8: the noise image](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/11-noise-image.png)

## What you gain

- Ready-made generators (`arange`, `linspace`, `random`) instead of typing values.
- Slicing with start, stop and step, and reversing without a loop.
- The idea that an array of numbers can be a picture.
