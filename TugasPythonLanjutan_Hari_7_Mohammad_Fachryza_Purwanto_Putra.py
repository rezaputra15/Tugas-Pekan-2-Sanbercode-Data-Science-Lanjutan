import sqlite3
import pandas as pd

conn = sqlite3.connect('fachreyzaputra.db')  
c = conn.cursor()

read_pulau = pd.read_csv (r'pulau_indonesia.csv').fillna(0)
read_pulau.rename(columns = {'Provini':'Provinsi', 'Pulau Bernama':'Pulau_Bernama', 'Pulau Tak Bernama':'Pulau_Tak_Bernama'}, inplace = True)

create_table = """CREATE TABLE IF NOT EXISTS Pulau(
   No INT PRIMARY KEY,
   Provinsi TEXT,
   Pulau_Bernama INT,
   Pulau_Tak_Bernama INT,
   Total INT);"""
c.execute(create_table)

# Insert the values from the csv file into the table 'Pulau' 
read_pulau.to_sql('Pulau', conn, if_exists='append', index = False) 

pilih = '''SELECT * FROM Pulau'''  
c.execute(pilih)
conn.commit()

all_results = c.fetchall()
print(all_results)
c.close()
conn.close()