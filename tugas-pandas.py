import pandas as pd

#1
df_sampah = pd.read_excel('disperkim-od_16985_jumlah_produksi_sampah_berdasarkan_kabupatenkota_v3_data.xlsx', sheet_name='dataframe')
print(df_sampah)

#2
sum = 0 

for i, row in df_sampah.iterrows():
    if row["Tahun"] == 2015:
        sum += row["Jumlah Produksi Sampah (dalam ton)"]

print(f"Total produksi sampah pada tahun 2015: {sum:.2f} ton")

#3
totalpertahun = {}

for i, row in df_sampah.iterrows():
    tahun = row['Tahun']
    berat = row["Jumlah Produksi Sampah (dalam ton)"]
    
    if tahun in totalpertahun:
        totalpertahun[tahun] += berat
    else:
        totalpertahun[tahun] = berat

for tahun, total in totalpertahun.items():
    print(f"Total sampah di {tahun} adalah {total:.2f}")

#4
totalperkotkab = {}

for i, row in df_sampah.iterrows():
    tahun = row['Tahun']
    berat = row["Jumlah Produksi Sampah (dalam ton)"]
    kota_kab = row["Kabupaten/Kota"]
    
    key = (kota_kab,tahun)

    if key in totalperkotkab:
        totalperkotkab[key] += berat
    else:
        totalperkotkab[key] = berat

for (kota_kab,tahun), total in totalperkotkab.items():
    print(f"Total sampah di {kota_kab} pada tahun {tahun} adalah {total:.2f}")

#export dataframe ke .csv dan .xlsx
df_sampah.to_csv('dataframe.csv', index=False)
df_sampah.to_excel('dataframe.xlsx', index=False)



