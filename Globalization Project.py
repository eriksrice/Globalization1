import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
sns.set_style('darkgrid')

#importing trade to world GDP ratio data
trade_to_gdp_ratio_df = pd.read_csv('/Users/erikrice/Downloads/world-trade-gdp-ratio (1).csv')

#quick look at the data
print(trade_to_gdp_ratio_df.head())
print(trade_to_gdp_ratio_df.dtypes)

#converting date column to datetime 
trade_to_gdp_ratio_df['date'] = pd.to_datetime(trade_to_gdp_ratio_df['date'])
print(trade_to_gdp_ratio_df.dtypes)

#let's get a visual of this
sns.set_palette('Blues_d')
sns.relplot(data=trade_to_gdp_ratio_df, kind='line', x='date', y=' Trade (% of GDP)')
plt.xlabel('Year') 
plt.ylabel('% of GDP')
plt.title('Trade to World GDP (%)', y=.94)
plt.show()

#what about the last decade? 2023 data (even projects) isn't available, so 2022 is the most recent year
trade_to_gdp_ratio_10yr_df = trade_to_gdp_ratio_df[trade_to_gdp_ratio_df['date'] > '2012-12-31']
print(trade_to_gdp_ratio_10yr_df)

#what about the last three years (excluding 2023 so far)
trade_to_gdp_ratio_3yr_df = trade_to_gdp_ratio_df[trade_to_gdp_ratio_df['date'] > '2019-12-31']
print(trade_to_gdp_ratio_3yr_df)

#let's pivot now to FDI data. importing the df
FDI_df = pd.read_csv('/Users/erikrice/Downloads/world-foreign-direct-investment (1).csv')
print(FDI_df.head())
print(FDI_df.dtypes)

#changing year column to datatype data
FDI_df['date'] = pd.to_datetime(FDI_df['date'])
print(FDI_df.dtypes)

#let's see a visual of the FDI data over time
sns.set_palette('BuGn_d')
sns.relplot(data=FDI_df, kind='line', x='date', y=' Inflows')
plt.xlabel('Year') 
plt.ylabel('FDI (USD)')
plt.title('Global Foreign Direct Investment', y=.94)
plt.show()

#what about the last decade?
FDI_10yr_df = FDI_df[FDI_df['date'] > '2012-12-31']
print(FDI_10yr_df)

#what about the last three years only?
FDI_3yr_df = FDI_df[FDI_df['date'] > '2019-12-31']
print(FDI_3yr_df)

#let's merge these datatables for future macro analysis
df = trade_to_gdp_ratio_df.merge(FDI_df, on='date', how='outer')
print(df)

#cleaning up new macro dataframe
df['Year'] = df['date']
df['Trade (% of GDP)'] = df[' Trade (% of GDP)']
df['Annual Change (% of GDP)'] = df[' Annual Change']
df['FDI (in Billions of USD)'] = df[' Inflows']
df['FDI (% of GDP)'] = df[' US $']
df = df[['Year', 'Trade (% of GDP)', 'Annual Change (% of GDP)', 'FDI (in Billions of USD)', 'FDI (% of GDP)']]
print(df)

#what about world exports?
exports_df = pd.read_csv('/Users/erikrice/Downloads/world-exports.csv')
print(exports_df.head())
print(exports_df.dtypes)

#converting date column to datetime 
exports_df['date'] = pd.to_datetime(exports_df['date'])
print(exports_df.dtypes)

#what about the last decade?
exports_10yr_df = exports_df[exports_df['date'] > '2012-12-31']
print(exports_10yr_df)

#what about the last three years only?
exports_3yr_df = exports_df[exports_df['date'] > '2019-12-31']
print(exports_3yr_df)

#cleaning export data for merge
exports_df['Year'] = exports_df['date']
exports_df['Exports (in Billions of USD)'] = exports_df[' Billions of US $']
exports_df['Exports (% of GDP)'] = exports_df[' % of GDP']
exports_df = exports_df[['Year', 'Exports (in Billions of USD)', 'Exports (% of GDP)']]

#merging into macro dataframe
df = df.merge(exports_df, how='outer', on='Year')
print(df)

#let's get a visual of world exports across time
sns.set_palette('BuPu_d')
sns.relplot(data=df, kind='line', x='Year', y='Exports (in Billions of USD)')
plt.xlabel('Year') 
plt.ylabel('Exports (in Billions of (USD)')
plt.title('Global Exports Over Time', y=.94)
plt.show()

#what about the other side of this coin - imports?
imports_df = pd.read_csv('/Users/erikrice/Downloads/world-imports.csv')
print(imports_df.head())
print(imports_df.dtypes)

