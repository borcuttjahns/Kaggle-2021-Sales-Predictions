"""Here lie the data import functions"""

import os
from functools import lru_cache
from os.path import join
import numpy as np
import pandas as pd

path_here = os.path.dirname(os.path.dirname(__file__))

def getShops():
    path = os.path.dirname(os.path.dirname(__file__))
    shopsDF = pd.read_csv(join(path, "MLfuncs/data/shops.csv"))
    return shopsDF

def getCategories():
    path = os.path.dirname(os.path.dirname(__file__))
    catsDF = pd.read_csv(join(path, "MLfuncs/data/item_categories.csv"))
    return catsDF

def getItems():
    path = os.path.dirname(os.path.dirname(__file__))
    itemsDF = pd.read_csv(join(path, "MLfuncs/data/items.csv.zip"))
    return itemsDF

def getSalesTrain():
    path = os.path.dirname(os.path.dirname(__file__))
    trainDF = pd.read_csv(join(path, "MLfuncs/data/sales_train.csv.zip"))
    return trainDF

def getSalesTest():
    path = os.path.dirname(os.path.dirname(__file__))
    testDF = pd.read_csv(join(path, "MLfuncs/data/test.csv.zip"))
    return testDF