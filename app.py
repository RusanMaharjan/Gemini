import streamlit as st
from model import gemini

st.header('Gemini Project')

user_input = st.text_area('Prompt', placeholder='Explain about LLM.')

if st.button('Send Prompt🛩️'):
    if user_input.strip() == '':
        st.warning('Enter valid promt.')
    else:
        with st.spinner('Thinking...🤔'):
            answer = gemini(user_input)
            st.success('Content Generated.')
            st.write(answer)