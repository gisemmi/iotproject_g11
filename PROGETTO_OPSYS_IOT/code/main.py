import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import functionalities as funcs


if __name__ == "__main__":

    dataset = pd.read_csv("../../dataset/GlobalLandTemperaturesByCountry.csv")
    c = "Italy"
    m = "AVG"
    y = 1743

    #burnt_area_plot(c, dataset)
    #year_temperatures_plot(c, dataset=dataset)
    funcs.year_temperatures_plot(c, m, dataset)

