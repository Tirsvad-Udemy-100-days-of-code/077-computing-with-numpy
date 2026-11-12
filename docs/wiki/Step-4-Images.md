**English** · [Dansk](Step-4-Images-da) · [Bahasa Malaysia](Step-4-Images-ms)

# Step 4: Images as ndarrays

An image is a collection of pixels, and a pixel is a combination of red, green and blue. So a colour image is a 3-dimensional array: rows, columns and 3 channels. Code: `computing_with_numpy.domain.images`.

The lecture's raccoon picture comes from `scipy.misc.face()`, which no longer exists. This project generates a picture of the same size (768 x 1024 x 3) instead; see the decision record ADR-0001 in the repository. `load_image(path)` opens any 3-channel picture of your own.

## Type, shape and resolution

The picture is a `numpy.ndarray` of `uint8` with shape `(768, 1024, 3)`: 3 dimensions, a resolution of 1024 x 768.

![Images are ndarrays](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/16-image-info.png)
![Show the image](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/17-image-show.png)

## Convert to grayscale

Divide by 255 to get sRGB values between 0 and 1 (broadcasting), then multiply by `[0.2126, 0.7152, 0.0722]` with matrix multiplication. The result is a 2-dimensional array; `cmap='gray'` tells Matplotlib it is black and white.

![Convert the image to grayscale](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/18-grayscale.png)

## Flip, rotate and invert

`np.flip` turns the grayscale image upside down, `np.rot90` rotates the colour image, and `255 - img` inverts (solarizes) it.

![Flip the grayscale image](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/19-flip-gray.png)
![Rotate the colour image](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/20-rotate.png)
![Invert the colour image](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/21-invert.png)

## Use your own image

Open a picture with Pillow and turn it into an array. It needs 3 channels (a 4-channel PNG needs extra steps).

![Use your own image](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/22-own-image.png)

## What you gain

- Pictures are numbers, so every array tool works on them.
- Broadcasting and matrix multiplication solve a real task: grayscale in two lines.
- Flip, rotate and invert are one-liners on the array.
