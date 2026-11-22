import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



def year_temperatures_plot(country : str, mode : str, dataset : pd.DataFrame):
    #Filtro per la nazione assegnata
    country_temps = dataset[dataset["Country"] == country].dropna()
    # Asse x: Anni
    years = list(set(x.year for x in pd.to_datetime(country_temps["dt"])))
    print(years)
    avg_temps = []
    # Asse y: Massima temperatura ogni anno
    for y in years:
        mask = pd.to_datetime(country_temps["dt"]).dt.year == y
        temp_per_year = country_temps.loc[mask, "AverageTemperature"]
        if (mode.lower() == "max"):
            avg_temps.append(temp_per_year.max())
        elif (mode.lower() == "avg"):
            avg_temps.append(temp_per_year.mean())
        if (mode.lower() == "min"):
            avg_temps.append(temp_per_year.min())        
        
        
    # Plot risultati
    plt.plot(years, avg_temps)
    plt.xlabel("Anno")
    plt.ylabel("Temperatura media di picco")
    plt.title(f"Evoluzione temperatura {country}")
    plt.show()

def cities_avgtemp_plot(country : str, year : int, dataset : pd.DataFrame):
    country_year_temps = dataset[dataset["Country"] == country]
    country_year_temps = country_year_temps[pd.to_datetime(country_year_temps["dt"]).dt.year == year].dropna().copy()
    
    #Estrazione città e temperature massime per città
    cities_max_temps = country_year_temps[["City", "AverageTemperature"]].groupby(["City"]).max()
    #Temperatura media delle massime temperature per città
    avg_temp = cities_max_temps["AverageTemperature"].mean()

    #Estrazione città e temperature
    cities = country_year_temps["City"].drop_duplicates().to_list()
    avg_temps = cities_max_temps["AverageTemperature"].to_list()

    fig, ax = plt.subplots(figsize = (10,5))

    ax.scatter(
        cities,
        avg_temps,
        color="steelblue"
    )
    ax.axhline(
        avg_temp,
        color="crimson",
        linewidth=1.5,
        label=f"Media: {avg_temp}"
    )

    plt.xlabel("Città")
    plt.ylabel("Temperatura massima")
    plt.title(f"Città che hanno superato la temperatura media ({country}-{year}")
    plt.show()

def n_fires_plot(country : str, dataset : pd.DataFrame):
    country_fires = dataset[["Year", country]].dropna().copy()
    # Asse x: Anno
    years = country_fires["Year"].to_list()
    n_of_fires = country_fires[country].to_list()
    
    plt.plot(years, n_of_fires)
    plt.xlabel("Anno")
    plt.ylabel("Numero di incendi")
    plt.title(f"Evoluzione numero di incendi {country}")
    plt.show()

def burnt_areas_plot(country : str, dataset : pd.DataFrame):
    country_fires = dataset[["Year", country]].dropna().copy()
    # Asse x: Anno
    years = country_fires["Year"].to_list()
    burnt_areas = country_fires[country].to_list()
    
    plt.plot(years, burnt_areas)
    plt.xlabel("Anno")
    plt.ylabel("Aree incendiate")
    plt.title(f"Evoluzione aree incendiate {country}")
    plt.show()



    
      


    
        
        


        
    
    
    


    
    
