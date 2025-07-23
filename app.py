import streamlit as st
import nltk

def word_tokenize1(s):
    if s==[]:
        st.write_stream("Please a enter to sentence to be tokenized")
        
    else:
        tokens = nltk.word_tokenize(s)
        return tokens
        
st.title("Sentence Tokenizer App")

st.write("Enter a sentence below to be tokenized into words.")

user_sentence = st.text_input("Enter your sentence here:")

if st.button("Tokenize"):
    tokens = word_tokenize1(user_sentence)
    for token in tokens:
        st.write(token)
 
    
