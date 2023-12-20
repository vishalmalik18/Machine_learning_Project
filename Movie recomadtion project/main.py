import streamlit as st

from helper import Movies

st.title("Movie Recommendation")

question = st.text_input("Question")

if question:
    method = Movies(movie_name=question)

    for rank, title in method:
        st.write(f"{rank}. {title}")
