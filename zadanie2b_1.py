import io
import pandas as pd
import numpy as np

filename = "zadanie2b.xlsx"

def fill_missing_values():
    # Odczyt danych z pliku excel
    # Na pliku .csv nie działała funkcja "replace"
    data = pd.read_excel(filename)
    # Zamiana domyślnych brakujących danych (-200) wartościami NaN
    data = data.replace(-200, np.nan)
    # Wypełnienie brakujących (NaN) wartości danymi z poprzedniego znacznika czasowego
    fixed_data = data.bfill()
    # Zapis do pliku
    writer = pd.ExcelWriter(filename, engine='openpyxl')
    fixed_data.to_excel(excel_writer=writer, index=False)
    writer.save()

fill_missing_values()
