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

# image = Image.open('dataset_caps/crime2.jpg')
# st.image(image, caption='', use_column_width=True)

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
            
            Kumpulan data ini mencerminkan insiden kejahatan di Kota Los Angeles sejak tahun 2020 hingga saat ini. Data ini ditranskrip dari laporan kejahatan asli yang diketik di atas kertas dan oleh karena itu mungkin ada beberapa ketidakakuratan dalam data. Beberapa bidang lokasi dengan data yang hilang dicatat sebagai (0°, 0°). Kolom alamat hanya disediakan hingga seratus blok terdekat untuk menjaga privasi. Data ini seakurat data yang ada di database.
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

# Penjelasan Singkat Mengenai Tidak Kriminal
string1 = '''
         Dalam era digital yang terus berkembang, analisis data telah menjadi salah satu alat yang paling kuat dalam memahami dan mengatasi tantangan keamanan masyarakat. Dengan adanya akses terhadap dataset kriminalitas yang kaya informasi, kita dapat mengeksplorasi pola-pola yang tersembunyi dan mendapatkan wawasan yang berharga untuk meningkatkan efektivitas penegakan hukum serta keamanan masyarakat.\n
         
         Artikel ini mengusung tujuan untuk memberikan pandangan mendalam terhadap tren dan pola kriminal yang terjadi sejak tahun 2020 hingga saat ini. Dataset yang digunakan merupakan kumpulan data laporan tindak kriminal yang mencakup beragam informasi, mulai dari tanggal kejadian, lokasi, hingga deskripsi kejahatan. Analisis yang dilakukan tidak hanya sekedar mencari statistik umum, tetapi juga mencoba untuk melihat lebih jauh, mengidentifikasi pola yang mungkin tidak terlihat pada pandangan pertama.\n
         
         Melalui artikel ini, penulis akan memperkenalkan pembaca pada hasil analisis mendalam terhadap beberapa variabel kunci seperti nomor laporan, tanggal pelaporan, lokasi kejadian, jenis kejahatan, serta karakteristik korban dan status laporan. Semua informasi yang disajikan berdasarkan data aktual yang telah dipersiapkan dan diolah sebelumnya, memberikan keandalan dan keakuratan yang diperlukan dalam mengambil kesimpulan.\n
         
         Diharapkan artikel ini tidak hanya memberikan wawasan baru tentang kriminalitas / kejahatan yang terjadi di lingkungan kita, tetapi juga menjadi landasan untuk kebijakan dan langkah-langkah yang lebih efektif dalam mencegah dan menanggulangi tindak kriminal / kejahatan. Mari kita bersama-sama menjelajahi dunia tindak kriminalitas melalui lensa data, untuk menciptakan lingkungan yang lebih aman bagi kita semua.
         '''
st.write(string1)

# Tambahkan garis batas horizontal
st.markdown("---")

# ---------------------------------------------------------------

# Menampilkan judul dengan fungsi st.title()
st.title('Analisa Tren Waktu Kriminal')

# Membuat Columns Grafik
yearLpr_col, monthLpr_col = st.columns(2)
yearOcc_col, monthOcc_col = st.columns(2)

# Membuat Column Analisa
analisa_col1, analisa_col2 = st.columns(2)

# ---------------------------------------------------------------

# Import Dataset
data_yearLpr = pd.read_csv('dataset_caps/yearLpr_report_count.csv')
data_monthLpr = pd.read_csv('dataset_caps/monthLpr_report_count.csv')
data_yearOcc = pd.read_csv('dataset_caps/yearOcc_report_count.csv')
data_monthOcc = pd.read_csv('dataset_caps/monthOcc_report_count.csv')
data_reportLpr = pd.read_csv('dataset_caps/reportLpr_count.csv')

# ---------------------------------------------------------------

