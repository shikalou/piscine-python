from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


def millions_formatter(x, pos):
    """function to format float to str (millions (M))."""
    return (f'{int(x/1e6)}M')


def display_graph(file: pd.DataFrame, cou: list):
    """display_graph(file: pd.DataFrame, cou: list)
    function to reformat dataframe values and display plot graph
    takes a dataframe panda object as first params and a list of 2
    country in english as second params"""
    try:
        assert len(cou) == 2, "needs two country name in english"
        cou.sort()
        data = file[(file['country'] == cou[0]) | (file['country'] == cou[1])]
        assert len(data) == 2, "country not in database"
        data = data.transpose()
        data = data[1:]
        data.reset_index(inplace=True)
        data.columns = ['Year', cou[0], cou[1]]
        data['Year'] = data['Year'].astype(int)
        data = data[data['Year'] <= 2050]
        data[cou[0]] = data[cou[0]].str.replace('M', 'e6')\
            .str.replace('k', 'e3').astype(float)
        data[cou[1]] = data[cou[1]].str.replace('M', 'e6')\
            .str.replace('k', 'e3').astype(float)
        # print(data)
        formatter = FuncFormatter(millions_formatter)
        plt.gca().yaxis.set_major_formatter(formatter)
        plt.plot(data["Year"], data[cou[0]], label=cou[0])
        plt.plot(data["Year"], data[cou[1]], label=cou[1])
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.title("Population Projections")
        plt.legend([cou[0], cou[1]])
        plt.show()
    except AssertionError as msg:
        print("AssertionError:", msg)
    except Exception as msg:
        print(msg)


def main():
    file = load("../population_total.csv")
    if file is None:
        return (1)
    display_graph(file, ['France', 'Belgium'])


if __name__ == "__main__":
    main()
