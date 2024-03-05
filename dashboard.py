import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

sns.set(style='dark')

st.title('Proyek Analisis Data: Bike Sharing')
st.text("by Valentino Rocky A.")

st.write(
    """
    ## Menentukan Pertanyaan Bisnis
    - Jam berapakah jam sibuk penyewaan sepeda dilihat dari rata-rata penyewaan sepeda tiap jam berdasarkan linkungan sekitar (temperatur udara, kelembapan udara, dan kecepatan angin) dan musim?
    - Berapa rata-rata penyewaan sepeda pada tiap harinya berdasarkan tipe usernya?
    """
)

st.write("## Import Semua Packages/Library yang Digunakan")
st.code(
    """import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
""", language='python'
)

st.write("## Data Wrangling")
st.write("### Gathering Data")
st.write("Pertama kita load day.csv ke day_df.")
st.code(
    """day_df = pd.read_csv("/content/day.csv")
day_df.head()
""", language='python'
)
st.write("Kedua kita load hour.csv ke hour_df.")
st.code(
    """hour_df = pd.read_csv("/content/hour.csv")
hour_df.head()
""", language='python'
)
st.write("Karena data hanya ada 2, jadi langkah gathering sampai disini. Selanjutnya kita akan melakukan assessing.")
st.write("### Assessing Data")
st.write("Sekarang kita akan menilai day_df.")
st.code(
    """day_df.info()
""", language='python'
)
st.write("Dengan code diatas, kita bisa melihat banyak data tiap kolom serta tipe datanya. Disini kolom dteday harusnya memiliki tipe data datetime, kita akan mengubahnya di langkah cleaning.")
st.code(
    """print("Jumlah duplikasi: ", day_df.duplicated().sum())
""", language='python'
)
st.write("Dengan code diatas kita bisa melihat duplikasi data. Jika terjadi duplikasi kita akan menghapus duplikasinya di langkah cleaning. Disini tidak terlihat ada data yang terduplikasi.")
st.write("Sekarang kita akan menilai hour_df.")
st.code(
    """hour_df.info()

print("Jumlah duplikasi: ", hour_df.duplicated().sum())
""", language='python'
)
st.write("Disini dteday juga perlu diubah ke tipe data datetime.")
st.write("### Cleaning Data")
st.code(
    """def changeToDate(df, columns):
  for column in columns:
    df[column] = pd.to_datetime(df[column])
""", language='python'
)
st.write("Dengan code diatas kita bisa mengubah kolom dalam dataframe menjadi tipe data datetime.")
st.code(
    """changeToDate(day_df, ['dteday'])
day_df.info()

changeToDate(hour_df, ['dteday'])
hour_df.info()
""", language='python'
)
st.write("Dengan ini sekarang dteday memiliki tipe data datetime.")
st.write("## Exploratory Data Analysis (EDA)")
st.write("Disini kita akan mengeksplore dataset untuk mencari cara menjawab pertanyaan diatas.")
st.code(
    """hour_df.groupby(by=["hr", pd.cut(hour_df["temp"], np.arange(0.0, 1.1, 0.2))]).agg({
    "cnt" : "mean"
})
""", language='python'
)
st.code(
    """hour_df.groupby(by=["hr", pd.cut(hour_df["hum"], np.arange(0.0, 1.1, 0.2))]).agg({
    "cnt" : "mean"
})
""", language='python'
)
st.code(
    """hour_df.groupby(by=["hr", pd.cut(hour_df["windspeed"], np.arange(0.0, 1.1, 0.2))]).agg({
    "cnt" : "mean"
})
""", language='python'
)
st.code(
    """hour_df.groupby(by=["hr", "season"]).agg({
    "cnt" : "mean"
})
""", language='python'
)
st.code(
    """day_df.groupby(by="weekday").agg({
    "casual" : "mean",
    "registered" : "mean"
})
""", language='python'
)
st.write("Dengan code diatas, akhirnya kita tahu cara menjawab pertanyaan diatas. Langkah selanjutnya kita akan memvisualisasikan jawaban agar mudah dimengerti orang lain.")
st.write("## Visualization & Explanatory Analysis")

day_df = pd.read_csv("clean_day.csv")
hour_df = pd.read_csv("clean_hour.csv")