with yearLpr_col:
    # Buat plot menggunakan Altair
    chart = alt.Chart(data_yearLpr).mark_line(point=True).encode(
        x=alt.X('Year_Lpr:O', title='Tahun', axis=alt.Axis(labelAngle=0)),
        y=alt.Y('Jml_Kejahatan:Q', title='Jumlah Laporan Kriminalitas'),
        tooltip=['Year_Lpr', 'Jml_Kejahatan']
    ).properties(
        width=600,
        height=400,
        title='Tren Jumlah Laporan Kriminal dari Tahun ke Tahun'
    ).interactive()

    # Tampilkan plot di aplikasi Streamlit
    st.altair_chart(chart, use_container_width=True)

with monthLpr_col:
    # Buat plot menggunakan Altair
    chart = alt.Chart(data_monthLpr).mark_line(point=True).encode(
        x=alt.X('Month_Lpr:O', title='Bulan', axis=alt.Axis(labelAngle=0)),
        y=alt.Y('Jml_Kejahatan:Q', title='Jumlah Laporan Kriminalitas'),
        tooltip=['Month_Lpr', 'Jml_Kejahatan']
    ).properties(
        width=600,
        height=400,
        title='Tren Jumlah Laporan Kriminal dari Bulan ke Bulan'
    ).interactive()

    # Tampilkan plot di aplikasi Streamlit
    st.altair_chart(chart, use_container_width=True)

with yearOcc_col:
    # Buat plot menggunakan Altair
    chart = alt.Chart(data_yearOcc).mark_line(point=True).encode(
        x=alt.X('Year_Occ:O', title='Tahun', axis=alt.Axis(labelAngle=0)),
        y=alt.Y('Jml_Kejahatan:Q', title='Jumlah Laporan Kriminalitas'),
        tooltip=['Year_Occ', 'Jml_Kejahatan']
    ).properties(
        width=600,
        height=400,
        title='Tren Jumlah Kejadian Kriminal dari Tahun ke Tahun'
    ).interactive()

    # Tampilkan plot di aplikasi Streamlit
    st.altair_chart(chart, use_container_width=True)

with monthOcc_col:
    # Buat plot menggunakan Altair
    chart = alt.Chart(data_monthOcc).mark_line(point=True).encode(
        x=alt.X('Month_Occ:O', title='Bulan', axis=alt.Axis(labelAngle=0)),
        y=alt.Y('Jml_Kejahatan:Q', title='Jumlah Laporan Kriminalitas'),
        tooltip=['Month_Occ', 'Jml_Kejahatan']
    ).properties(
        width=600,
        height=400,
        title='Tren Jumlah Kejadian Kriminal dari Bulan ke Bulan'
    ).interactive()

    # Tampilkan plot di aplikasi Streamlit
    st.altair_chart(chart, use_container_width=True)

# Bagian Analisa pada chart
with analisa_col1:
    st.markdown('#### Analisa Tren Tahun Laporan dan Kejadian Kriminal')
    string2 = '''
                1. **Trend Jumlah Tindak Kriminal dari Tahun ke Tahun**: Jumlah tindak kriminal cenderung mengalami penurunan dari tahun 2020 hingga 2024 baik dalam laporan maupun kejadian. Namun, terdapat penurunan yang signifikan dalam jumlah laporan tindak kriminal dari tahun 2023 ke 2024 sebesar **8752** kasus, sementara penurunan dalam jumlah kejadian tindak kriminal tidak sebesar itu hanya diangka **6973**.
                
                2. **Perbandingan antara Laporan dan Kejadian Kriminalitas**: Meskipun terdapat fluktuasi tahunan dalam jumlah laporan dan kejadian kriminal, perbandingan antara jumlah laporan dan kejadian kriminal relatif stabil dari tahun ke tahun. Namun, pada tahun 2024, perbandingan ini menjadi lebih rendah, menunjukkan bahwa lebih sedikit tindak kriminal yang dilaporkan dibandingkan dengan tindak kriminal yang terjadi.
                
                3. **Potensi Penurunan Kualitas Pelaporan**: Penurunan yang signifikan dalam jumlah laporan tindak kriminal pada tahun 2024, sementara jumlah kejadian kriminalitas tidak turun sebanyak itu, mungkin mengindikasikan adanya potensi penurunan kualitas pelaporan atau pelaporan yang kurang akurat pada tahun tersebut.
                
                4. **Faktor Penyebab Penurunan**: Penurunan jumlah laporan tindak kriminal dari tahun 2023 ke 2024 dapat disebabkan oleh berbagai faktor, seperti perubahan kebijakan pelaporan, peningkatan kesadaran masyarakat, atau perubahan dalam aktivitas tindak kriminal sebenarnya.
            '''
    st.write(string2)

