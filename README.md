# 🍽️ Swiggy Restaurant Recommendation System

A smart recommendation system that suggests restaurants based on user preferences such as city, cuisine, rating, and cost — built using Python, Machine Learning, and Streamlit.

---

## 🚀 Features

- 🔍 Filter-based restaurant discovery (City, Cuisine, Rating, Cost)
- 🤖 Recommendation engine using Cosine Similarity
- ⚡ Fast performance with `@st.cache_data`
- 🧠 Smart filtering logic (e.g., multi-cuisine matching)
- 💅 Stylish card layout UI built with Streamlit

---

## 📊 Tech Stack

- Python 🐍
- Pandas, Scikit-learn
- Streamlit (for the dashboard)
- Cosine Similarity (for recommendations)

---

## 📁 Project Structure

```
swiggy_recommendation_system/
├── app.py                      # Streamlit application
├── README.md                   # Project overview
├── requirements.txt            # Libraries used
├── cleaned_data/
│   ├── cleaned_data.csv
│   └── encoded_data.csv
├── encoder/
│   └── encoder.pkl
├── scripts/
│   ├── 01_data_cleaning.py
│   ├── 02_encoding.py
│   └── 03_recommendation_engine.py
```

---

## 🧪 How to Run the App Locally

1. **Clone the repo**
```bash
git clone https://github.com/your-username/swiggy-recommendation-system.git
cd swiggy-recommendation-system
```

2. **Create and activate a virtual environment**
```bash
python -m venv venv
venv\Scripts\activate   # for Windows
```

3. **Install required packages**
```bash
pip install -r requirements.txt
```

4. **Run the Streamlit app**
```bash
streamlit run app.py
```

## 🔗 Connect With Me

📍 [Sai Vennela Yadavalli on LinkedIn](https://www.linkedin.com/in/sai-vennela-yadavalli-8b854432a)  
💼 Let’s build smart data-driven solutions together!
