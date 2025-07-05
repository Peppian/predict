import pandas as pd
import numpy as np
import time
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
from xgboost import XGBRegressor

# === Konfigurasi ===
CURRENT_YEAR = 2025
MIN_MODEL_OCCURRENCE = 3
FOLDER = "data"

# Pastikan folder output tersedia
os.makedirs(FOLDER, exist_ok=True)

DATA_FILE = os.path.join(FOLDER, 'mobil123_data_updated.csv')
MODEL_FILE = os.path.join(FOLDER, 'xgb_price_predictor.joblib')
COLUMNS_FILE = os.path.join(FOLDER, 'xgb_model_columns.joblib')
TEST_SET_FILE = os.path.join(FOLDER, 'xgb_test_set.joblib')
TARGET_COLUMN = 'price'

def preprocess_data(df):
    print("📦 Memulai preprocessing...")

    df['value_mileage'] = pd.to_numeric(df['value_mileage'], errors='coerce')
    df['vehicleModelDate'] = pd.to_numeric(df['vehicleModelDate'], errors='coerce')
    df.dropna(subset=['value_mileage', 'vehicleModelDate'], inplace=True)

    df = df[df[TARGET_COLUMN] < 2_000_000_000]
    df['age'] = CURRENT_YEAR - df['vehicleModelDate']

    model_counts = df['model'].value_counts()
    common_models = model_counts[model_counts >= MIN_MODEL_OCCURRENCE].index
    df = df[df['model'].isin(common_models)]
    print(f"🧹 Dibuang model langka (<{MIN_MODEL_OCCURRENCE}x): {len(model_counts) - len(common_models)} model")

    df.drop(columns=['color', 'addressLocality'], inplace=True, errors='ignore')

    categorical_cols = ['name', 'model', 'bodyType', 'fuelType', 'addressRegion', 'transmision']
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

    df.dropna(inplace=True)
    print(f"✅ Data siap digunakan. Total baris: {len(df)}\n")
    return df

def train_xgb():
    print("🚗 Memulai training XGBoost...\n")

    df = pd.read_csv(DATA_FILE, low_memory=False)
    df = preprocess_data(df)

    X = df.drop(columns=[TARGET_COLUMN])
    y = df[TARGET_COLUMN]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.1, random_state=42
    )

    model = XGBRegressor(
        n_estimators=300,
        max_depth=12,
        learning_rate=0.1,
        subsample=0.8,
        colsample_bytree=0.8,
        random_state=42,
        n_jobs=-1
    )

    start = time.time()
    model.fit(X_train, y_train)
    end = time.time()

    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"✅ Training selesai dalam {end - start:.2f} detik.")
    print(f"📉 MAE : Rp {mae:,.2f}")
    print(f"📈 R²  : {r2 * 100:.2f}%\n")

    print("💾 Menyimpan model dan metadata...")
    joblib.dump(model, MODEL_FILE)
    joblib.dump(list(X.columns), COLUMNS_FILE)
    joblib.dump((X_test, y_test), TEST_SET_FILE)
    print("✅ Semua file berhasil disimpan ke folder LEGOAS/\n")

if __name__ == "__main__":
    train_xgb()
