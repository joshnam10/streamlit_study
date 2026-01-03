import streamlit as st

st.title('다양한 평균들')

st.subheader('평균')
with st.expander('성적 평균 구하기 실습'):
    korean=st.slider('국어 점수', 0, 100, 50)
    math=st.slider('수학 점수', 0, 100, 50)
    english=st.slider('영어 점수', 0, 100, 50)

    st.write(f'평균값:{(korean+math+english)/3}')


st.subheader('가중 평균')
with st.expander('짜장면 짬뽕 실습'):
    st.write('짜장면 7000원')
    st.write('짬뽕 8000원')
    
    짜장면=st.slider('짜장면 먹은 사람 수',0, 10, 5)
    짬뽕=st.slider('짬뽕 먹은 사람 수',0, 10, 5)
    st.write(f'전체인원수:{짜장면+짬뽕}')
    try:
        st.write(f'가중 평균:{(짜장면*7000+짬뽕*8000)/(짜장면+짬뽕)}')
    except:
        pass


st.subheader('기하 평균')
with st.expander('세뱃돈 실습'):
    a=st.text_input('매년 세뱃돈이 몇배씩 증가하는지 써줘 (예시: 1 2 8)')
    인풋=list(map(int,a.split()))
    if len(인풋)!=0:
        곱한수=1
        for i in 인풋:
            곱한수*=i
        st.write(곱한수**(1/(len(인풋)-1)))
    else:
        st.write(0.0)

st.subheader('조화 평균')
with st.expander('속도 거리 시간 예시'):
    st.write('중간 중간 정거장이 있고 정거장끼리 거리는 같다. 사람1은 정거장을 들리고 들릴때마다 속도가 달라질수 있다. 사람2는 처음부터 끝까지 같은 속도로 갈것이고 사람1과 똑같은 시간이 걸릴것이다. 이때 사람2의 속도는 몇으로 가야될까?')
    numberofstops=st.slider('정거장 개수',2,10,5)
    정답=0
    for i in range(1,numberofstops):
        속도=st.slider(f'{i}번째 속도',1,20,10)
        정답+=1/속도
    정답/=numberofstops-1
    정답=정답**-1
    st.write(f'사람2의 속도:{정답}')