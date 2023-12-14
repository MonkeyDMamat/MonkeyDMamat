import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.dates import DateFormatter
from babel.numbers import format_currency

# Mendefinisikan DataFrame day_df dan hour_df
url_day = "https://raw.githubusercontent.com/MonkeyDMamat/MonkeyDMamat/master/submission/data/day.csv"
url_hour = "https://raw.githubusercontent.com/MonkeyDMamat/MonkeyDMamat/master/submission/data/hour.csv"
day_df = pd.read_csv(url_day)
hour_df = pd.read_csv(url_hour)

# Set judul dashboard
st.title("Bike Sharing Data Analysis Dashboard")

# Menampilkan data
if st.checkbox("Tampilkan Data Hari"):
    st.write("### Data Hari")
    st.dataframe(day_df.head())

if st.checkbox("Tampilkan Data Jam"):
    st.write("### Data Jam")
    st.dataframe(hour_df.head())

# Menampilkan ringkasan statistik
if st.checkbox("Tampilkan Statistik Hari"):
    st.write("### Statistik Hari")
    st.write(day_df.describe())

if st.checkbox("Tampilkan Statistik Jam"):
    st.write("### Statistik Jam")
    st.write(hour_df.describe())

# Visualisasi untuk pertanyaan bisnis
# Pertanyaan 1: Bagaimana jumlah pengguna sepeda harian dipengaruhi oleh faktor-faktor seperti cuaca dan hari kerja?
st.subheader("Pertanyaan 1: Jumlah Pengguna Sepeda Harian dan Faktor-Faktor Pengaruhnya")
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Visualisasi 2: Jumlah pengguna sepeda harian berdasarkan hari kerja atau tidak
sns.boxplot(x='workingday', y='cnt', data=day_df, ax=axes[0, 1])
axes[0, 1].set_title('Jumlah Pengguna Sepeda Harian Berdasarkan Hari Kerja')

# Visualisasi 3: Distribusi jumlah pengguna sepeda harian pada jam tertentu
sns.lineplot(x='hr', y='cnt', data=hour_df, hue='workingday', ci=None, ax=axes[1, 0])
axes[1, 0].set_title('Distribusi Jumlah Pengguna Sepeda Harian pada Jam Tertentu (Hari Kerja vs. Libur)')

# Visualisasi 4: Pengaruh suhu dan kelembaban terhadap jumlah pengguna sepeda
sns.scatterplot(x='temp', y='cnt', hue='hum', size='hum', data=day_df, ax=axes[1, 1])
axes[1, 1].set_title('Pengaruh Suhu dan Kelembaban terhadap Jumlah Pengguna Sepeda')

plt.tight_layout()
st.pyplot()

# Pertanyaan 2: Apakah suhu dan kelembaban memiliki pengaruh pada penggunaan sepeda?
st.subheader("Pertanyaan 2: Pengaruh Suhu dan Kelembaban pada Penggunaan Sepeda")
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Visualisasi 1: Distribusi jumlah pengguna sepeda berdasarkan suhu
sns.histplot(day_df['temp'], bins=30, kde=True, ax=axes[0])
axes[0].set_title('Distribusi Jumlah Pengguna Sepeda Berdasarkan Suhu')

# Visualisasi 2: Distribusi jumlah pengguna sepeda berdasarkan kelembaban
sns.histplot(day_df['hum'], bins=30, kde=True, ax=axes[1])
axes[1].set_title('Distribusi Jumlah Pengguna Sepeda Berdasarkan Kelembaban')

plt.tight_layout()
st.pyplot()

# Pertanyaan 3: Bagaimana faktor cuaca mempengaruhi penggunaan sepeda pada level jam dalam sehari?
st.subheader("Pertanyaan 3: Pengaruh Faktor Cuaca pada Penggunaan Sepeda pada Level Jam")
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Visualisasi 1: Distribusi jumlah pengguna sepeda pada jam tertentu berdasarkan cuaca
sns.lineplot(x='hr', y='cnt', data=hour_df, hue='weathersit', ci=None, ax=axes[0])
axes[0].set_title('Distribusi Jumlah Pengguna Sepeda pada Jam Tertentu (Berdasarkan Cuaca)')

# Visualisasi 2: Boxplot jumlah pengguna sepeda pada jam tertentu berdasarkan cuaca
sns.boxplot(x='hr', y='cnt', data=hour_df, hue='weathersit', ax=axes[1])
axes[1].set_title('Boxplot Jumlah Pengguna Sepeda pada Jam Tertentu (Berdasarkan Cuaca)')

plt.tight_layout()
st.pyplot()

# Pertanyaan 4: Apakah terdapat perbedaan dalam penggunaan sepeda antara hari kerja dan hari libur pada jam-jam tertentu?
st.subheader("Pertanyaan 4: Perbedaan Penggunaan Sepeda antara Hari Kerja dan Hari Libur")
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Visualisasi 1: Distribusi jumlah pengguna sepeda pada jam tertentu berdasarkan hari kerja atau libur
sns.lineplot(x='hr', y='cnt', data=hour_df, hue='workingday', ci=None, ax=axes[0])
axes[0].set_title('Distribusi Jumlah Pengguna Sepeda pada Jam Tertentu (Hari Kerja vs. Libur)')

# Visualisasi 2: Boxplot jumlah pengguna sepeda pada jam tertentu berdasarkan hari kerja atau libur
sns.boxplot(x='hr', y='cnt', data=hour_df, hue='workingday', ax=axes[1])
axes[1].set_title('Boxplot Jumlah Pengguna Sepeda pada Jam Tertentu (Hari Kerja vs. Libur)')

plt.tight_layout()
st.pyplot()

# Menyimpan hasil analisis
st.sidebar.subheader("Kesimpulan")
st.sidebar.text("Penggunaan sepeda harian dipengaruhi oleh faktor hari kerja, suhu, dan cuaca. Suhu dan kelembaban tampaknya memiliki pengaruh yang signifikan pada penggunaan sepeda. Faktor cuaca, seperti hari yang cerah atau berawan, dapat memengaruhi pola penggunaan sepeda pada jam tertentu. Perbedaan signifikan terlihat antara hari kerja dan libur dalam hal pola penggunaan sepeda.")

# Menyajikan dashboard
st.set_option('deprecation.showPyplotGlobalUse', False)  # Agar matplotlib tidak menampilkan pesan peringatan
