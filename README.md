# Finding Supernova with Machine Learning
 
The goal of this project is to use machine and deep learning to classify variable sources
of light in images collected from the
[All-Sky Automated Survey for Supernovae (ASAS-SN) or Assassin](http://www.astronomy.ohio-state.edu/~assassin/index.shtml)
Project.

## Data

Currently the data are private, but it will be public eventually. It consists of of 11x11 image
patches taken in V-band. Each example contains 5 images: reference image, three difference
images, and one coadded of the three images.

### Structure

The images for each example are packaged into a fits file. We use the astropy.io.fits
package to parse these files. The fits files have an array of 6 HduObjects where the last 5 are images.
The header of the first image has 'RTYPE' which corresponds to the classification. It also has a
'RFCVAL' real source score from 0.0 (bogus) to 1.0 (real).

#### Classifications:

0 = variable star<br/>
1 = asteroid<br/>
2 = transient<br/>
3 = possible variable<br/>
4 = unknown classification<br/>
5 = some kind of bright star artifact -- can be either the core of the or a diffraction spike artifact<br/>
6 = some other kind of artifact<br/>

## Getting Started

The scripts are Python 3 and Jupyter Notebooks.
The first experiment uses [XGBoost](https://xgboost.readthedocs.io/en/latest/). You can follow
their [installation guide](https://xgboost.readthedocs.io/en/latest/build.html) for your platform.

Other Python packages needed are:

* astropy
* matplotlib
* numpy
* scikit-learn

Unpack the tar file into the `data/` directory then run the cells in the XGBoost.ipynb Jupyter notebook.

# Future Work

A neural network will be setup with Keras to see if it can out perform XGBoost.