#converting date column to datetime 
imports_df['date'] = pd.to_datetime(imports_df['date'])
print(imports_df.dtypes)

#what about the last decade?
imports_10yr_df = imports_df[imports_df['date'] > '2012-12-31']
print(imports_10yr_df)

#what about the last three years only?
imports_3yr_df = imports_df[imports_df['date'] > '2019-12-31']
print(imports_3yr_df)

#cleaning import data for merge
imports_df['Year'] = imports_df['date']
imports_df['Imports (in Billions of USD)'] = imports_df[' Billions of US $']
imports_df['Imports (% of GDP)'] = imports_df[' % of GDP']
imports_df = imports_df[['Year', 'Imports (in Billions of USD)', 'Imports (% of GDP)']]

#merging into macro dataframe
df = df.merge(imports_df, how='outer', on='Year')
print(df)

#let's get a visual of the global import data 
sns.set_palette('GnBu_d')
sns.relplot(data=df, kind='line', x='Year', y='Imports (in Billions of USD)')
plt.xlabel('Year') 
plt.ylabel('Imports (in Billions of USD)')
plt.title('Global Imports Over Time', y=.94)
plt.show()

#what about global tariff rates?
tariff_df = pd.read_csv('/Users/erikrice/Downloads/world-tariff-rates (1).csv')
print(tariff_df.head())
print(tariff_df.dtypes)

#converting date column to datetime 
tariff_df['date'] = pd.to_datetime(tariff_df['date'])
print(tariff_df.dtypes)

#what about the last decade?
tariff_10yr_df = tariff_df[tariff_df['date'] > '2012-12-31']
print(tariff_10yr_df)

#cleaning tariff data for merge
tariff_df['Year'] = tariff_df['date']
tariff_df['Mean World Tariff Rate'] = tariff_df[' Applied']
tariff_df = tariff_df[['Year', 'Mean World Tariff Rate']]

#merging into macro dataframe
df = df.merge(tariff_df, how='outer', on='Year')
print(df)

#let's get a visual
sns.set_palette('Greens_d')
sns.relplot(data=df, kind='line', x='Year', y='Mean World Tariff Rate')
plt.xlabel('Year') 
plt.ylabel('Mean Tariff Rate')
plt.title('Mean Global Tariff Rate Over Time', y=.94)
plt.show()

#what about tourism spending internationally?
tourism_df = pd.read_csv('/Users/erikrice/Downloads/world-tourism-statistics (1).csv')
print(tourism_df.head())
print(tourism_df.dtypes)

#converting year to datetime
tourism_df['date'] = pd.to_datetime(tourism_df['date'])
print(tourism_df.dtypes)

#what about the last decade?
tourism_10yr_df = tourism_df[tourism_df['date'] > '2012-12-31']
print(tourism_10yr_df)

#cleaning data for merge into main dataframe
tourism_df['Year'] = tourism_df['date']
tourism_df['Tourism Spending (USD)'] = tourism_df[' Spending ($)']
tourism_df['Tourism Spending (% of Exports)']= tourism_df[' % of Exports']
tourism_df = tourism_df[['Year', 'Tourism Spending (USD)', 'Tourism Spending (% of Exports)']]

#merging into main macro dataframe
df = df.merge(tourism_df, how='outer', on='Year')
print(df)

#let's get a visual for the tourism data
sns.set_palette('Greys_d')
sns.relplot(data=df, kind='line', x='Year', y='Tourism Spending (USD)')
plt.xlabel('Year') 
plt.ylabel('USD')
plt.title('Global Tourism Spending (USD) Over Time', y=.94)
plt.show()

#one final massasing of the tourism data for integration at end graphs. (converting raw USD to billions)
df['Tourism Spneding (USD in Billions)'] = (df['Tourism Spending (USD)'] / 1000000000)

#perhaps the most often-cited argument for deglobalization is merchandise trade as a % of GDP, and even that has rebounded a ton. let's take a look
merchandise_df = pd.read_csv('/Users/erikrice/Downloads/API_TG.VAL.TOTL.GD.ZS_DS2_en_csv_v2_5874556/API_TG.VAL.TOTL.GD.ZS_DS2_en_csv_v2_5874556.csv')
print(merchandise_df.head())
print(merchandise_df.dtypes)

#this dataframe is in a wide format and needs to be unpivoted. first let's isolate the world data, since we don't care about individual countries here
merchandise_df = merchandise_df[merchandise_df['Country Name'] == 'World']
print(merchandise_df.head())

#time to unpivot table 
merchandise_df = merchandise_df.melt()
print(merchandise_df)

