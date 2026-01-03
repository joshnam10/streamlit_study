#streamlit으로 누적합을 간단하게 소개
import streamlit as st

st.title("누적합")

#누적합
if st.button('누접합이 뭐야?'):
    st.write('누접합이란:')
    st.write('리스트나 배열에서 앞에서부터 값을 차례대로 더한 합을 저장한 것')


#예시
st.subheader('누적합의 예시')
select=st.selectbox(
    '',
    [
    '예시1',
    '예시2',
    '예시3'
    ]
    )

if select=='예시1':
    st.write('입력배열:[2,4,6]')
    st.write('누적합:[2,6,12]')
elif select=='예시2':
    st.write('입력배열:[1,1,1,1]')
    st.write('누적합:[1,2,3,4]')
else:
    st.write('입력배열:[5,-2,3]')
    st.write('누적합:[5,3,6]')


#퀴즈
st.subheader('OX퀴즈')

quiz=st.radio('다음 리스티는 위 배열의 누적합일까요?',['YES','NO'])
