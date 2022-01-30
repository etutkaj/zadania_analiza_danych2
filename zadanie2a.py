import numpy as np
from scipy.stats import beta
import pandas as pd
import matplotlib.pyplot as plt

size = 100       # liczebność zbioru
a = 3.2          # alfa
b = 1.6          # beta

def save_file(x, y, filename):
    data = [{'x': val_x, 'y': val_y} for val_x, val_y in zip(x, y)]
    dataframe = pd.DataFrame(data)

    with open(filename, mode='w', newline="") as file:
        file.write(dataframe.to_csv(index=False))

def beta_distribution():
    x = np.linspace(beta.ppf(0.0001, a, b), beta.ppf(0.9999, a, b), size)
    y = beta.pdf(x, a, b)

    save_file(x, y, 'zadanie2a.csv')

    plt.figure(figsize=(8, 6))
    plt.xlim(0, 1)
    plt.plot(x, y, 'r-')
    plt.title('Rozkład Beta')
    plt.xlabel('X(0, 1)')
    plt.ylabel('PDF | f(X)')
    plt.savefig(fname='zadanie2a.jpg', format='jpg')


beta_distribution()
