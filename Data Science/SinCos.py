import streamlit as st
import matplotlib.pyplot as plt
import math

st.title('원그리기')
code1='''
x=[]
d=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
y=[]
for i in d:
    x.append(i)
    y.append((1-i**2)**0.5)

for i in d:
    x.append(-i)
    y.append((1-i**2)**0.5)


for i in d:
    x.append(-i)
    y.append(-1*((1-i**2)**0.5))

for i in d:
    x.append(i)
    y.append(-1*((1-i**2)**0.5))
plt.scatter(x,y)

plt.axis('square')
plt.xlim(-1.1,1.1)
plt.ylim(-1.1,1.1)
'''
with st.expander('피타고라스로 원을 그리자'):
    st.code(code1)
    
    x=[]
    d=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
    y=[]
    for i in d:
        x.append(i)
        y.append((1-i**2)**0.5)

    for i in d:
        x.append(-i)
        y.append((1-i**2)**0.5)


    for i in d:
        x.append(-i)
        y.append(-1*((1-i**2)**0.5))

    for i in d:
        x.append(i)
        y.append(-1*((1-i**2)**0.5))
    
    fig, ax = plt.subplots()
    

    ax.scatter(x,y)

    ax.set_aspect('equal','box')
    st.pyplot(fig)

st.subheader('그렇게 하면 안된다')
code2='''
x=[]
d=range(0,361,10)
y=[]
for i in d:
    angle=math.radians(i)
    x.append(math.cos(angle))
    y.append(math.sin(angle))

plt.scatter(x,y)

plt.axis('square')
plt.xlim(-1.1,1.1)
plt.ylim(-1.1,1.1)
'''
with st.expander('원이 예쁘지가 않다'):
    st.write('각도를 사용해 원을 만들어 보자')
    st.code(code2)
    x=[]
    d=range(0,361,10)
    y=[]
    for i in d:
        angle=math.radians(i)
        x.append(math.cos(angle))
        y.append(math.sin(angle))

    fig,ax=plt.subplots()

    ax.scatter(x,y)

    ax.set_aspect('equal','box')
    st.pyplot(fig)
    