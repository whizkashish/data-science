import pandas as pd
import cufflinks as cf
import plotly.offline as pyo

# Initialize Plotly offline mode
pyo.init_notebook_mode(connected=False)
cf.set_config_file(sharing='public', theme='ggplot', offline=True)
print("Plotly initialized:", hasattr(pyo, '__PLOTLY_OFFLINE_INITIALIZED'))

# Read and clean the data
df_population_raw = pd.read_json('population.json', dtype={'year': 'int64'})
df_population_raw['population'] = pd.to_numeric(df_population_raw['population'].str.replace(",", ""))
df_population_raw.dropna(inplace=True)

# Make a pivot table
df_pivot = df_population_raw.pivot(index='year', columns='country', values='population')

# Select some countries
df_pivot = df_pivot[['United States', 'India', 'China', 'Indonesia', 'Brazil']]

# Display the pivot table (optional for script-based environments)
print(df_pivot)

# Line plot
fig_line = df_pivot.iplot(kind='line', xTitle='Years', yTitle='Population', title='Population (1955-2020)', asFigure=True)
pyo.plot(fig_line, filename='line_plot.html')

# Bar plot for the year 2024
df_pivot_2024 = df_pivot[df_pivot.index == '2024'].T
fig_bar_2024 = df_pivot_2024.iplot(kind='bar', color='lightgreen', xTitle='Country', yTitle='Population', title='Population in 2024', asFigure=True)
pyo.plot(fig_bar_2024, filename='bar_plot_2024.html')

# Bar plot for selected years
df_pivot_sample = df_pivot[df_pivot.index.isin(['1980', '1990', '2000', '2010', '2020', '2024'])]
fig_bar_sample = df_pivot_sample.iplot(kind='bar', xTitle='Years', yTitle='Population', title='Population in Selected Years', asFigure=True)
pyo.plot(fig_bar_sample, filename='bar_plot_sample.html')

# Pie chart for the year 2024
df_pivot_2024_pie = df_pivot[df_pivot.index == '2024'].T.reset_index()
df_pivot_2024_pie.columns = ['country', '2024']
fig_pie_2024 = df_pivot_2024_pie.iplot(kind='pie', labels='country', values='2024', title='Population Distribution in 2024', asFigure=True)
pyo.plot(fig_pie_2024, filename='pie_chart_2024.html')

# Box plot for United States
fig_box_us = df_pivot['United States'].iplot(kind='box', color='green', yTitle='Population', title='Population of United States', asFigure=True)
pyo.plot(fig_box_us, filename='box_plot_us.html')

# Box plot for all countries
fig_box_all = df_pivot.iplot(kind='box', yTitle='Population', title='Population Distribution by Country', asFigure=True)
pyo.plot(fig_box_all, filename='box_plot_all.html')

# Histogram
fig_hist = df_pivot.iplot(kind='hist', xTitle='Population', bins=3, title='Population Histogram', asFigure=True)
pyo.plot(fig_hist, filename='histogram.html')

# Scatter plot
fig_scatter = df_pivot.iplot(kind='scatter', mode='markers', xTitle='Years', yTitle='Population', title='Population Scatter Plot', asFigure=True)
pyo.plot(fig_scatter, filename='scatter_plot.html')