#cleaning table before getting visual
merchandise_df = merchandise_df.loc[4:66]
print(merchandise_df)

#final cleaning then merging into macro dataframe
merchandise_df['Year'] = merchandise_df['variable']
merchandise_df['Merchandise Trade (% of GDP)'] = merchandise_df['value']
merchandise_df = merchandise_df[['Year', 'Merchandise Trade (% of GDP)']]
print(merchandise_df)

#date formats don't match. must extract year from main dataframe to combine
df['Year'] = df['Year'].dt.year
print(df.dtypes)

#alligning datatypes
merchandise_df['Year'] = merchandise_df['Year'].astype(int)
print(merchandise_df.dtypes)

#merge should work now, and year column should be ready to conver to datetime 
df = df.merge(merchandise_df, on='Year', how='outer')
print(df.dtypes)
df['Year'] = pd.to_datetime(df.Year, format='%Y')
print(df.head())
print(df.dtypes)

#finally time for a visual of the merchandise data
sns.set_palette('OrRd_d')
sns.relplot(data=df, kind='line', x='Year', y='Merchandise Trade (% of GDP)')
plt.xlabel('Year') 
plt.ylabel('% of GDP')
plt.title('Global Merchandise Trade (% of GDP) Over Time', y=.94)
plt.show()

#what about global trade in services as a percentage of GDP?
services_df = pd.read_csv('/Users/erikrice/Downloads/global trade in services/API_NE.TRD.GNFS.ZS_DS2_en_csv_v2_5871884.csv')
print(services_df.head())
print(services_df.dtypes)

#this dataframe is also in a wide format and needs to be unpivoted. first let's isolate the world data, since we don't care about individual countries here
services_df = services_df[services_df['Country Name'] == 'World']
print(services_df.head())
      
#time to unpivot table 
services_df = services_df.melt()
print(services_df)

#cleaning table before getting visual
services_df = services_df.loc[4:66]
print(services_df)

#cleaning up trade in services table
services_df['Year'] = services_df['variable']
services_df['Services (% of GDP)'] = services_df['value']
services_df = services_df[['Year','Services (% of GDP)' ]]

#changing to datetime format
services_df['Year'] = pd.to_datetime(services_df['Year'])

#merging into main table
df = df.merge(services_df, how='outer', on='Year')
print(df.head())

#time for a visual of services
sns.set_palette('Oranges_d')
sns.relplot(data=df, kind='line', x='Year', y='Services (% of GDP)')
plt.xlabel('Year') 
plt.ylabel('(% of GDP)')
plt.title('Global Trade in Services (% of GDP) Over Time', y=.94)
plt.show()

#what about digital trade, which famously skyrocked (proportionally) during the pandemic
digital_df = pd.read_csv('/Users/erikrice/Downloads/us_digitallydeliverableservices_15327080298793.csv')
print(digital_df.head())
print(digital_df.dtypes)

#different source, but this is also a wide format and we'll need to isolate just the world data. 
digital_df = digital_df[digital_df['YEAR'] == 'World']
print(digital_df.head())

#time to unpivot table 
digital_df = digital_df.melt()
print(digital_df.head())

#removing top "row", which will mess up any analysis
digital_df = digital_df.loc[1:]
print(digital_df.head())

#cleaning up digital table
digital_df['Year'] = digital_df['variable']
digital_df['Digital Trade (USD in Millions)'] = digital_df['value']
digital_df = digital_df[['Year', 'Digital Trade (USD in Millions)']]
digital_df = digital_df.sort_values('Digital Trade (USD in Millions)')
print(digital_df.head())

#changing to datetime
digital_df['Year'] = pd.to_datetime(digital_df['Year'])
print(digital_df.dtypes)

#merging into main dataframe
df = df.merge(digital_df, on='Year', how='outer')
print(df.head())

#let's see a visual of digital trade
sns.set_palette('PuBu_d')
sns.relplot(data=df, kind='line', x='Year', y='Digital Trade (USD in Millions)')
plt.xlabel('Year') 
plt.ylabel('USD (in Millions)')
plt.gca().invert_yaxis()
plt.title('Global Digital Trade (USD in Millions) Over Time', y=.94)
plt.show()

#what about regional trade agreements (RTAs)?
RTA_df = pd.read_csv('/Users/erikrice/Downloads/RTA Data - Evolution Dashboard.csv')
print(RTA_df.head())
print(RTA_df.dtypes)

#some minor cleanup. less on this one than others
RTA_df['Year'] = RTA_df['Year of entry into force']
RTA_df['Active RTAs'] = RTA_df['Cumulative Number of RTAs in force']
RTA_df = RTA_df[['Year', 'Active RTAs']]