st.write("### Pertanyaan 1:")
st.code(
    """hourly_based_temp = hour_df.groupby(by=["hr", pd.cut(hour_df["temp"], np.arange(0.0, 1.1, 0.2))]).agg({
    "cnt" : "mean"
})
hourly_based_hum = hour_df.groupby(by=["hr", pd.cut(hour_df["hum"], np.arange(0.0, 1.1, 0.2))]).agg({
    "cnt" : "mean"
})
hourly_based_windspeed = hour_df.groupby(by=["hr", pd.cut(hour_df["windspeed"], np.arange(0.0, 1.1, 0.2))]).agg({
    "cnt" : "mean"
})
hourly_based_season = hour_df.groupby(by=["hr", "season"]).agg({
    "cnt" : "mean"
})
""", language='python'
)

hourly_based_temp = hour_df.groupby(by=["hr", pd.cut(hour_df["temp"], np.arange(0.0, 1.1, 0.2))]).agg({
    "cnt" : "mean"
})
hourly_based_hum = hour_df.groupby(by=["hr", pd.cut(hour_df["hum"], np.arange(0.0, 1.1, 0.2))]).agg({
    "cnt" : "mean"
})
hourly_based_windspeed = hour_df.groupby(by=["hr", pd.cut(hour_df["windspeed"], np.arange(0.0, 1.1, 0.2))]).agg({
    "cnt" : "mean"
})
hourly_based_season = hour_df.groupby(by=["hr", "season"]).agg({
    "cnt" : "mean"
})

st.code(
    """fig, ax = plt.subplots(nrows=6, ncols=4, figsize=(30, 60))

for i in range(6):
  for j in range(4):
    sns.barplot(y="cnt", x=["(0.0, 8.2]","(8.2, 16.4]","(16.4, 24.6]","(24.6, 32.8]","(32.8, 41.0]"], data=hourly_based_temp[i*20+j*5:i*20+j*5+5], ax=ax[i][j])
    ax[i][j].set_ylabel(None)
    ax[i][j].set_ylim(0, 650)
    ax[i][j].set_xlabel(None)
    ax[i][j].set_xticklabels(ax[i][j].get_xticklabels(), rotation=15)
    ax[i][j].set_title("Jam "+str(i*4+j)+":00 - "+str(i*4+j)+":59", loc="center", fontsize=18)
    ax[i][j].tick_params(axis ='x', labelsize=15)

plt.suptitle("Rata-rata Penyewaan Sepeda Tiap Jam Berdasarkan Temperatur Udara", fontsize=38)
plt.subplots_adjust(top=0.96)
plt.show()
""", language='python'
)

fig, ax = plt.subplots(nrows=6, ncols=4, figsize=(30, 60))

for i in range(6):
  for j in range(4):
    sns.barplot(y="cnt", x=["(0.0, 8.2]","(8.2, 16.4]","(16.4, 24.6]","(24.6, 32.8]","(32.8, 41.0]"], data=hourly_based_temp[i*20+j*5:i*20+j*5+5], ax=ax[i][j])
    ax[i][j].set_ylabel(None)
    ax[i][j].set_ylim(0, 650)
    ax[i][j].set_xlabel(None)
    ax[i][j].set_xticklabels(ax[i][j].get_xticklabels(), rotation=15)
    ax[i][j].set_title("Jam "+str(i*4+j)+":00 - "+str(i*4+j)+":59", loc="center", fontsize=18)
    ax[i][j].tick_params(axis ='x', labelsize=15)

plt.suptitle("Rata-rata Penyewaan Sepeda Tiap Jam Berdasarkan Temperatur Udara", fontsize=38)
plt.subplots_adjust(top=0.96)

st.write("Dengan code diatas akan menghasilkan gambar seperti dibawah ini.")

st.pyplot(fig)

st.code(
    """fig, ax = plt.subplots(nrows=6, ncols=4, figsize=(30, 60))

for i in range(6):
  for j in range(4):
    sns.barplot(y="cnt", x=["(0, 20]","(20, 40]","(40, 60]","(60, 80]","(80, 100]"], data=hourly_based_hum[i*20+j*5:i*20+j*5+5], ax=ax[i][j])
    ax[i][j].set_ylabel(None)
    ax[i][j].set_ylim(0, 650)
    ax[i][j].set_xlabel(None)
    ax[i][j].set_xticklabels(ax[i][j].get_xticklabels(), rotation=15)
    ax[i][j].set_title("Jam "+str(i*4+j)+":00 - "+str(i*4+j)+":59", loc="center", fontsize=18)
    ax[i][j].tick_params(axis ='x', labelsize=15)

plt.suptitle("Rata-rata Penyewaan Sepeda Tiap Jam Berdasarkan Kelembapan Udara", fontsize=38)
plt.subplots_adjust(top=0.96)
plt.show()
""", language='python'
)

