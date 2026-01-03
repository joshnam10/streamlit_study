import streamlit as st
import random


a=['checkbox','code','radio','button','audio','selectbox','video']



color=['blue','gray','green','violet','primary','orange']
st.write(a)
ss=st.multiselect('그동안 배운거',a,default=a)
b=random.sample(population=ss,k=3)
st.write(f'당신이 사용해야할거')
ee=random.sample(color,len(b))
for i,j in zip(b,ee):
    st.badge(i,color=j)

# for i in color:
#     st.badge('hello',color=i)