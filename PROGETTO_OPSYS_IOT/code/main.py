import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from functionalities import cities_avgtemp_plot


if __name__ == "__main__":

    dataset = pd.read_csv("../../dataset/GlobalLandTemperaturesByCity.csv")
    c = "Italy"
    y = 1743
    #burnt_area_plot(c, dataset)
    #year_temperatures_plot(c, dataset=dataset)
    cities_avgtemp_plot(c,y,dataset)

