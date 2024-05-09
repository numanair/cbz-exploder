# cbz-exploder
Breaks up all cbz files of separate volumes and chapters into sortable images

## How to use
Install python and click `cbz_exploder.py`, or run from the terminal
```
python3 cbz_exploder.py
```

Enter the full path which contains CBZ files for volumes and chapters.
After the script finishes running, an `output` directory will appear with sortable JPG/PNGs

## Note
This script works best when the files are named `<Title> v<Volume Number> c<Chapter Number>`.
The output of the jpgs are useful to plug into a tool like [KCC](https://github.com/ciromattia/kcc) to convert into epub format.