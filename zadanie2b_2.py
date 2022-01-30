import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

filename = 'zadanie2b.xlsx'

def draw_trendline():
    # Wczytanie pliku xlsx
    data = pd.read_excel(filename)
    # Wybranie danych z jednego dnia w każdym miesiącu
    data_every_30th_day = data.iloc[::672, :]
    # Wyliczenie danych do wykresów
    x = np.arange(len(data_every_30th_day.index))
    fit = np.polyfit(x, data_every_30th_day['CO(GT)'], 1)
    fit_fn = np.poly1d(fit)
    y = fit_fn(x)
    # Narysowanie wykresów
    plt.title('Stężenie CO w mg/m^3 w poszczególnych miesiącach')
    plt.xlabel('Miesiąc')
    plt.ylabel('Stężenie CO[mg/m^3]')
    plt.plot(data_every_30th_day['Date'], y, 'k-')
    plt.plot(data_every_30th_day['Date'], data_every_30th_day['CO(GT)'], '-o', ms=2)
    plt.savefig(fname='zadanie2b.jpg', format='jpg')

draw_trendline()
