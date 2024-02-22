from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


def k_formatter(x, pos):
    """Function to format float to str (thousands (k))."""
    if (x < 1000):
        return (x)
    return (f'{int(x/1e3)}k')


def display_graph(df1: pd.DataFrame, df2: pd.DataFrame, year: str):
    """display_graph(df1: pd.DataFrame, df2: pd.DataFrame, year: str
        function get dataframe values from two cvs files
        and display scatter graph"""
    try:
        assert int(year) in range(1800, 2050), "need year between 1800 - 2050"
        df1 = df1.loc[:, year]
        df2 = df2.loc[:, year]
        plt.scatter(df1, df2)
        plt.xscale('log')
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life Expectancy")
        plt.title(year)
        formatter = FuncFormatter(k_formatter)
        plt.gca().xaxis.set_major_formatter(formatter)
        plt.xticks([300, 1000, 10000])
        plt.show()
    except AssertionError as msg:
        print("AssertionError:", msg)
    except Exception as msg:
        print(msg)


def main():
    inc = load("../income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life = load("../life_expectancy_years.csv")
    if life is None or inc is None:
        return (1)
    display_graph(inc, life, '1900')


if __name__ == "__main__":
    main()
