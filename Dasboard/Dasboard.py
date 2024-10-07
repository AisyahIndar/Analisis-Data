import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Judul aplikasi
st.title("Dashboard Analisis Penyewaan Sepeda Tahun 2011-2012")

# Membaca dataset
data = pd.read_csv('main_data.csv')

# --- Visualisasi Penyewaan Berdasarkan Tahun ---
st.subheader("Jumlah Penyewaan Sepeda Berdasarkan Tahun")
Yearly_counts = pd.DataFrame({
    'year': [2011, 2012],
    'cnt': [2409500, 3202576]
})
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x='year', y='cnt', data=Yearly_counts, palette="magma", ax=ax)
ax.set_title("Jumlah Penyewaan Sepeda Berdasarkan Tahun", fontsize=16)
ax.set_xlabel("Tahun", fontsize=14)
ax.set_ylabel("Jumlah Penyewaan Sepeda", fontsize=14)
plt.tight_layout()
st.pyplot(fig)

# --- Visualisasi Penyewaan Berdasarkan Bulan (Bar Plot untuk 2011 dan 2012) ---
st.subheader("Jumlah Penyewaan Sepeda Berdasarkan Bulan")
if 'mnth' in data.columns and 'cnt' in data.columns and 'yr' in data.columns:
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Filter data untuk tahun 2011 dan 2012
    data_2011 = data[data['yr'] == 0]  # Tahun 2011 (yr=0)
    data_2012 = data[data['yr'] == 1]  # Tahun 2012 (yr=1)

    # Agregasi penyewaan per bulan untuk setiap tahun
    mnth_counts_2011 = data_2011.groupby('mnth')['cnt'].sum().reset_index()
    mnth_counts_2012 = data_2012.groupby('mnth')['cnt'].sum().reset_index()

    # Gabungkan kedua dataset berdasarkan bulan untuk visualisasi bar terpisah
    mnth_counts_2011['year'] = 2011
    mnth_counts_2012['year'] = 2012
    combined_mnth_counts = pd.concat([mnth_counts_2011, mnth_counts_2012])

    # Plot bar terpisah untuk 2011 dan 2012
    sns.barplot(x='mnth', y='cnt', hue='year', data=combined_mnth_counts, palette='Set2', dodge=True, ax=ax)
    
    ax.set_title("Jumlah Penyewaan Sepeda Berdasarkan Bulan", fontsize=16)
    plt.xticks(ticks=range(12), labels=['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul','Agst', 'Sept', 'Okt', 'Nov', 'Des'])
    ax.set_xlabel("Bulan", fontsize=14)
    ax.set_ylabel("Jumlah Penyewaan Sepeda", fontsize=14)
    plt.tight_layout()
    st.pyplot(fig)
else:
    st.error("Kolom 'mnth', 'cnt', dan 'yr' tidak ditemukan dalam dataset.")

# --- Visualisasi Penyewaan Berdasarkan Hari (Line-Bar Plot) ---
st.subheader("Jumlah Penyewaan Sepeda Berdasarkan Hari dalam Minggu")
if 'weekday' in data.columns and 'cnt' in data.columns and 'yr' in data.columns:
    # Mengganti nilai yr dengan label tahun
    data['Tahun'] = data['yr'].replace({0: 2011, 1: 2012})
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Line-bar plot berdasarkan hari dalam minggu, dibedakan per tahun
    sns.lineplot(x='weekday', y='cnt', hue='Tahun', data=data, marker='o', ax=ax, palette='Set1')
    
    ax.set_title("Jumlah Penyewaan Sepeda Berdasarkan Hari dalam Minggu", fontsize=16)
    ax.set_xlabel("Hari dalam Minggu", fontsize=14)
    ax.set_ylabel("Jumlah Penyewaan Sepeda", fontsize=14)
    plt.xticks(ticks=range(7), labels=['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu'])
    plt.tight_layout()
    st.pyplot(fig)
else:
    st.error("Kolom 'weekday', 'cnt', dan 'yr' tidak ditemukan dalam dataset.")

