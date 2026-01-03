import streamlit as st

st.title('분포들')


st.subheader('큰수의 법칙')
code10='''
import random
import matplotlib.pyplot as plt

l=[]
for i in range(10):

    a=random.randint(1,7)
    l.append(a)
x=range(1,7)
y=[]
for i in x:
    y.append(l.count(i))
fig,ax=plt.subplots()

ax.bar(x,y)
st.pyplot(fig)
'''
code100='''
import random
import matplotlib.pyplot as plt

l=[]
for i in range(100):

    a=random.randint(1,7)
    l.append(a)
x=range(1,7)
y=[]
for i in x:
    y.append(l.count(i))
fig,ax=plt.subplots()

ax.bar(x,y)
st.pyplot(fig)
'''
code10000='''
import random
import matplotlib.pyplot as plt

l=[]
for i in range(10000):

    a=random.randint(1,7)
    l.append(a)
x=range(1,7)
y=[]
for i in x:
    y.append(l.count(i))
fig,ax=plt.subplots()

ax.bar(x,y)
st.pyplot(fig)

'''
with st.expander('주사위'):
    st.write('10번')
    exec(code10)
    st.write('100번')
    exec(code100)
    st.write('10000번')
    exec(code10000)

st.subheader('이항분포')

with st.expander('구슬 실습'):
    st.write('구슬이 랜덤으로 왼쪽/오른쪽으로 4번 떨어짐')
    with open('__data/분포들/1.txt','r') as f:
        code1=f.read()
    with st.expander('구슬 한개짜리 코드는 이거다'):
        st.code(code1)
        exec(code1)

    with st.expander('구슬 여러개짜리는 이거다'):
        with open('__data/분포들/2.txt','r') as f:
            code2=f.read()
        st.code(code2)
        exec(code2)

    with st.expander('이거를 그래프로 표현'):
        with open('__data/분포들/3.txt','r') as f:
            code3=f.read()
        exec(code3)

    with st.expander('구슬 여러개'):
        with open('__data/분포들/4.txt','r',encoding='utf-8') as f:
            code4=f.read()
        exec(code4)
        이항분포(1)
        이항분포(100)
        이항분포(10000)
        이항분포(1000000)


with st.expander('동전을 n번 던졌을때 k번 앞면이 나올 확률은?'):
    st.write('동전을 4번 던진다')
    with open('__data/분포들/5.txt','r') as f:
        code5=f.read()
    exec(code5)

with st.expander('문제찍기'):
    st.write('문제가 10개, 각 문제당 보기가 4개인 시험에서 문제찍기')
    with open('__data/분포들/6.txt','r') as f:
        code6=f.read()
    exec(code6)


st.subheader('기하분포')

with st.expander('기하분포'):
    with st.expander('주사위'):
        st.write('1이 나올때 까지 굴린 주사위')
        with open('__data/분포들/7.txt','r') as f:
            code7=f.read()
        exec(code7)

    with st.expander('가위바위보'):
        st.write('가위바위보를 이길때 까지')
        with open('__data/분포들/8.txt','r') as f:
            code8=f.read()
        exec(code8)
        st.write('그래프를 보아하니 최대 10번까지는 갈것 같다')