#changing to datetime
RTA_df['Year'] = pd.to_datetime(RTA_df.Year, format='%Y')
print(RTA_df.dtypes)

#merging into main dataframe
df = df.merge(RTA_df, on='Year', how='outer')

#dates are disjointed + taked-on in a couple columns. let's sort the data
df = df.sort_values('Year')
print(df.head())

#let's peak at the RTA data 
sns.set_palette('PuBuGn_d')
sns.relplot(data=df, kind='line', x='Year', y='Active RTAs')
plt.xlabel('Year') 
plt.ylabel('Active RTAs')
plt.title('Cumulative Global Number of Regional Trade Agreements Over Time', y=.94)
plt.show()

#what about the record-setting data out of the panama canal? 
panama_df = pd.read_csv('/Users/erikrice/Downloads/Panama Canal Data - Sheet1.csv')
print(panama_df.head())
print(panama_df.dtypes)

#quick cleanup and it goes into the main dataframe too
panama_df['Year'] = pd.to_datetime(panama_df['Year'])
print(panama_df.dtypes)

#merging
df = df.merge(panama_df, on='Year', how='outer')
print(df.head())

#what about the historical level of monthly global data traffic?
data_traffic_df = pd.read_csv('/Users/erikrice/Downloads/Monthly Global Data Traffic - Sheet1.csv')
print(data_traffic_df.head())
print(data_traffic_df.dtypes)

#some quick cleanup before merging
data_traffic_df['Year'] = data_traffic_df['Date']
data_traffic_df['Year'] = pd.to_datetime(data_traffic_df.Year, format='%Y')
data_traffic_df = data_traffic_df[['Year', 'Monthly Data Traffic (Exabytes Per Month)']]
print(data_traffic_df.dtypes)

#merging into macro df
df = df.merge(data_traffic_df, on='Year', how='outer')
print(df.head())

#what about total used capacity of international internet bandwidth? importing the data
bandwidth_df = pd.read_csv('/Users/erikrice/Downloads/Total Used Capacity of International Internet Bandwidth - Sheet1.csv')
print(bandwidth_df.head())
print(bandwidth_df.dtypes)

#quick clean and then into the main dataframe
bandwidth_df['Year'] = pd.to_datetime(bandwidth_df.Year, format='%Y')
print(bandwidth_df.dtypes)

#merging
df = df.merge(bandwidth_df, on='Year', how='outer')
print(df)

#what about the total number of international migrants?
migrants_df = pd.read_csv('/Users/erikrice/Downloads/International Migrants Data - Sheet1.csv')
print(migrants_df.head())
print(migrants_df.dtypes)

#cleaning data for merge
migrants_df['Year'] = pd.to_datetime(migrants_df.Year, format='%Y')
print(migrants_df.dtypes)

#merging
df = df.merge(migrants_df, on='Year', how='outer')
print(df)

#let's look at some of these indicators on the same chart. currency (in billions) first
sns.set_palette('Accent')
fig, ax = plt.subplots(figsize=(20, 5))
sns.lineplot(data=df, x='Year', y='FDI (in Billions of USD)', label='Foreign Direct Investment')
sns.lineplot(data=df, x='Year', y='Exports (in Billions of USD)', label='Exports')
sns.lineplot(data=df, x='Year', y='Imports (in Billions of USD)', label='Imports')
sns.lineplot(data=df, x='Year', y='Tourism Spneding (USD in Billions)', label='Tourism Spending').set(title='Various Global Trade Spending Over Time', xlabel='Year', ylabel='USD (in Billions)')
plt.show()

#grouped bar graph for above information also created in different program for quality purposes 

#what about proportional GDP data?
sns.set_palette('Dark2')
fig = plt.subplots(figsize=(20, 5))
sns.lineplot(data=df, x='Year', y='Trade (% of GDP)', label='Trade (Goods/Services)')
sns.lineplot(data=df, x='Year', y='Merchandise Trade (% of GDP)', label='Merchandise Trade')
sns.lineplot(data=df, x='Year', y='Services (% of GDP)', label='Trade in Services')
sns.lineplot(data=df, x='Year', y='Exports (% of GDP)', label='Exports')
sns.lineplot(data=df, x='Year', y='Imports (% of GDP)', label='Imports')
sns.lineplot(data=df, x='Year', y='FDI (% of GDP)', label='Foreign Direct Investment').set(title='Various Global Trade Indicator to GDP Ratio', xlabel='Year', ylabel='% of GDP')
plt.show()

