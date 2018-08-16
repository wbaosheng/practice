import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
    population = pd.Series([1000, 2000, 3000])
    cities = pd.DataFrame({'City name': city_names, 'Population': population})
    # print type(cities['City name'])
    # print cities['City name']
    #
    # print type(cities['City name'][1])
    # print cities['City name'][1]
    #
    # print type(cities['City name'][0:2])
    # print cities['City name'][0:2]
    #
    # print population / 1000

    # print np.log(population)

    print population.apply(lambda val: val > 2000)

    # read from remote
    california_housing_dataframe = pd.read_csv('/home/wbs/Downloads/california_housing_train.csv', sep=',')
    california_housing_dataframe.describe()
    california_housing_dataframe.hist('housing_median_age')
    # plt.show()

if __name__ == '__main__':
    main()
