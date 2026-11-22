import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



def year_temperatures_plot(country : str, dataset : pd.DataFrame):
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
        avg_temps.append(temp_per_year.max())
        
    # Plot risultati
    plt.plot(years, avg_temps)
    plt.xlabel("Anno")
    plt.ylabel("Temperatura media di picco")
    plt.title(f"Evoluzione temperatura {country}")
    plt.show()
 
      


    
        
        


        
    
    
    


    
    
