import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from functionalities import year_temperatures_plot


if __name__ == "__main__":

    dataset = pd.read_csv("../../dataset/GlobalLandTemperaturesByCountry.csv")
    c = "Italy"
    year_temperatures_plot(c, dataset=dataset)
    