with analisa_col2:
    st.markdown('#### Analisa Tren Bulan Laporan dan Kejadian Kriminal')
    string3 = '''
                1. **Trend Bulanan Jumlah Kriminalitas**: Berdasarkan grafik line diatas tidak ada fluktuasi yang signifikan dalam jumlah kriminalitas dari bulan ke bulan. Baik dalam laporan maupun kejadian tindak kriminal, jumlahnya cenderung relatif stabil dari bulan ke bulan.
                
                2. **Polanya Relatif Serupa**: Terdapat konsistensi dalam pola jumlah kejahatan antara bulan laporan dan bulan kejadian. Jumlah kejahatan cenderung meningkat pada awal tahun, mencapai puncaknya di pertengahan tahun, dan kemudian turun kembali menjelang akhir tahun.
                
                3. **Perbedaan dalam Jumlah Tertentu**: Meskipun polanya serupa, terdapat perbedaan kecil dalam jumlah tertentu antara bulan laporan dan bulan kejadian. Namun, perbedaan ini tidak signifikan dalam skala besar. Bisa dilihat dari grafik line laporan kriminal pada bulan ke-8 dan kejadian tindak kriminal dari bulan ke bulan pada bulan ke-8 juga, disana terdapat penurunan yang tidak terlalu signifikan.
                
                4. **Penurunan pada Akhir Tahun**: Terdapat penurunan yang konsisten dalam jumlah kejahatan pada bulan November dan Desember. Hal ini mungkin terkait dengan faktor-faktor seperti peningkatan keamanan menjelang liburan atau perubahan perilaku masyarakat selama musim liburan.
            '''
    st.write(string3)

# Tambahkan garis batas horizontal
st.markdown("---")

# ---------------------------------------------------------------

# Menampilkan judul dengan fungsi st.title()
st.title('Analisa Tren Musiman Tindak Kriminal')

# Membuat Column Report
reportLpr_col1, reportLpr_col2 = st.columns(2)
reportLpr_col3, reportLpr_col4 = st.columns(2)

with reportLpr_col1:
    # Grafik Interaktif untuk Analisis Lebih Lanjut
    interactive_chart = alt.Chart(data_reportLpr).mark_line().encode(
        x=alt.X('Month_Lpr:O', axis=alt.Axis(title='Bulan', labelAngle=0)),
        y='Jumlah Laporan:Q',
        color='Year_Lpr:N',
        tooltip=['Year_Lpr', 'Month_Lpr', 'Jumlah Laporan']
    ).properties(
        width=600,
        height=400,
        title='Tren Musiman Jumlah Laporan Kriminal (Interaktif)'
    ).interactive()
    
    interactive_chart
    
with reportLpr_col2:
    # Heatmap untuk Melihat Pola
    heatmap = alt.Chart(data_reportLpr).mark_rect().encode(
        x=alt.X('Month_Lpr:O', axis=alt.Axis(title='Bulan', labelAngle=0)),
        y='Year_Lpr:O',
        color='Jumlah Laporan:Q'
    ).properties(
        width=600,
        height=400,
        title='Heatmap Pola Musiman Jumlah Laporan Kriminal'
    )
    
    heatmap
    
