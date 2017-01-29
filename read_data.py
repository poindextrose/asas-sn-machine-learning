import os.path
import glob

from astropy.io import fits
import numpy as np


def read_fits(path):
    """Reads all fits files in path. Each fits file should have 5 images at indices 1 through 5
    in the Hdulist object."""
    print('Reading fits files in {}'.format(path))
    X, rfc, y, bad = [], [], [], 0
    images = 5
    file_names = glob.glob(os.path.join(path, '*.fits'))
    if len(file_names) == 0:
        raise Exception("No fits files found in {}".format(path))
    for file_name in file_names:
        with fits.open(file_name) as hdulist:
            if len(hdulist) < images + 1:
                bad += 1
                continue
            X.append(np.array([hdu.data for hdu in hdulist[1:images + 1]]))
            y.append(hdulist[1].header['RTYPE'])
            rfc.append(hdulist[1].header['RFCVAL'])
    print("Found {} bad fits files".format(bad))
    print("Processed {} good fits files".format(len(X)))
    return np.array(X), np.array(rfc), np.array(y, dtype=np.int8)


def get_raw_data():
    """Get the image data without any pre-processing"""
    Xy_raw_file_name = 'Xy_raw.npz'
    if os.path.exists(Xy_raw_file_name):
        print("Restoring X and y from {}".format(Xy_raw_file_name))
        npz_file = np.load(Xy_raw_file_name)
        X = npz_file['X']
        rfc = npz_file['rfc']
        y = npz_file['y']
        print("Done")
    else:
        X, rfc, y = read_fits('data/deepl/')
        np.savez(Xy_raw_file_name, X=X, rfc=rfc, y=y)
    return X, rfc, y
