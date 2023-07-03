import streamlit as st

#####################
# Custom function for printing text
def txt(a, b):
    col1, col2 = st.columns([4,1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)

def txt2(a, b):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(a, unsafe_allow_html=True)
    with col2:
        st.markdown(b, unsafe_allow_html=True)
