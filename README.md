# 🧠 Titanic Survival Prediction App

Bu proje, Titanic yolcularının hayatta kalıp kalamayacağını tahmin eden bir makine öğrenimi modelini içerir. Model, [seaborn](https://github.com/mwaskom/seaborn-data/blob/master/titanic.csv) veri seti kullanılarak eğitilmiş ve Streamlit ile kullanıcı dostu bir arayüzle sunulmuştur.

---

## 🎯 Proje Amacı

Yolcuların yaş, cinsiyet, sınıf gibi özelliklerine göre hayatta kalma ihtimallerini tahmin etmek ve bu tahmini kullanıcıya web üzerinden sunmak.

---

## 🗃️ Kullanılan Veri Seti
- Kaynak: [Seaborn Titanic Dataset](https://github.com/mwaskom/seaborn-data/blob/master/titanic.csv)
- Öznitelikler:
  - `pclass`, `sex`, `age`, `sibsp`, `parch`, `fare`
  - `adult_male`, `class_Second`, `class_Third`, `who_man`, `who_woman`
- Hedef değişken: `survived`

---

## ⚙️ Modelleme Süreci

1. Veri Temizleme  
2. Sayısallaştırma  
3. Model Seçimi (Random Forest)  
4. Hiperparametre Optimizasyonu (GridSearchCV)  
5. Test Doğruluğu: %82 — CV Doğruluğu: %83.95

---

## 🖥️ Uygulama Arayüzü

- Kullanıcı Streamlit arayüzünden bilgileri girer  
- “Tahmini Göster” butonuna tıklar  
- Model sonucu: ✅ Hayatta Kalır veya ❌ Kurtulamaz olarak gösterilir

---

## 📦 Kullanılan Teknolojiler

| Kategori       | Araçlar |
|----------------|---------|
| Programlama    | Python 3.12 |
| ML Kütüphaneleri | pandas, numpy, sklearn |
| Arayüz         | Streamlit |
| Model Kaydı    | Pickle (.pkl) |
| Versiyonlama   | Git + GitHub |

---

## ☁️ Yayınlanan Uygulama Linki

🔗 [https://kocagilhasip-titanic-streamlit-app.streamlit.app](https://kocagilhasip-titanic-streamlit-app.streamlit.app)

---

## ✍️ Geliştiren  
**Hasip Kocagil**  
[linkedin.com/in/hasipkocagil](https://linkedin.com/in/hasipkocagil)  
[github.com/kocagilhasip](https://github.com/kocagilhasip)

---

## 📌 Notlar
- Bu proje eğitim ve demo amaçlıdır  
- Geliştirmeye açıktır: SHAP yorumlama, XGBoost, görsel analiz eklenebilir