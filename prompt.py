def generate_price_explanation_prompt(
    brand,
    model,
    year,
    transmission,
    fuel_type,
    body_type,
    seating_capacity,
    region,
    mileage,
    estimated_price
):
    prompt = f"""
Mobil bekas dengan spesifikasi berikut:

• Merek           : {brand}
• Model           : {model}
• Tahun produksi  : {year}
• Transmisi       : {transmission}
• Jenis bahan bakar: {fuel_type}
• Tipe bodi       : {body_type}
• Kapasitas kursi : {seating_capacity} penumpang
• Wilayah         : {region}
• Jarak tempuh    : {mileage:,} km

diperkirakan memiliki harga sebesar **Rp {estimated_price:,.0f}**.

Jelaskan secara ringkas dan profesional dalam maksimal 250 kata, alasan mengapa harga tersebut masuk akal berdasarkan informasi di atas. Sertakan pertimbangan umum seperti usia kendaraan, tipe transmisi, kondisi pasar, dan wilayah.
"""
    return prompt.strip()