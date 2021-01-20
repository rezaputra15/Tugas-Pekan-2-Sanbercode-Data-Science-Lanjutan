import csv, pandas as pd
import matplotlib.pyplot as plt

class tugas:
    def __init__(self, data):
        self.data = data

    def proses (self):
        df = pd.read_csv(self.data)
        
        gdp = df[['Country Name', 'Indicator Code', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011']].copy()
        gdp.rename(columns = {'Country Name' : 'Nama', 'Indicator Code': 'Kode_Indikator'}, inplace = True)
        gdp = gdp[gdp.Kode_Indikator == 'NA.GDP.EXC.OG.CR']
        gdp = gdp[gdp["Nama"].isin(["Bandung Barat, Kab.", "Bandung, Kab.", "Cimahi, Kota", "Bandung, Kota"])]
        gdp = gdp.drop(columns=['Kode_Indikator'])
        gdp = gdp.fillna(0)
        
        # gdp['2001'] = gdp['2001'].apply(lambda x: (x - df['2001'].min()) / (df['2001'].max() - df['2001'].min()))
        # gdp['2002'] = gdp['2002'].apply(lambda x: (x - df['2002'].min()) / (df['2002'].max() - df['2002'].min()))
        # gdp['2003'] = gdp['2003'].apply(lambda x: (x - df['2003'].min()) / (df['2003'].max() - df['2003'].min()))
        # gdp['2004'] = gdp['2004'].apply(lambda x: (x - df['2004'].min()) / (df['2004'].max() - df['2004'].min()))
        # gdp['2005'] = gdp['2005'].apply(lambda x: (x - df['2005'].min()) / (df['2005'].max() - df['2005'].min()))
        # gdp['2006'] = gdp['2006'].apply(lambda x: (x - df['2006'].min()) / (df['2006'].max() - df['2006'].min()))
        # gdp['2007'] = gdp['2007'].apply(lambda x: (x - df['2007'].min()) / (df['2007'].max() - df['2007'].min()))
        # gdp['2008'] = gdp['2008'].apply(lambda x: (x - df['2008'].min()) / (df['2008'].max() - df['2008'].min()))
        # gdp['2009'] = gdp['2009'].apply(lambda x: (x - df['2009'].min()) / (df['2009'].max() - df['2009'].min()))
        # gdp['2010'] = gdp['2010'].apply(lambda x: (x - df['2010'].min()) / (df['2010'].max() - df['2010'].min()))
        # gdp['2011'] = gdp['2011'].apply(lambda x: (x - df['2011'].min()) / (df['2011'].max() - df['2011'].min()))  
        
        gdp = pd.melt(gdp, id_vars=['Nama'], value_vars=['2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011'], var_name='Tahun', value_name='Nilai GDP Tanpa Migas')
        gdp = gdp.pivot(index='Tahun', columns='Nama', values='Nilai GDP Tanpa Migas').reset_index()
        gdp.rename(columns = {'Bandung Barat, Kab.' : 'Kab. Bandung Barat', 'Bandung, Kab.': 'Kab. Bandung', 'Bandung, Kota': 'Kota Bandung', 'Cimahi, Kota': 'Kota Cimahi'}, inplace = True)
        
        plt.figure(figsize=(15,10))
        ax = plt.gca()
        gdp.plot(kind='line',x='Tahun',y='Kab. Bandung Barat', marker = 'p', ax=ax)
        gdp.plot(kind='line',x='Tahun',y='Kab. Bandung', color = 'red', marker = 'D', ax=ax)
        gdp.plot(kind='line',x='Tahun',y='Kota Bandung', color = 'green', marker = '*', ax=ax)
        gdp.plot(kind='line',x='Tahun',y='Kota Cimahi', color = 'orange', marker = '.', ax=ax)

        plt.title('GDP Tanpa Migas')
        plt.xlabel('Tahun')
        plt.ylabel('Nilai GDP')
        plt.show()

data = r"INDODAPOERData.csv"

hasil = tugas(data)
hasil.proses()