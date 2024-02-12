# Mengimpor modul-modul yang dibutuhkan
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from PIL import Image

# Mengatur tata letak judul ke tengah dengan CSS
st.markdown(
    f"""
    <style>
        .reportview-container .main .block-container{{
            max-width: 1000px;
            padding-top: 5rem;
            padding-right: 3rem;
            padding-left: 3rem;
            padding-bottom: 5rem;
        }}
        h1 {{
            text-align: center;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Menampilkan judul dengan fungsi st.title()
st.title('Analisa Kasus Kejahatan Pada Negara US (Los Angeles)')

# Tag Penulis
stringHeader = 'Penulis : **Syarifudin Jaelani**'
st.markdown(stringHeader)

image = Image.open('dataset_caps/crime1.jpg')
st.image(image, caption='')

# ---------------------------------------------------------------

# Sidebar Content
stringInfo1 = '''
            ### Dataset 
            
           Dataset yang digunakan dalam artikel ini bersumber dari :
            
            1. [Data.gov - Crime Data from 2020 to Present](https://catalog.data.gov/dataset/crime-data-from-2020-to-present)
            
            2. [LA City - Crime Data](https://data.lacity.org/browse)
            '''
st.sidebar.info(stringInfo1)

stringInfo2 = '''
            **Penjelasan Mengenai Dataset Tindak Kejahatan**
            
            Prosess....
            '''
st.sidebar.info(stringInfo2)

stringInfoAuthor = '''
            **Syarifudin Jaelani**
            
            Prosesss....           
            '''
st.sidebar.info(stringInfoAuthor)

# Penjelasan Singkat Mengenai Tidak Kejahatan
string1 = '''
         Prosess....
         '''
st.write(string1)

# ---------------------------------------------------------------

# Menampilkan judul dengan fungsi st.title()
st.title('Analisa Tren Waktu Kejahatan')

# Import Dataset
data_year = pd.read_csv('dataset_caps/yearly_report_count.csv')

# Buat daftar tahun unik
tahun_unik = list(data_year['Year_Occ'].unique())

# Buat pilihan dropdown untuk tahun pertama
tahun_pertama = st.selectbox('Pilih Tahun Pertama:', tahun_unik)

# Buat pilihan dropdown untuk tahun kedua
tahun_kedua = st.selectbox('Pilih Tahun Kedua:', tahun_unik)

# Filter data berdasarkan tahun yang dipilih
df_filtered1 = data_year[data_year['Year_Occ'] == tahun_pertama]
df_filtered2 = data_year[data_year['Year_Occ'] == tahun_kedua]

# Buat plot dengan Altair untuk perbandingan antara tahun pertama dan tahun kedua
chart = alt.Chart(df_filtered1).mark_line().encode(
    x=alt.X('Month_Occ', title='Bulan'),
    y=alt.Y('Jml_Kejahatan', title='Jumlah Kejahatan'),
    color=alt.value('blue'),
    tooltip=['Year_Occ:N', 'Jml_Kejahatan:Q']  # Menambahkan tooltip untuk tahun dan jumlah kejahatan
).properties(
    width=600,
    height=400
)

chart += alt.Chart(df_filtered2).mark_line().encode(
    x=alt.X('Month_Occ', title='Bulan'),
    y=alt.Y('Jml_Kejahatan', title='Jumlah Kejahatan'),
    color=alt.value('red'),
    tooltip=['Year_Occ:N', 'Jml_Kejahatan:Q']  # Menambahkan tooltip untuk tahun dan jumlah kejahatan
)

# Tambahkan titik pada setiap lekukan grafik
chart += alt.Chart(df_filtered1).mark_circle(color='blue').encode(
    x=alt.X('Month_Occ', title='Bulan'),
    y=alt.Y('Jml_Kejahatan', title='Jumlah Kejahatan'),
    tooltip=['Year_Occ:N', 'Jml_Kejahatan:Q']  # Menambahkan tooltip untuk tahun
)

chart += alt.Chart(df_filtered2).mark_circle(color='red').encode(
    x=alt.X('Month_Occ', title='Bulan'),
    y=alt.Y('Jml_Kejahatan', title='Jumlah Kejahatan'),
    tooltip=['Year_Occ:N', 'Jml_Kejahatan:Q']  # Menambahkan tooltip untuk tahun
)

# Tampilkan plot menggunakan Streamlit
st.altair_chart(chart, use_container_width=True)

# ---------------------------------------------------------------