#we can get servicable scatterplots and heatmaps in pythoh. let's take a look. verifying data types first
print(df.dtypes)
df[['Merchandise Trade (% of GDP)', 'Services (% of GDP)', 'Digital Trade (USD in Millions)']] = df[['Merchandise Trade (% of GDP)', 'Services (% of GDP)', 'Digital Trade (USD in Millions)']].astype(float)
print(df.dtypes)

#let's take a look at the broad correlation picture
sns.heatmap(df.corr(), annot=True, cmap="YlGnBu")
plt.show()

#time to look at some scatterplots. first, let's peek at trade to world GDP and RTA agreements
sns.set_palette('YlOrRd_d')
sns.relplot(data=df, x='Trade (% of GDP)', y='Active RTAs', kind='scatter')
plt.xlabel('Trade (% of GDP)')
plt.ylabel('Cummulative Regional Trade Agreements')
plt.title('Trade to World GDP as a Function of Active RTAs')
plt.show()

#what about FDI and merchandise trade?
sns.set_palette('YlOrBr_d')
sns.relplot(data=df, x='FDI (in Billions of USD)', y='Merchandise Trade (% of GDP)', kind='scatter')
plt.xlabel('Foreign Direct Investment (USD in Billions)')
plt.ylabel('Merchandise Trade (% of GDP)')
plt.title('Global FDI as a Function of Merchandise Trade to GDP')
plt.show()

#what about FDI and trade in services?
sns.set_palette('YlGnBu_d')
sns.relplot(data=df, x='FDI (in Billions of USD)', y='Services (% of GDP)', kind='scatter')
plt.xlabel('Foreign Direct Investment (USD in Billions)')
plt.ylabel('Trade in Services (% of GDP)')
plt.title('Global FDI as a Function of Services Trade to GDP')
plt.show()

#what about exports and tourism?
sns.set_palette('YlGn_d')
sns.relplot(data=df, x='Exports (in Billions of USD)', y='Tourism Spneding (USD in Billions)', kind='scatter')
plt.xlabel('Exports (USD in Billions)')
plt.ylabel('Tourism Spending (USD in Billions)')
plt.title('Global Exports as a Function of Tourism Spending')
plt.show()

#what about exports and RTAs?
sns.set_palette('Reds_d')
sns.relplot(data=df, x='Exports (in Billions of USD)', y='Active RTAs', kind='scatter')
plt.xlabel('Exports (USD in Billions)')
plt.ylabel('Cummulative Regional Trade Agreements')
plt.title('Global Exports as a Function of Active RTAs')
plt.show()

#what about tariff rates over time?
sns.set_palette('RdPu_d')
sns.relplot(data=df, x='Mean World Tariff Rate', y='Year')
plt.xlabel('Mean Global Tariff Rate')
plt.ylabel('Year')
plt.title('Global Average Tariff Rate as a Function of Time')
plt.show()

#what about tourism and digital trade?
sns.set_palette('Purples_d')
sns.relplot(data=df, x='Tourism Spneding (USD in Billions)', y='Digital Trade (USD in Millions)', kind='scatter')
plt.xlabel('Tourism Spending (USD in Billions)')
plt.ylabel('Digital Trade (USD in Millions)')
plt.title('Global Tourism Spending as a Function of Digital Trade')
plt.show()

#what about tourism and RTAs?
sns.set_palette('PuRd_d')
sns.relplot(data=df, x='Tourism Spneding (USD in Billions)', y='Active RTAs', kind='scatter')
plt.xlabel('Tourism Spending (USD in Billions)')
plt.ylabel('Cummulative Regional Trade Agreements')
plt.title('Global Tourism Spending as a Function of Active RTAs')
plt.show()

#what about services and exports?
sns.set_palette('PuBuGn_d')
sns.relplot(data=df, x='Services (% of GDP)', y='Exports (in Billions of USD)', kind='scatter')
plt.xlabel('Trade in Services (% of GDP)')
plt.ylabel('Exports (USD in Billions)')
plt.title('Global Trade in Services as a Function of Exports')
plt.show()

#finally, what about RTAs and digital trade?
sns.set_palette('PuBu_d')
sns.relplot(data=df, x='Active RTAs', y='Digital Trade (USD in Millions)', kind='scatter')
plt.xlabel('Cummulative Regional Trade Agreements')
plt.ylabel('Digital Trade (USD in Millions)')
plt.title('Global Active RTAs as a Function of Digital Trade')
plt.show()

#some excellent pie, donut, stacked bar and waterfall charts created for the above data as well in other programs. looks better there - on site. 

#exporting macro df for said visuals
df.to_csv('/Users/erikrice/Downloads/Globalization Part 1 df.csv')