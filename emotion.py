import streamlit as st

import joblib

st.header('Emotion Analysis')



user_input = st.text_area('Enter your Sentence Here')

col1, col2, col3 = st.columns(3)
with col1:
    pass

with col2:
    button_pressed = st.button('Click to find emotion/sentiment')

with col3:
    pass

if button_pressed:
    model = joblib.load('Emotion_Analysis_model.pkl')
    tf_idf = joblib.load('TF-IDF vectorizer.pkl')
    user_input = tf_idf.transform([user_input, ])
    emotion = model.predict(user_input)
    st.write(f'Emotion/Sentiment  State: { emotion[0]}')

   # emotion = ['neutral', 'worry', 'surprise', 'love', 'fun', 'hate',
    #           'happiness', 'boredom', 'relief',
     #          'anger', 'sadness', 'enthusiasm', 'empty']
    if (emotion == 0):
        st.write('neutral')
    elif (emotion == 1):
        st.write('worry')

    elif (emotion == 2):
        st.write('surprise')
    elif (emotion == 3):
        st.write('love')
    elif (emotion == 4):
        st.write('fun')
    elif (emotion == 5):
        st.write('hate')
    elif (emotion == 6):
        st.write('happiness')
    elif (emotion == 7):
        st.write('boredom')
    elif (emotion == 8):
        st.write('relief')
    elif (emotion == 9):
        st.write('anger')
    elif (emotion == 10):
        st.write('sadness')
    elif (emotion == 11):
        st.write('enthusiasm')
    else:
        st.write('empty')




   # st.write(f'emotion : {'neutral'}')
    #st.write(f'emotion : {'worry'}')
    #st.write(f'emotion : {'surprise'}')
    #st.write(f'emotion : {'love'}')
    #st.write(f'emotion : {'fun'}')
    #st.write(f'emotion : {'hate'}')
    #st.write(f'emotion : {'happiness'}')
    #st.write(f'emotion : {'boredom'}')
    #st.write(f'emotion : {'relief'}')
    #st.write(f'emotion : {'anger'}')
    #st.write(f'emotion : {'sadness'}')


