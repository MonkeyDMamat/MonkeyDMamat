import streamlit as st
from streamlit_folium import folium_static
import folium

def main():
    st.set_page_config(page_icon="🌊")
    st.sidebar.success("Select Page Above.")
    st.title("Persebaran Makrozoobenthos")

    # Koordinat persebaran untuk contoh (ganti sesuai kebutuhan)
    species_coordinates = {
        'Clams': (-2.457, 118.701),
        'Crabs': (-34.611, 150.768),
        'Jelly_Fish': (0.789, -30.125),
        'Lobster': (-16.918, 145.775),
        'Nudibranchs': (-16.5, 152.5),
        'Octopus': (39.933, 32.859),
        'Sea_Urchins': (35.861, 14.365),
        'Shrimp': (13.408, -87.083),
        'Squid': (-6.228, 106.807),
        'Starfish': (43.735, 7.426)
    }

    # Inisialisasi peta menggunakan folium
    m = folium.Map(location=[0, 0], zoom_start=2)

    # Tambahkan marker untuk setiap spesies
    for species, coordinates in species_coordinates.items():
        folium.Marker(location=coordinates, popup=species).add_to(m)

    # Menampilkan peta di dalam streamlit
    folium_static(m)

if __name__ == '__main__':
    main()
