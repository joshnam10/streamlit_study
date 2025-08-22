import streamlit as st

choice=st.radio('아무거나 골라봐',['사과','바나나','딸기','키위'])
st.write(choice)

if choice=='사과':
    st.write('맞다')
else:
    st.write("틀리다")


st.selectbox('선택해',['안녕하세요','저는 남기현','입니다.'])