with reportLpr_col3:
    # Layout
    st.markdown('##### Tren Jumlah Perbandingan Berdasarkan Tahun')

    # Buat daftar tahun unik
    tahun_unik = list(data_reportLpr['Year_Lpr'].unique())

    # Buat pilihan dropdown untuk tahun pertama
    tahun_pertama = st.selectbox('Pilih Tahun Pertama:', tahun_unik)

    # Buat pilihan dropdown untuk tahun kedua
    tahun_kedua = st.selectbox('Pilih Tahun Kedua:', tahun_unik)

    # Filter data berdasarkan tahun yang dipilih
    data_reportLpr_filtered1 = data_reportLpr[data_reportLpr['Year_Lpr'] == tahun_pertama]
    data_reportLpr_filtered2 = data_reportLpr[data_reportLpr['Year_Lpr'] == tahun_kedua]

    # Buat plot dengan Altair untuk perbandingan antara tahun pertama dan tahun kedua
    chart = alt.Chart(data_reportLpr_filtered1).mark_line().encode(
        x=alt.X('Month_Lpr', title='Bulan'),
        y=alt.Y('Jumlah Laporan', title='Jumlah Kejahatan'),
        color=alt.value('blue'),
        tooltip=['Year_Lpr:N', 'Jumlah Laporan:Q']  # Menambahkan tooltip untuk tahun dan jumlah kejahatan
    ).properties(
        width=600,
        height=400
    )

    chart += alt.Chart(data_reportLpr_filtered2).mark_line().encode(
        x=alt.X('Month_Lpr', title='Bulan'),
        y=alt.Y('Jumlah Laporan', title='Jumlah Kejahatan'),
        color=alt.value('red'),
        tooltip=['Year_Lpr:N', 'Jumlah Laporan:Q']  # Menambahkan tooltip untuk tahun dan jumlah kejahatan
    )

    # Tambahkan titik pada setiap lekukan grafik
    chart += alt.Chart(data_reportLpr_filtered1).mark_circle(color='blue').encode(
        x=alt.X('Month_Lpr', title='Bulan'),
        y=alt.Y('Jumlah Laporan', title='Jumlah Kejahatan'),
        tooltip=['Year_Lpr:N', 'Jumlah Laporan:Q']  # Menambahkan tooltip untuk tahun
    )

    chart += alt.Chart(data_reportLpr_filtered2).mark_circle(color='red').encode(
        x=alt.X('Month_Lpr', title='Bulan'),
        y=alt.Y('Jumlah Laporan', title='Jumlah Kejahatan'),
        tooltip=['Year_Lpr:N', 'Jumlah Laporan:Q']  # Menambahkan tooltip untuk tahun
    )

    # Tampilkan plot menggunakan Streamlit
    st.altair_chart(chart, use_container_width=True)
    
    # Menggunakan widget bar Altair untuk memilih tahun
    year_selected = alt.binding_select(options=sorted(data_reportLpr['Year_Lpr'].unique()), name='Tahun  ')
    year_selection = alt.selection_single(fields=['Year_Lpr'], bind=year_selected)

with reportLpr_col4:
    st.markdown('##### Analisa Tren Musiman Tindak Kriminal')
    string4 = '''
                1. **Tren Menurun pada Tahun 2024**: Terdapat penurunan yang signifikan dalam jumlah laporan kejahatan pada tahun 2024, terutama pada bulan Januari, dibandingkan dengan tahun-tahun sebelumnya. Ini menunjukkan adanya perubahan yang mungkin signifikan dalam situasi keamanan atau perubahan dalam kebijakan penegakan hukum yang berdampak pada tingkat kejahatan.
                
                2. **Fluktuasi Tren Tahunan**: Secara umum, terlihat fluktuasi dalam jumlah laporan kejahatan dari bulan ke bulan dalam setiap tahun. Meskipun ada peningkatan dan penurunan yang terjadi dari bulan ke bulan, tetapi secara keseluruhan, trennya cenderung stabil atau menurun dari tahun ke tahun.
                
                3. **Pola Musiman**: Terlihat pola musiman dalam jumlah laporan kejahatan, dengan biasanya terjadi peningkatan selama beberapa bulan tertentu dalam setahun. Hal ini mungkin berkaitan dengan faktor-faktor musiman seperti liburan, cuaca, atau peristiwa-peristiwa khusus yang mempengaruhi tingkat kejahatan.
                
                Kesimpulan-konklusi ini memberikan gambaran yang komprehensif tentang situasi kejahatan berdasarkan data yang disediakan, serta menunjukkan potensi untuk penelitian dan tindakan lanjutan dalam rangka meningkatkan keamanan dan kesejahteraan masyarakat.
            '''
    st.write(string4)