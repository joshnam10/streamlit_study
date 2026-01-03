import streamlit as st
st.title('다양한 selects')

st.subheader('radio')
choice=st.radio('아무거나 골라봐',['사과','바나나','딸기','키위'])
st.write(choice)

if choice=='사과':
    st.write('맞다')
else:
    st.write("틀리다")
st.divider()

st.subheader('selectbox')
st.selectbox('선택해',['안녕하세요','저는 남기현','입니다.'])

st.divider()

options=st.multiselect('여행가방에 챙길것',['옷','컴퓨터','안경','물안경','선글라스'])
st.write(options,'를 선택')

options=st.multiselect('여행가방에 챙길것(최대 5)',
                       ['옷','컴퓨터','안경','물안경','선글라스'],
                       accept_new_options=True,
                       max_selections=5)
st.write(options,'를 선택')

st.divider()

st.subheader('pills')
st.pills('방향',['동','서','남','북'])

# option_map=

st.pills('필터',[":material/add:",':material/zoom_in:',':material/zoom_out:'],selection_mode='multi')

st.pills('필터',['❤','🧡','🖤'],selection_mode='multi')

st.divider()

st.subheader('segmented control')
st.segmented_control('필터',['❤','🧡','🖤'],selection_mode='multi')

st.divider()

