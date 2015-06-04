import pickle
import os


def storeDataInPickle(fileOut, dataToStore):
    with open(fileOut, "wb") as fo:
        pickle.dump(dataToStore, fo)


def loadDataFromPickle(fileIn=None):
    if os.path.isfile(fileIn) and os.access(fileIn, os.R_OK):
        with open(fileIn, "rb") as fi:
            v = pickle.load(fi)
        return v
    else:
        print("Error: %s is not found or is not accessible." % fileIn)
        os.sys.exit(1)

def loadDataFromTxt(arg1):
    """TODO: Docstring for loadDataFromTxt.

    :arg1: TODO
    :returns: TODO

    """
    pass
