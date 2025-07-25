# 📩 SMS Spam Classifier

This project is a machine learning-based **SMS Spam Classifier** that detects whether a given message is "spam" or "ham" (not spam). It includes full preprocessing, model training, and a deployed **Streamlit web app** for real-time predictions.

---

## 🚀 Features

- Cleaned and preprocessed SMS messages (HTML tags, punctuation, stopwords removed)
- Trained with a Naive Bayes classifier using `sklearn`
- Real-time message prediction via Streamlit
- Easy-to-use and interactive interface

---

## 🧠 Tech Stack

- **Python**
- **Pandas**, **NumPy**
- **Scikit-learn**
- **NLTK**
- **Streamlit**

---

## ⚙️ Preprocessing Steps

The following steps were applied to clean the raw SMS data:
1. Removed HTML tags
2. Removed punctuation
3. Removed stopwords
4. Lowercased all text

Each step was modularized into separate Python functions for maintainability.

---

## 🧪 Model Training

- Model: **Multinomial Naive Bayes**
- Trained on a labeled dataset with `spam` and `ham` categories
- Used `CountVectorizer` or `TfidfVectorizer` for converting text into numeric features
- The model is saved using `joblib` for deployment

---

## 🖥️ How to Run the Project Locally

### 1. Clone the repository:

```bash
git clone https://github.com/yourusername/sms-spam-classifier.git
cd sms-spam-classifier

###  Install dependencies:

pip install streamlit scikit-learn nltk
streamlit run app.py

## Feel free to fork this repo, improve the model or UI, and make pull requests!
## This is a open source code