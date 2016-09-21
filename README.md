# DDSM-LJPEG
This repository is created for converting Mammography of [Digital Database for Screening Mammography (DDSM)](http://marathon.csee.usf.edu/Mammography/Database.html) form LJPEG to more ordinary format.

## Prerequisite
[ImageMagick](http://www.imagemagick.org/) is a great tool for image processing.


## Install
1. Download the resources.
```
# make sure to clone with --recursive
git clone --recursive git@github.com:Xiaoming-Zhao/DDSM-LJPEG.git
```

2. ljpeg
```
cd ljpeg/jpegdir
make
```

3. ddsm
```
cd ddsm/ddsm-software
g++ -Wall -O2 ddsmraw2pnm.c -o ddsmraw2pnm
```

## Usage
Directly run the command below. I just write the `ddsm_ljpeg.sh` to fit my desire. It is easy for anyone who want to use for their own need to modify the bash code.
```
bash /path/to/DDSM-LJPEG/ddsm_ljpeg.sh -d /path/to/your/LJPEG/directory -i /path/to/your/imdb_IRMA
```