fig, ax = plt.subplots(nrows=6, ncols=4, figsize=(30, 60))

for i in range(6):
  for j in range(4):
    sns.barplot(y="cnt", x=["(0, 20]","(20, 40]","(40, 60]","(60, 80]","(80, 100]"], data=hourly_based_hum[i*20+j*5:i*20+j*5+5], ax=ax[i][j])
    ax[i][j].set_ylabel(None)
    ax[i][j].set_ylim(0, 650)
    ax[i][j].set_xlabel(None)
    ax[i][j].set_xticklabels(ax[i][j].get_xticklabels(), rotation=15)
    ax[i][j].set_title("Jam "+str(i*4+j)+":00 - "+str(i*4+j)+":59", loc="center", fontsize=18)
    ax[i][j].tick_params(axis ='x', labelsize=15)

plt.suptitle("Rata-rata Penyewaan Sepeda Tiap Jam Berdasarkan Kelembapan Udara", fontsize=38)
plt.subplots_adjust(top=0.96)

st.write("Dengan code diatas akan menghasilkan gambar seperti dibawah ini.")

st.pyplot(fig)

st.code(
    """fig, ax = plt.subplots(nrows=6, ncols=4, figsize=(30, 60))

for i in range(6):
  for j in range(4):
    sns.barplot(y="cnt", x=["(0.0, 13.4]","(13.4, 26.8]","(26.8, 40.2]","(40.2, 53.6]","(53.6, 67.0]"], data=hourly_based_windspeed[i*20+j*5:i*20+j*5+5], ax=ax[i][j])
    ax[i][j].set_ylabel(None)
    ax[i][j].set_ylim(0, 650)
    ax[i][j].set_xlabel(None)
    ax[i][j].set_xticklabels(ax[i][j].get_xticklabels(), rotation=15)
    ax[i][j].set_title("Jam "+str(i*4+j)+":00 - "+str(i*4+j)+":59", loc="center", fontsize=18)
    ax[i][j].tick_params(axis ='x', labelsize=15)

plt.suptitle("Rata-rata Penyewaan Sepeda Tiap Jam Berdasarkan Kecepatan Angin", fontsize=38)
plt.subplots_adjust(top=0.96)
plt.show()
""", language='python'
)

fig, ax = plt.subplots(nrows=6, ncols=4, figsize=(30, 60))

for i in range(6):
  for j in range(4):
    sns.barplot(y="cnt", x=["(0.0, 13.4]","(13.4, 26.8]","(26.8, 40.2]","(40.2, 53.6]","(53.6, 67.0]"], data=hourly_based_windspeed[i*20+j*5:i*20+j*5+5], ax=ax[i][j])
    ax[i][j].set_ylabel(None)
    ax[i][j].set_ylim(0, 650)
    ax[i][j].set_xlabel(None)
    ax[i][j].set_xticklabels(ax[i][j].get_xticklabels(), rotation=15)
    ax[i][j].set_title("Jam "+str(i*4+j)+":00 - "+str(i*4+j)+":59", loc="center", fontsize=18)
    ax[i][j].tick_params(axis ='x', labelsize=15)

plt.suptitle("Rata-rata Penyewaan Sepeda Tiap Jam Berdasarkan Kecepatan Angin", fontsize=38)
plt.subplots_adjust(top=0.96)

st.write("Dengan code diatas akan menghasilkan gambar seperti dibawah ini.")

st.pyplot(fig)

