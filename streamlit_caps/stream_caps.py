# Mengimpor modul-modul yang dibutuhkan
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from PIL import Image

st.set_page_config(
    page_title = 'Belajar Streamlit',
    layout='wide'
)

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

image = Image.open('dataset_caps/crime2.jpg')
st.image(image, caption='', use_column_width=True)

# ---------------------------------------------------------------

# Sidebar Content
stringInfo1 = '''
            ### Dataset 
            
           Dataset yang digunakan dalam artikel ini bersumber dari :
            
            1. [Data.gov - Crime Data from 2020 to Present](https://catalog.data.gov/dataset/crime-data-from-2020-to-present)
            
            2. [LA City - Crime Data](https://data.lacity.org/Public-Safety/Crime-Data-from-2020-to-Present/2nrs-mtv8/about_data)
            '''
st.sidebar.info(stringInfo1)

stringInfo2 = '''
            **Penjelasan Mengenai Dataset Tindak Kejahatan**
            
            Kumpulan data ini mencerminkan insiden kejahatan di Kota Los Angeles sejak tahun 2020 hingga saat ini. 
            Data ini ditranskrip dari laporan kejahatan asli yang diketik di atas kertas dan oleh karena itu 
            mungkin ada beberapa ketidakakuratan dalam data. Beberapa bidang lokasi dengan data yang hilang 
            dicatat sebagai (0°, 0°). Kolom alamat hanya disediakan hingga seratus blok terdekat untuk menjaga privasi. 
            Data ini seakurat data yang ada di database.
            '''
st.sidebar.info(stringInfo2)

stringInfoAuthor = '''
            **Kontak Saya:**
            
            📬 syarifudinjaelani@gmail.com\n
            📲 [LinkedIn](https://www.linkedin.com/in/syarifudin-jaelani-b956761b3/)\n
            📰 [Medium](https://medium.com/@syarifudinjaelani)\n
            📑 [GitHub](https://github.com/RIFF7)\n
            🧾 [Instagram](https://www.instagram.com/paper.curt/)
            '''
st.sidebar.info(stringInfoAuthor)

# Penjelasan Singkat Mengenai Tidak Kejahatan
string1 = '''
         Dalam era digital yang terus berkembang, analisis data telah menjadi salah satu alat yang paling kuat dalam memahami dan mengatasi tantangan keamanan masyarakat. Dengan adanya akses terhadap dataset kriminalitas yang kaya informasi, kita dapat mengeksplorasi pola-pola yang tersembunyi dan mendapatkan wawasan yang berharga untuk meningkatkan efektivitas penegakan hukum serta keamanan masyarakat.\n
         Artikel ini mengusung tujuan untuk memberikan pandangan mendalam terhadap tren dan pola kejahatan yang terjadi sejak tahun 2020 hingga saat ini. Dataset yang digunakan merupakan kumpulan data laporan kejahatan yang mencakup beragam informasi, mulai dari tanggal kejadian, lokasi, hingga deskripsi kejahatan. Analisis yang dilakukan tidak hanya sekedar mencari statistik umum, tetapi juga mencoba untuk melihat lebih jauh, mengidentifikasi pola yang mungkin tidak terlihat pada pandangan pertama.\n
         Melalui artikel ini, penulis akan memperkenalkan pembaca pada hasil analisis mendalam terhadap beberapa variabel kunci seperti nomor laporan, tanggal pelaporan, lokasi kejadian, jenis kejahatan, serta karakteristik korban dan status laporan. Semua informasi yang disajikan berdasarkan data aktual yang telah dipersiapkan dan diolah sebelumnya, memberikan keandalan dan keakuratan yang diperlukan dalam mengambil kesimpulan.\n
         Diharapkan artikel ini tidak hanya memberikan wawasan baru tentang kejahatan yang terjadi di komunitas kita, tetapi juga menjadi landasan untuk kebijakan dan langkah-langkah yang lebih efektif dalam mencegah dan menanggulangi kejahatan. Mari kita bersama-sama menjelajahi dunia kejahatan melalui lensa data, untuk menciptakan lingkungan yang lebih aman bagi kita semua.
         '''
st.write(string1)

# ---------------------------------------------------------------

# Menampilkan judul dengan fungsi st.title()
st.title('Analisa Tren Waktu Kejahatan')

# Import Dataset
data_year = pd.read_csv('dataset_caps/yearly_report_count.csv')

# ---------------------------------------------------------------