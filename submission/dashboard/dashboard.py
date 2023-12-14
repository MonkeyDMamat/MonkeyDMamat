import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.dates import DateFormatter

# Mendefinisikan DataFrame keduanya_df
url_keduanya = "https://raw.githubusercontent.com/MonkeyDMamat/MonkeyDMamat/master/submission/dashboard/keduanya.csv"
keduanya_df = pd.read_csv(url_keduanya)

# Set judul dashboard
st.title("Bike Sharing Data Analysis Dashboard")

# Menampilkan data
if st.checkbox("Tampilkan Data Hari"):
    st.write("### Data Hari")
    st.dataframe(keduanya_df.head())

if st.checkbox("Tampilkan Data Jam"):
    st.write("### Data Jam")
    st.dataframe(keduanya_df.head())

# Menampilkan ringkasan statistik
if st.checkbox("Tampilkan Statistik Hari"):
    st.write("### Statistik Hari")
    st.write(keduanya_df.describe())

if st.checkbox("Tampilkan Statistik Jam"):
    st.write("### Statistik Jam")
    st.write(keduanya_df.describe())

# Visualisasi untuk pertanyaan bisnis
# Pertanyaan 1: Bagaimana jumlah pengguna sepeda harian dipengaruhi oleh faktor-faktor seperti cuaca dan hari kerja?
st.subheader("Pertanyaan 1: Bagaimana jumlah pengguna sepeda harian dipengaruhi oleh faktor-faktor seperti cuaca dan hari kerja?")
plt.figure(figsize=(12, 6))
sns.lineplot(x='dteday', y='cnt', hue='weathersit', data=keduanya_df)
plt.title('Pengaruh Cuaca terhadap Jumlah Peminjaman Sepeda Harian')
plt.xlabel('Tanggal')
plt.ylabel('Jumlah Peminjaman')
plt.show()

plt.tight_layout()
st.pyplot()

# Pertanyaan 2: Apakah suhu dan kelembaban memiliki pengaruh pada penggunaan sepeda?
st.subheader("Pertanyaan 2: Apakah suhu dan kelembaban memiliki pengaruh pada penggunaan sepeda?")
plt.figure(figsize=(12, 6))
sns.scatterplot(x='temp', y='cnt', hue='hum', data=keduanya_df)
plt.title('Pengaruh Suhu dan Kelembaban terhadap Jumlah Peminjaman Sepeda')
plt.xlabel('Suhu')
plt.ylabel('Jumlah Peminjaman')
plt.legend(title='Kelembaban')
plt.show()

plt.tight_layout()
st.pyplot()

# Pertanyaan 3: Bagaimana faktor cuaca mempengaruhi penggunaan sepeda pada level jam dalam sehari?
st.subheader("Pertanyaan 3: Bagaimana faktor cuaca mempengaruhi penggunaan sepeda pada level jam dalam sehari?")
plt.figure(figsize=(12, 6))
sns.lineplot(x='hr', y='cnt', hue='weathersit', data=keduanya_df)
plt.title('Pengaruh Cuaca terhadap Jumlah Peminjaman Sepeda pada Level Jam')
plt.xlabel('Jam')
plt.ylabel('Jumlah Peminjaman')
plt.legend(title='Cuaca')
plt.show()

plt.tight_layout()
st.pyplot()

# Pertanyaan 4: Apakah terdapat perbedaan dalam penggunaan sepeda antara hari kerja dan hari libur pada jam-jam tertentu?
st.subheader("Pertanyaan 4: Apakah terdapat perbedaan dalam penggunaan sepeda antara hari kerja dan hari libur pada jam-jam tertentu?")
plt.figure(figsize=(12, 6))
sns.pointplot(x='hr', y='cnt', hue='workingday', data=keduanya_df, markers=['o', 's'])
plt.title('Perbedaan Penggunaan Sepeda antara Hari Kerja dan Hari Libur pada Level Jam')
plt.xlabel('Jam')
plt.ylabel('Jumlah Peminjaman')
plt.legend(title='Hari Kerja')
plt.show()

plt.tight_layout()
st.pyplot()

# Menyimpan hasil analisis
st.subheader("Kesimpulan")
st.text("Kesimpulan dari Pertanyaan 1 adalah Dari visualisasi, terlihat bahwa penggunaan sepeda harian dipengaruhi oleh cuaca. Pada hari-hari dengan cuaca yang buruk (weathersit tinggi), jumlah peminjaman sepeda cenderung lebih rendah.")

st.subheader("Kesimpulan")
st.text("Kesimpulan dari Pertanyaan 2 adalah Dari scatter plot, terlihat bahwa terdapat hubungan positif antara suhu dan jumlah peminjaman sepeda, namun tidak terlihat pola yang jelas antara kelembaban dan jumlah peminjaman sepeda.")
        
st.subheader("Kesimpulan")
st.text("Kesimpulan dari Pertanyaan 3 adalah Dari line plot, terlihat bahwa cuaca berpengaruh pada jumlah peminjaman sepeda pada berbagai jam dalam sehari. Pada cuaca tertentu, penggunaan sepeda cenderung lebih tinggi atau lebih rendah pada jam-jam tertentu.")

st.subheader("Kesimpulan")
st.text("Kesimpulan dari Pertanyaan 4 adalah Dari point plot, terlihat bahwa terdapat perbedaan pola penggunaan sepeda antara hari kerja dan hari libur pada jam-jam tertentu. Pada hari kerja, peminjaman sepeda cenderung lebih tinggi pada jam-jam tertentu dibandingkan hari libur.")
             
st.sidebar.subheader("Fauzi Ramadhan")
st.sidebar.text ("Portopolio Projects Bike Sharing Data Analysis.")
# Menyajikan dashboard
st.set_option('deprecation.showPyplotGlobalUse', False)  # Agar matplotlib tidak menampilkan pesan peringatan
