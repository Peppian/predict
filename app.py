import streamlit as st
import pandas as pd
import joblib
import numpy as np
import os

from generative_ai_response import ask_openrouter
from prompt import generate_price_explanation_prompt

# === Konfigurasi ===
MODEL_PATH = 'predict/data/xgb_price_predictor.joblib'
COLUMNS_PATH = 'predict/data/xgb_model_columns.joblib'
DATA_PATH =  'predict/data/mobil123_data_updated.csv'

model = joblib.load(MODEL_PATH)
columns = joblib.load(COLUMNS_PATH)
data = pd.read_csv(DATA_PATH)

st.set_page_config(page_title="Estimasi Harga Mobil Bekas", page_icon="🚘")
st.title("🚘 Estimasi Harga Mobil Bekas")

# INPUT UI
brand_list = sorted(data['name'].dropna().unique())
brand = st.selectbox("Pilih Merek Mobil", ["-"] + brand_list)

filtered_models = data[data['name'] == brand]['model'].unique() if brand != "-" else []
model_selected = st.selectbox("Pilih Tipe / Model", ["-"] + list(filtered_models))

# Auto metadata
row = data[(data['name'] == brand) & (data['model'] == model_selected)].head(1)
if not row.empty:
    body_type = row['bodyType'].values[0]
    seating_capacity = int(row['seatingCapacity'].values[0])
    fuel_type = row['fuelType'].values[0]
else:
    body_type = "-"
    seating_capacity = "-"
    fuel_type = "-"

# Auto display
st.markdown(f"**Body Type (auto):** {body_type}")
st.markdown(f"**Jumlah Kursi (auto):** {seating_capacity if seating_capacity != '-' else '-'} kursi")

region = st.selectbox("Wilayah", ["-", "Jabodetabek", "Jawa - Bali", "Luar Jawa"])
transmission = st.selectbox("Transmisi", ["-", "AT", "MT"])
year = st.slider("Tahun Produksi", 2000, 2025, 2020)
mileage = st.number_input("Kilometer", min_value=0, value=0)

# PREDIKSI HARGA
if st.button("🔍 Estimasi Harga"):
    if "-" in [brand, model_selected, region, transmission, fuel_type, body_type, seating_capacity]:
        st.warning("Mohon lengkapi semua input terlebih dahulu.")
    else:
        # Inisialisasi data input
        input_data = {
            "value_mileage": mileage,
            "vehicleModelDate": year,
            "age": 2025 - year,
            "seatingCapacity": seating_capacity,
        }

        # One-hot encoding manual
        input_encoded = pd.DataFrame([input_data])

        # Tambahkan kolom dummy yang sesuai dengan model
        for col in columns:
            if col not in input_encoded.columns:
                input_encoded[col] = 0  # default semua kolom kategori = 0

        # Set kolom spesifik menjadi 1 jika cocok
        feature_flags = {
            f"name_{brand}": 1,
            f"model_{model_selected}": 1,
            f"bodyType_{body_type}": 1,
            f"fuelType_{fuel_type}": 1,
            f"addressRegion_{region}": 1,
            f"transmision_{transmission}": 1,
        }
        for col_name, val in feature_flags.items():
            if col_name in input_encoded.columns:
                input_encoded[col_name] = val

        # Urutkan kolom agar sama persis
        input_encoded = input_encoded[columns]

        # Prediksi
        estimated_price = model.predict(input_encoded)[0]
        st.success(f"💰 Estimasi Harga: **Rp {estimated_price:,.0f}**")

        # GENERATIVE AI
        with st.spinner("🧠 Menyusun penjelasan dari AI..."):
            prompt = generate_price_explanation_prompt(
                brand=brand,
                model=model_selected,
                year=year,
                transmission=transmission,
                fuel_type=fuel_type,
                body_type=body_type,
                seating_capacity=seating_capacity,
                region=region,
                mileage=mileage,
                estimated_price=estimated_price
            )
            explanation = ask_openrouter(prompt)

        st.markdown("---")
        st.subheader("🧠 Penjelasan AI:")
        st.markdown(explanation)
