# 🚘 Estimasi Harga Mobil Bekas dengan XGBoost & LLM
Proyek ini bertujuan membangun sistem prediksi harga mobil bekas di Indonesia menggunakan teknik Machine Learning (XGBoost) yang dikombinasikan dengan model Generatif AI (LLM) untuk memberikan penjelasan prediktif yang lebih natural kepada pengguna.

## Machine Learning Prediktif (XGBoost)
Model XGBoost digunakan untuk memprediksi angka harga mobil bekas secara kuantitatif. Model ini dilatih menggunakan data historis (merek, tahun, jarak tempuh, dll) dan belajar pola dari data untuk meminimalkan kesalahan prediksi.
Karakteristik:
Output berupa angka estimasi harga.
Berdasarkan statistik dan pola data aktual.
Akurasi diukur dengan metrik seperti MAE dan R².

## Generative AI (LLM)
Model LLM (Large Language Model) digunakan untuk menghasilkan penjelasan naratif berdasarkan hasil prediksi. Tujuannya adalah membantu pengguna memahami mengapa harga tersebut masuk akal, dengan bahasa yang lebih manusiawi dan deskriptif.
Karakteristik:
Output berupa teks penjelasan.
Tidak mengambil keputusan harga, hanya memberikan konteks.
Bersifat probabilistik dan tidak selalu 100% akurat.

Keduanya tidak bertentangan, melainkan saling melengkapi: ML memberikan angka, LLM memberikan narasi.

---

## 🔧 Fitur Utama
Scraping data harga mobil dari website otomotif Indonesia.
Model XGBoost untuk prediksi harga berdasarkan fitur mobil (merek, model, tahun, km, dll).
Evaluasi performa model menggunakan MAE dan R².
Integrasi LLM untuk memberikan penjelasan mengapa harga segitu.
Deployment sederhana via Streamlit.
Visualisasi analisis data dan performa model.

---

## 📊 Evaluasi Model
Model yang digunakan adalah XGBoost Regressor.
Hasil evaluasi:
📉 MAE (Mean Absolute Error): Rp 13.629.436
📈 R² (R-Squared): 98.47%
MAE menunjukkan rata-rata selisih prediksi dengan harga sebenarnya. Semakin kecil, semakin baik.
R² menunjukkan seberapa baik model menjelaskan variasi data. Semakin mendekati 100%, semakin baik.

---

## 🧠 Tentang Penjelasan LLM
Model ini juga menggunakan LLM untuk menghasilkan natural explanation setelah prediksi harga.
Contoh:
“Harga diperkirakan Rp 178.000.000 karena mobil ini bertransmisi otomatis, keluaran 2020, dan termasuk tipe yang cukup diminati di wilayah Jabodetabek…”

⚠️ Catatan: Respons LLM bersifat generatif dan dapat sesekali memberikan jawaban yang kurang tepat. Untuk meningkatakan akurasi LLM dengan melakukan finetuning model dibutuhkan waktu, data dan komputasi yang lebih besar.

---

## 🤝 Kontribusi & Saran
Proyek ini masih bisa dikembangkan lebih jauh:
Penambahan data sepeda motor
Segmentasi pasar berdasarkan budget
Penyesuaian harga berdasarkan kondisi kendaraan (opsional)
Validasi prediksi via crowdsource atau data pasar nyata

---

## 📬 Kontak
Dibuat dengan semangat data dan sedikit idealisme.
Hubungi saya untuk kolaborasi, pengembangan, atau sekadar berdiskusi tentang AI dan otomotif 🚗✨
febriandwfzr@gmail.com
