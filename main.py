# This is an example of popping a packet from the Emotiv class's packet queue
# and printing the gyro x and y values to the console. 

import data_gatherer
from utils import *
import numpy as np
import matplotlib.pyplot as plt
from data import *

if __name__ == "__main__":

    data_gatherer.session()

    # prepare_training_data()