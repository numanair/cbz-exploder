# cbz-exploder
Breaks up all cbz files of separate volumes and chapters into sortable images.

Fun fact, `cbz` files are just glorified `zip` files. All the images can be zipped and they will be ordered, then simply rename the extension to `cbz`.

You can also plug the images into a tool like [KCC](https://github.com/ciromattia/kcc) to convert into a single `epub` format without any faff

## How to use
Install python and click `cbz_exploder.py`, or run from the terminal
```
python3 cbz_exploder.py
```

Enter the full path which contains CBZ files for volumes and chapters.
After the script finishes running, an `output` directory will appear with sortable JPG/PNGs

## Note
This script works best when the files are named `<Title> v<Volume Number> c<Chapter Number>`.
