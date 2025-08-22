import streamlit as st

code="""print(input())"""

st.code(code, language="python")

done=[]
st.subheader("TO-DO LIST")
done.append(st.checkbox('재밌게 놀기'))
done.append(st.checkbox('잘 자기'))
done.append(st.checkbox('컴퓨터 고치기'))


print(done)

st.write(done)

st.write(f'오늘 할것 개수:{len(done)} / 완료한것 개수:{done.count(True)}')
st.write(f'오늘 할것 개수:{len(done)} / 완료한것 개수:{sum(done)}')
