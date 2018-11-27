import sys
import os
import json
from randommodel import RandomModel

if __name__ == "__main__":
    m = RandomModel()
    try:
        train_fname = sys.argv[1]
    except:
        train_fname = os.path.join(os.getcwd(), "development.json")

    try:
        pred_fname = sys.argv[2]
    except:
        pred_fname = os.path.join(os.getcwd(), "pred.json")

    m.predict(train_fname,pred_fname)