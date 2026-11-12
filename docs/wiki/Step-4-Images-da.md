[English](Step-4-Images) · **Dansk** · [Bahasa Malaysia](Step-4-Images-ms)

# Trin 4: Billeder som ndarrays

Et billede er en samling pixels, og en pixel er en kombination af rød, grøn og blå. Et farvebillede er altså et 3-dimensionalt array: rækker, kolonner og 3 kanaler. Kode: `computing_with_numpy.domain.images`.

Lektionens vaskebjørnebillede kommer fra `scipy.misc.face()`, som ikke findes mere. Dette projekt genererer i stedet et billede i samme størrelse (768 x 1024 x 3); se beslutningsnotatet ADR-0001 i repositoriet. `load_image(path)` åbner et vilkårligt 3-kanals billede af dit eget.

## Type, shape og opløsning

Billedet er et `numpy.ndarray` af `uint8` med shape `(768, 1024, 3)`: 3 dimensioner og en opløsning på 1024 x 768.

![Billeder er ndarrays](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/16-image-info.png)
![Vis billedet](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/17-image-show.png)

## Konvertér til gråtoner

Divider med 255 for at få sRGB-værdier mellem 0 og 1 (broadcasting), og multiplicer derefter med `[0.2126, 0.7152, 0.0722]` med matrixmultiplikation. Resultatet er et 2-dimensionalt array; `cmap='gray'` fortæller Matplotlib, at det er sort/hvidt.

![Konvertér billedet til gråtoner](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/18-grayscale.png)

## Spejl, rotér og inverter

`np.flip` vender gråtonebilledet på hovedet, `np.rot90` roterer farvebilledet, og `255 - img` inverterer (solariserer) det.

![Spejl gråtonebilledet](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/19-flip-gray.png)
![Rotér farvebilledet](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/20-rotate.png)
![Inverter farvebilledet](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/21-invert.png)

## Brug dit eget billede

Åbn et billede med Pillow og lav det om til et array. Det skal have 3 kanaler (en 4-kanals PNG kræver ekstra trin).

![Brug dit eget billede](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/077-computing-with-numpy/raw/branch/main/docs/images/22-own-image.png)

## Det får du ud af det

- Billeder er tal, så alle array-værktøjer virker på dem.
- Broadcasting og matrixmultiplikation løser en virkelig opgave: gråtoner på to linjer.
- Spejling, rotation og invertering er enlinjeløsninger på arrayet.
