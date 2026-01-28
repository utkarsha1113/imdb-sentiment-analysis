#step1: import all libraries and the load the model
import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import load_model


#load the imdb dataset word index
word_index=imdb.get_word_index()
reverse_word_index={value:key for key,value in word_index.items()}

#load the pretrained model with relu activation
model=load_model('SimpleRNN_project.h5')
#step 2:helper functions
#functions to decode reviews
def decode_review(encoded_review):
    return ' '.join([reverse_word_index.get(i-3,'?')for i in encoded_review])
#function to prerprocess user input
def preprocess_text(text):
    words=text.lower().split()
    encoded_review=[word_index.get(word,2)+3 for word in words]
    padded_review=sequence.pad_sequences([encoded_review],maxlen=500)
    return padded_review

#stremlit app
import streamlit as st
st.title("IMDB MOVIE REVIEW SENTIMENT ANALYSIS")
st.write("Enter a Movie Review to Classify it is a Positive or Negative")
#user input
user_input=st.text_area('Movie Review')

if st.button("classify"):
    preprocessed_input=preprocess_text(user_input)
    
    #make prediction
    prediction=model.predict(preprocessed_input)
    sentiment='positive' if prediction[0][0]> 0.5 else 'negative'
    #Display the result 
    st.write(f"Setiment:{sentiment}")
    st.write(f"Predictioin Score:{prediction[0][0]}")
else:
    st.write('Please Enter a movie review')
    