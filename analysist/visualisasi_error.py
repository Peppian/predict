import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_absolute_error, r2_score

# === File Paths ===
MODEL_FILE = 'LEGOAS/xgb_price_predictor.joblib'
COLUMNS_FILE = 'LEGOAS/xgb_model_columns.joblib'
TEST_SET_FILE = 'LEGOAS/xgb_test_set.joblib'

# === Load model dan data ===
print("📦 Loading model dan test set...")
model = joblib.load(MODEL_FILE)
columns = joblib.load(COLUMNS_FILE)
X_test, y_test = joblib.load(TEST_SET_FILE)

# === Prediksi ===
y_pred = model.predict(X_test)

# === Evaluasi ===
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"📉 MAE : Rp {mae:,.2f}")
print(f"📈 R²  : {r2 * 100:.2f}%\n")

# === Visualisasi Error ===
plt.figure(figsize=(14, 6))

# Histogram Error
plt.subplot(1, 2, 1)
errors = y_pred - y_test
sns.histplot(errors, bins=50, kde=True, color='skyblue')
plt.title("Distribusi Error (y_pred - y_actual)")
plt.xlabel("Error (Rp)")
plt.ylabel("Frekuensi")

# Scatter Plot Prediksi vs Aktual
plt.subplot(1, 2, 2)
sns.scatterplot(x=y_test, y=y_pred, alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], '--', color='red')
plt.xlabel("Harga Aktual")
plt.ylabel("Harga Prediksi")
plt.title("Prediksi vs Harga Aktual")

plt.tight_layout()
plt.show()