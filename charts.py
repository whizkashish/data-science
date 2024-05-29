import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# plt.style.use('seaborn')

df_population_raw = pd.read_json('population.json', dtype={'year': 'int64'})
df_population_raw['population'] = pd.to_numeric(df_population_raw['population'].str.replace(",",""))
df_population_raw.dropna(inplace=True)

df_pivot = df_population_raw.pivot(index='year', columns='country', values='population')

df_pivot = df_pivot[['India', 'Pakistan', 'Canada', 'China']]
# show the plot
# df_pivot.plot(kind='line')
df_pivot_2020 = df_pivot[df_pivot.index.isin(['2024'])]

# Bar Pot
df_pivot_2020 = df_pivot_2020.T
df_pivot_2020.plot(kind='bar', xlabel='year',ylabel= 'polulation')


#Piechart

df_pivot_2020.plot(kind='pie', y='2024')


#boxplot

#df_pivot.plot(kind='box', color='green', ylabel='Population')

#histogram

df_pivot.plot(kind='hist')

#scatterplot

data_frame_sample = df_population_raw[df_population_raw['country'].isin(['India','China','Pakistan'])]
sorted_arrray_sample = data_frame_sample.sort_values(by=['year'])
sorted_arrray_sample.plot(kind='scatter', x = 'year', y = 'population')

plt.savefig('test.png')

df_pivot.to_excel('pivot_table.xlsx')

plt.show()