# titanic_app.py

import streamlit as st
import numpy as np
import pickle

print("Streamlit app başladı")
st.write("✅ Uygulama yükleniyor...")

# --- 1. Başlık ---
st.title("🚢 Titanic Survival Prediction App")
st.write("Bu uygulama, verdiğiniz bilgilere göre Titanic yolcusunun hayatta kalıp kalamayacağını tahmin eder.")

# --- 2. Kullanıcı Girdileri ---
st.sidebar.header("✍️ Yolcu Bilgileri")

pclass = st.sidebar.selectbox("Yolcu Sınıfı (1 = First, 2 = Second, 3 = Third)", [1, 2, 3])
sex = st.sidebar.radio("Cinsiyet", ("Erkek", "Kadın"))
age = st.sidebar.slider("Yaş", 0, 100, 30)
sibsp = st.sidebar.selectbox("Yanında kardeş/eş var mı? (Sayı)", list(range(0, 6)))
parch = st.sidebar.selectbox("Yanında çocuk/ebeveyn var mı? (Sayı)", list(range(0, 6)))
fare = st.sidebar.slider("Bilet Ücreti", 0.0, 300.0, 30.0)

# --- 3. Girdileri modele uygun hale getir ---
sex_bin = 1 if sex == "Erkek" else 0
adult_male = 1 if sex == "Erkek" and age >= 18 else 0
who_man = 1 if sex == "Erkek" and age >= 18 else 0
who_woman = 1 if sex == "Kadın" and age >= 18 else 0

class_Second = 1 if pclass == 2 else 0
class_Third = 1 if pclass == 3 else 0

X_input = np.array([[pclass, sex_bin, age, sibsp, parch, fare,
                     adult_male, class_Second, class_Third,
                     who_man, who_woman]])

# --- 4. Eğitilmiş modeli yükle (pickle) ---
model_path = "final_random_forest.pkl"
try:
    with open(model_path, "rb") as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("Model dosyası bulunamadı. Lütfen 'final_random_forest.pkl' dosyasını uygulama klasörüne ekleyin.")
    st.stop()

# --- 5. Tahmin ---
if st.button("🚀 Tahmini Göster"):
    prediction = model.predict(X_input)[0]
    result = "✅ Hayatta Kalır" if prediction == 1 else "❌ Kurtulamaz"
    st.subheader("🔍 Tahmin Sonucu:")
    st.success(result)
