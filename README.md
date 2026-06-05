# 📧 Email Spam Classifier using NLP & Streamlit

An end-to-end **Natural Language Processing (NLP)** project that classifies incoming emails as **Spam** or **Not Spam (Ham)** using Machine Learning.  
The project is deployed as an **interactive Streamlit web app** for real-time predictions.

---

## 🚀 Project Overview
This project demonstrates the full lifecycle of an NLP-based text classification model — from text cleaning and preprocessing to model training, evaluation, and deployment.

It uses **NLTK** for text processing, **TF-IDF** for feature extraction, and a **Naive Bayes classifier** for spam detection.

🔗 **Live App:** https://email-spam-classifier-nlp-op8tjqyeeu5o6cz8a6k2yu.streamlit.app/

---

## 🧠 Key Features
- Clean and preprocess raw email text using NLP techniques.
- Convert text to numeric vectors with TF-IDF.
- Train ML models to detect spam emails.
- Interactive Streamlit interface for user input and instant predictions.
- Model evaluation using accuracy, confusion matrix, and F1-score.

---
🧾 Model & Libraries Used

Python

NLTK

scikit-learn

pandas, numpy

matplotlib, seaborn

Streamlit

## 🧩 Project Workflow

### 1. Data Preprocessing
- Loaded dataset: `spam-1(in).csv`
- Removed unwanted columns and null values.
- Tokenized and normalized text using:
  - **Stopword removal**
  - **Stemming (PorterStemmer)**
  - **Lemmatization (WordNetLemmatizer)**
- Converted text to lowercase and removed punctuation/special characters.

### 2. Feature Engineering
- Transformed cleaned text into numerical features using **TF-IDF Vectorizer**.

### 3. Model Training
- Trained **Naive Bayes** classifier (MultinomialNB) for binary text classification.
- Compared models using accuracy, precision, recall, and F1-score.

### 4. Evaluation
- Evaluated model performance with metrics such as:
  - Accuracy
  - Confusion Matrix
  - Classification Report

### 5. Deployment (Streamlit)
- Created an interactive UI using **Streamlit**.
- User can input an email text → app predicts whether it’s *Spam* or *Ham*.
- Simple and lightweight web interface.
- 
📊 Results

Model: Multinomial Naive Bayes

Accuracy: ~97–99% (depending on dataset and parameters)

Precision & Recall: High performance in identifying spam messages.


---

## 🧱 Folder Structure
📁 Email_Spam_Classifier_NLP/
│
├── 📘 Email_Spam_Classifier_NLP.ipynb # Jupyter Notebook for model development
├── 📄 spam-1(in).csv # Dataset used
├── 📦 model.pkl # Trained model (optional)
├── 🧠 vectorizer.pkl # TF-IDF vectorizer (optional)
├── 🖥️ app.py # Streamlit app script
├── 📜 requirements.txt # Dependencies list
└── README.md # Project documentation


---

### 💡 Future Improvements

Implement deep learning model (LSTM / BERT) for higher accuracy.

Add multilingual spam detection.

Integrate API endpoint for third-party usage.

Visualize spam trends and keyword insights.

## ⚙️ Installation & Run

### 1. Clone the repository
```bash
git clone https://github.com/mr-akash12/Email_Spam_Classifier_NLP.git
cd Email_Spam_Classifier_NLP
