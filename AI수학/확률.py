import streamlit as st
from fractions import Fraction

st.title('확률')

code1='''
w=0

cnt=0

for i in ['가위','바위','보']:
    for j in ['가위','바위','보']:
        cnt+=1
        if i==j:
            w+=1

print(w/cnt)
'''
with st.expander('가위바위보를 해서 비길 확률'):
    st.code(code1)
    exec(code1.replace('print(w/cnt)','st.write(Fraction(w,cnt))'))


code2='''
l3=0
ttl=0

for i in [1,2,3,4,5,6]:
    for j in [1,2,3,4,5,6]:
        ttl+=1
        if i+j <= 3:
            l3+=1

print(Fraction(l3,ttl))
'''
with st.expander('주사위를 두번 굴려서 합이 3이하일 확률'):
    st.code(code2)
    exec(code2.replace('print','st.write'))