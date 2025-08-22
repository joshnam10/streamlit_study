import streamlit as st

st.title('남기현.')

st.header('자기소개')
st.write('- 이름: 남기현')
st.write('- 나이: 14')
st.write('- 성별: 남자')
st.write('- 취미: 레슬링')

st.header('코딩 실력')
st.write('파이썬')
# st.image('http://mazassumnida.wtf/api/v2/generate_badge?boj=josh1204')
st.markdown(
    """
        <a href="https://solved.ac/profile/josh1204">
            <image src="http://mazassumnida.wtf/api/v2/generate_badge?boj=josh1204"/>
        </a>
    """,
    unsafe_allow_html=True
)

st.header('퀴즈')
quiz=st.radio('다음중 내가 안가본 나라는?',['한국','중국','일본'])
if st.button('정답확인'):
    if quiz=='일본':
        st.success('정답')
    else:
        st.error('정답아님')

st.header('내가 제일 좋아하는 노래')
st.audio('Soda Pop.mp3',autoplay=True)

st.header('마무리')
st.write('이건 남기현이 만든 페이지다')