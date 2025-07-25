import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load('sms_spam_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

# preprocessing function
def preprocessing(text):
    # REMOVING HTML TAGs
    import re
    def remove_html_tags_(text):
        pattern = re.compile('<.*?>')
        return pattern.sub(r'',text)
    
    # REMOVING PUNCTUATIONS
    import string as sr

    punctuations = sr.punctuation
    def remove_punc(text):
        return text.translate(str.maketrans('','',punctuations))
    
    #REMOVING STOP WORDS
    from nltk.corpus import stopwords

    stop_words = set(stopwords.words('english'))
    def remove_stopwords_(text):
        return ' '.join([word for word in text.split() if word.lower() not in stop_words])
    
    
    text = remove_html_tags_(text)
    text = remove_punc(text)
    text = remove_stopwords_(text)
    
    return text.lower().strip()

# Streamlit UI
st.title("📱 SMS Spam Classifier")

input_sms = st.text_area("Enter your message here:")

if st.button("Check"):
    processed = preprocessing(input_sms)
    vec = vectorizer.transform([processed])
    prediction = model.predict(vec)[0]
    
    if prediction == 1:
        st.error("🚨 This message is SPAM!")
    else:
        st.success("✅ This message is NOT spam.")