st.code(
    """for i in range(6):
  for j in range(4):
    sns.barplot(y="cnt", x=["Semi", "Panas", "Gugur", "Dingin"], data=hourly_based_windspeed[i*16+j*4:i*16+j*4+4], ax=ax[i][j])
    ax[i][j].set_ylabel(None)
    ax[i][j].set_ylim(0, 650)
    ax[i][j].set_xlabel(None)
    ax[i][j].set_title("Jam "+str(i*4+j)+":00 - "+str(i*4+j)+":59", loc="center", fontsize=18)
    ax[i][j].tick_params(axis ='x', labelsize=15)

plt.suptitle("Rata-rata Penyewaan Sepeda Tiap Jam Berdasarkan Musim", fontsize=38)
plt.subplots_adjust(top=0.96)
plt.show()
""", language='python'
)

fig, ax = plt.subplots(nrows=6, ncols=4, figsize=(30, 60))

for i in range(6):
  for j in range(4):
    sns.barplot(y="cnt", x=["Semi", "Panas", "Gugur", "Dingin"], data=hourly_based_windspeed[i*16+j*4:i*16+j*4+4], ax=ax[i][j])
    ax[i][j].set_ylabel(None)
    ax[i][j].set_ylim(0, 650)
    ax[i][j].set_xlabel(None)
    ax[i][j].set_title("Jam "+str(i*4+j)+":00 - "+str(i*4+j)+":59", loc="center", fontsize=18)
    ax[i][j].tick_params(axis ='x', labelsize=15)

plt.suptitle("Rata-rata Penyewaan Sepeda Tiap Jam Berdasarkan Musim", fontsize=38)
plt.subplots_adjust(top=0.96)

st.write("Dengan code diatas akan menghasilkan gambar seperti dibawah ini.")

st.pyplot(fig)

st.write("### Pertanyaan 2:")
st.code(
    """daily_rental = day_df.groupby(by="weekday", as_index=False).agg({
    "casual" : "mean",
    "registered" : "mean"
})
""", language='python'
)

daily_rental = day_df.groupby(by="weekday", as_index=False).agg({
    "casual" : "mean",
    "registered" : "mean"
})

st.code(
    """fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(30, 15))

sns.barplot(x=["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"], y="casual", data=daily_rental, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_ylim(0, 4500)
ax[0].set_xlabel(None)
ax[0].set_title("Casual User", loc="center", fontsize=15)
ax[0].tick_params(axis ='y', labelsize=12)

sns.barplot(x=["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"], y="registered", data=daily_rental, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_ylim(0, 4500)
ax[1].set_xlabel(None)
ax[1].set_title("Registered User", loc="center", fontsize=15)
ax[1].tick_params(axis ='y', labelsize=12)

plt.suptitle("Rata-rata Penyewaan Sepeda Pada Tiap Hari Berdasarkan Tipe User", fontsize=38)
plt.show()
""", language='python'
)

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(30, 15))

sns.barplot(x=["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"], y="casual", data=daily_rental, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_ylim(0, 4500)
ax[0].set_xlabel(None)
ax[0].set_title("Casual User", loc="center", fontsize=15)
ax[0].tick_params(axis ='y', labelsize=12)

sns.barplot(x=["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"], y="registered", data=daily_rental, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_ylim(0, 4500)
ax[1].set_xlabel(None)
ax[1].set_title("Registered User", loc="center", fontsize=15)
ax[1].tick_params(axis ='y', labelsize=12)

plt.suptitle("Rata-rata Penyewaan Sepeda Pada Tiap Hari Berdasarkan Tipe User", fontsize=38)

st.write("Dengan code diatas akan menghasilkan gambar seperti dibawah ini.")

st.pyplot(fig)

st.write(
    """
    ## Conclusion
    - Jadi, berdasarkan temperatur udara, jam sibuknya berada pada jam 17.00 hingga 17.59 dengan tingkat temperatur udara berkisaran 24,6 hingga 32,8. Berdasarkan kelembapan udara, jam sibuknya berada pada jam 18.00 hingga 18.59 dengan tingkat kelembapan udara berkisaran 0 hingga 20. Berdasarkan kecepatan angin, jam sibuknya berada pada jam 17.00 hingga 17.59 dengan tingkat kecepatan angin berkisaran 13,4 hingga 26,8. Berdasarkan musim, jam sibuknya berada pada jam 21.00 hingga 21.59 pada musim gugur.
    - Jadi, untuk casual user banyak menyewa sepeda pada hari sabtu. Sedangkan untuk registered user banyak menyewa sepeda pada hari kamis.
    """
)

st.caption('Copyright (c) 2024')