# --- Visualisasi Penyewaan Berdasarkan Jam ---
st.subheader("Jumlah Penyewaan Sepeda Berdasarkan Jam")
if 'hr' in data.columns and 'cnt' in data.columns:
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Plot penyewaan sepeda berdasarkan jam (bar plot)
    sns.barplot(x='hr', y='cnt', data=data, palette='Blues_d', ax=ax)
    
    ax.set_title("Jumlah Penyewaan Sepeda Berdasarkan Jam", fontsize=16)
    ax.set_xlabel("Jam", fontsize=14)
    ax.set_ylabel("Jumlah Penyewaan Sepeda", fontsize=14)
    plt.tight_layout()
    st.pyplot(fig)
else:
    st.error("Kolom 'hr' dan 'cnt' tidak ditemukan dalam dataset.")

# --- Visualisasi Penyewaan Berdasarkan Kondisi Cuaca ---
weather_counts_2011 = pd.DataFrame({
    'weathersit': ['Cerah', 'Berawan', 'Hujan/Salju Sedikit', 'Hujan/Salju Lebat'],
    'cnt': [875053, 300519, 67495, 36]
})
weather_counts_2012 = pd.DataFrame({
    'weathersit': ['Cerah', 'Berawan', 'Hujan/Salju Sedikit', 'Hujan/Salju Lebat'],
    'cnt': [1463120, 495433, 90836, 187]
})
weather_counts_2011['year'] = 2011
weather_counts_2012['year'] = 2012
combined_weather_counts = pd.concat([weather_counts_2011, weather_counts_2012], ignore_index=True)

st.subheader("Jumlah Penyewaan Sepeda Berdasarkan Kondisi Cuaca")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='weathersit', y='cnt', hue='year', data=combined_weather_counts, palette="coolwarm", ax=ax)
ax.set_title("Jumlah Penyewaan Sepeda Berdasarkan Kondisi Cuaca", fontsize=16)
ax.set_xlabel("Kondisi Cuaca", fontsize=14)
ax.set_ylabel("Jumlah Penyewaan Sepeda", fontsize=14)
ax.grid(axis='y')
ax.legend(title='Tahun')
plt.tight_layout()
st.pyplot(fig)

# --- Visualisasi Penyewaan Berdasarkan Musim ---
season_counts_2011 = pd.DataFrame({
    'season': ['Musim Hujan', 'Musim Panas', 'Musim Dingin', 'Musim Semi'],
    'cnt': [419650, 347316, 326137, 150000]
})
season_counts_2012 = pd.DataFrame({
    'season': ['Musim Hujan', 'Musim Panas', 'Musim Dingin', 'Musim Semi'],
    'cnt': [641479, 571273, 515476, 321348]
})
season_counts_2011['year'] = 2011
season_counts_2012['year'] = 2012
combined_season_counts = pd.concat([season_counts_2011, season_counts_2012], ignore_index=True)

st.subheader("Jumlah Penyewaan Sepeda Berdasarkan Musim")
fig, ax = plt.subplots(figsize=(10, 6))
bar_plot = sns.barplot(x='season', y='cnt', hue='year', data=combined_season_counts, palette="Set2", ax=ax)
for i, bar in enumerate(bar_plot.patches):
    if i % 2 == 0:
        bar.set_hatch('///')
    else:
        bar.set_hatch('\\\\')
ax.set_title("Jumlah Penyewaan Sepeda Berdasarkan Musim", fontsize=16)
ax.set_xlabel("Musim", fontsize=14)
ax.set_ylabel("Jumlah Penyewaan Sepeda", fontsize=14)
ax.grid(axis='y')
ax.legend(title='Tahun')
plt.tight_layout()
st.pyplot(fig)

# Menyimpulkan analisis
st.subheader("Kesimpulan")
st.markdown("""
Dari analisis yang telah dilakukan, kita dapat menyimpulkan beberapa hal sebagai insight dari analisis ini, yaitu :
- Terjadi peningkatan penyewaan sepeda yang signifikan dari Tahun 2011 ke Tahun 2012
- Di Tahun 2011 puncak penyewaan terjadi pada saat Musim Hujan, Kondisi Cuaca Cerah, di Bulan Juni, Hari Jumat dan Jam 17.00-18.00 di sore hari serta di jam 08.00 dipagi hari. 
- Sedangkan di Tahun 2011 puncak penyewaan terjadi pada saat Musim Hujan, Kondisi Cuaca Cerah, di Bulan September, Hari Kamis dan Jam 17.00-18.00 di sore hari serta di jam 08.00 dipagi hari. 
""")


