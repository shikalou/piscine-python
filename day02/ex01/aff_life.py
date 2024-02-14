from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def display_graph(file: pd.DataFrame, country: str):
    """function which format dataframe received as parameter and
    display plot graph of chosen country info"""
    try:
        assert country != "", "needs existing country name in english"
        fra = file[file['country'] == country]
        assert not fra.empty, "country not found in database"
        fra = fra.transpose()
        fra = fra[1:]
        fra.reset_index(inplace=True)
        fra.columns = ['Year', 'Life expectancy']
        # print(fra)
        fra.plot(x='Year', y='Life expectancy')
        plt.title(f'{country} Life expectancy projections')
        plt.ylabel('Life expectancy')
        plt.show()
    except AssertionError as msg:
        print("AssertionError:", msg)
    except Exception as msg:
        print(msg)


def main():
    file = load("../life_expectancy_years.csv")
    if file is None:
        return (1)
    # print(file)
    display_graph(file, "Italy")


if __name__ == "__main__":
    main()
