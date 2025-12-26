# 🎯 Career Recommendation System (Machine Learning)

An **AI-powered Career Recommendation System** that suggests suitable career paths based on a user's **education level, specialization, skills, and certifications**. The project demonstrates a complete **end-to-end Machine Learning pipeline**, from data preprocessing to model deployment using **Streamlit**.

---

## 🚀 Features

* Predicts recommended career paths using Machine Learning
* Handles categorical data using **Label Encoding** and **Ordinal Encoding**
* Interactive **Streamlit web application** with a dark-themed UI
* Trained and evaluated using classification models
* Model persistence using **joblib**

---

## 🧠 Machine Learning Workflow

1. Data Cleaning & Exploration
2. Feature Selection
3. Encoding Categorical Variables
4. Train-Test Split
5. Model Training (Decision Tree / Random Forest)
6. Model Evaluation
7. Model Serialization
8. Web App Deployment (Streamlit)

---

## 📊 Dataset

**Input Features:**

* Education Level
* Specialization
* Skills
* Certifications

**Target Variable:**

* Recommended Career

---

## 🛠 Tech Stack

* **Programming Language:** Python
* **Libraries:**

  * pandas
  * numpy
  * scikit-learn
  * joblib
  * streamlit
* **Model:** Decision Tree / Random Forest Classifier
* **Deployment:** Streamlit

---

## 📦 Project Structure

```
career-recommendation-system/
│
├── career.ipynb                # Jupyter Notebook (Model Training)
├── career.py                   # Streamlit Application
├── career_model.pkl            # Trained ML Model
├── ordinal_encoder.pkl         # Ordinal Encoder
├── label_encoder.pkl           # Label Encoder
├── requirements.txt            # Project Dependencies
└── README.md                   # Project Documentation
```

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/career-recommendation-system.git
cd career-recommendation-system
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit App

```
streamlit run career.py
```

---

## 🖥 Streamlit App Preview

* Dropdown-based user inputs
* Instant career prediction

## 📈 Model Performance

* Achieved high accuracy after tuning
* Evaluated using:

  * Accuracy Score
  * Confusion Matrix
  * Classification Report

---

## 📌 Learning Outcomes

* Hands-on experience with categorical data encoding
* Understanding of classification algorithms
* End-to-end ML deployment experience
* Improved debugging and model evaluation skills

---

## 🔮 Future Enhancements

* Add more career categories
* Improve accuracy with ensemble models
* Deploy on cloud (AWS / Azure / Streamlit Cloud)
* Add resume-based career recommendations

---

## 👤 Author

**Shaik Zaid**
Aspiring Data Analyst / Data Scientist

🔗 LinkedIn: https://www.linkedin.com/in/shaik-mohammed-zaid
🔗 GitHub: https://github.com/shaikzaid7919/Career-Path-Recommendation

---

⭐ If you like this project, don’t forget to **star the repository**!
