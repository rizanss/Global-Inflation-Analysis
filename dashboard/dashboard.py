import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Gathering Data
@st.cache_data
def load_data():
    df = pd.read_csv('https://raw.githubusercontent.com/rizanss/Global-Inflation-Analysis/main/data/global_inflation_data.csv')
    return df

# Exploratory Data Analysis
def main():
    st.title('Global Inflation Analysis')

    # Load data
    df = load_data()

    #Analisis Perbandingan Tingkat Inflasi Antar Negara
    st.header('1. Analisis Perbandingan Tingkat Inflasi Antar Negara')
    st.write('Dari analisis ini, kita dapat melihat negara-negara yang mengalami tingkat inflasi rata-rata tertinggi pada tahun 2024.')
    st.write('Negara-negara tersebut mungkin memiliki kondisi ekonomi yang mempengaruhi tingkat inflasi yang signifikan. Kita bisa lihat di nomor 1 yaitu Zimbabwe dengan tingkat rata-rata tertinggi inflasi pada tahun 2024.')
    st.write('Visualisasi bar ini membantu membandingkan tingkat inflasi antara negara-negara secara langsung.')
    mean_inflation_by_country = df.groupby('country_name').mean(numeric_only=True).reset_index()
    mean_inflation_by_country = mean_inflation_by_country.sort_values(by='2024', ascending=False)
    top_10_countries = mean_inflation_by_country.head(10)

    st.write(top_10_countries)

    plt.figure(figsize=(12, 8))
    sns.barplot(data=top_10_countries, x='2024', y='country_name', palette='viridis')
    plt.title('Top 10 Countries with Highest Average Inflation Rate in 2024')
    plt.xlabel('Average Inflation Rate (%)')
    plt.ylabel('Country')
    st.pyplot(plt)

    #Tren Inflasi Global Seiring Waktu
    st.header('2. Tren Inflasi Global Seiring Waktu')
    st.write('Tren Inflasi Global (1980-2024):')
    st.write('Dari grafik, kita bisa melihat bagaimana tren inflasi global berubah dari waktu ke waktu. Tren ini bisa memberikan wawasan tentang kondisi ekonomi global dan faktor-faktor makroekonomi yang memengaruhi inflasi. Terkadang, tren ini bisa mencerminkan periode inflasi tinggi atau rendah secara keseluruhan.')
    mean_inflation_by_year = df.iloc[:, 2:].mean()

    plt.figure(figsize=(10, 6))
    plt.plot(mean_inflation_by_year.index, mean_inflation_by_year.values, marker='o', linestyle='-')
    plt.title('Global Inflation Trends Over Time (1980-2024)')
    plt.xlabel('Year')
    plt.ylabel('Average Inflation Rate (%)')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

    #Tren Inflasi di Setiap Negara
    st.header('3. Tren Inflasi di Setiap Negara')
    st.write('Analisis ini memungkinkan pengguna untuk memilih negara tertentu dan melihat bagaimana tingkat inflasi di negara tersebut berubah dari waktu ke waktu. Ini bisa memberikan pemahaman yang lebih mendalam tentang kondisi ekonomi setiap negara dan faktor-faktor yang mempengaruhi inflasi di tingkat negara.')
    st.write('Membandingkan tren inflasi antara negara-negara dapat memberikan wawasan tentang perbedaan dan kesamaan dalam dinamika ekonomi mereka.')
    st.write("Select a country to visualize its inflation trend:")
    countries = df['country_name'].unique()
    selected_country = st.selectbox('Country', countries)

    country_data = df[df['country_name'] == selected_country]
    years = [str(year) for year in range(1980, 2025)]
    inflation_data = country_data[years].iloc[0]

    plt.figure(figsize=(10, 6))
    plt.plot(years, inflation_data, marker='o', linestyle='-')
    plt.title(f'Inflation Trend in {selected_country}')
    plt.xlabel('Year')
    plt.ylabel('Inflation (%)')
    plt.grid(True)
    plt.xticks(rotation=45)
    st.pyplot(plt)

if __name__ == '__main__':
    main()