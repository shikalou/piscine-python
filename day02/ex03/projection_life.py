from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


def display_graph(file: pd.DataFrame, year: int):
    """function to reformat dataframe values and display scatter graph"""
    try:
        assert year in range(1800, 2050), "need year between 1800 and 2050"
        res = 
        print("lol")
    except AssertionError as msg:
        print("AssertionError:", msg)
    except Exception as msg:
        print(msg)


def main():
    file = load("../income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    if file is None:
        return (1)
    display_graph(file, 1900)


if __name__ == "__main__":
    main()
