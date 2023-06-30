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
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1, 2])
  with col1:
    st.markdown(a, unsafe_allow_html=True)
  with col2:
    st.markdown(b, unsafe_allow_html=True)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

def info(a, b, c, d, display_image=False):
  col1, col2, col3, col4 = st.columns(4)
  with col1:
    st.markdown(a, unsafe_allow_html=True)
  with col2:
    st.markdown(b, unsafe_allow_html=True)
  with col3:
    st.download_button(label=':red[Download the CV]', data=c, file_name='CV Edoardo Sezzi.pdf', mime='application/pdf', key=None)
  if display_image:
    with col4:
        st.markdown(d, unsafe_allow_html=True)