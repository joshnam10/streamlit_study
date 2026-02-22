import streamlit as st
st.title('DFS와 BFS')

st.subheader('BFS와 DFS의 개념')
with st.expander('BFS 개념'):
    st.write('''
        BFS(Breadth-First Search)는 너비 우선 탐색 알고리즘이다.
        시작 정점에서 가까운 노드부터 차례대로 탐색하며,
        한 레벨(같은 깊이)의 모든 노드를 먼저 방문한 뒤 다음 레벨로 이동한다.
        주로 큐(Queue) 를 사용해 구현한다.''')

with st.expander('DFS 개념'):
    st.write('''DFS(Depth-First Search)는 깊이 우선 탐색 알고리즘이다.
    한 경로를 끝까지 탐색한 뒤, 더 갈 곳이 없으면 되돌아와 다른 경로를 탐색한다.
    주로 재귀나 스택을 사용해 구현한다.''')


st.subheader('BFS와 DFS의 차이점')
st.write('예시 코드 결과들')
with st.expander('BFS'):
    with open('__data/bfs,dfs/BFS.txt','r',encoding='utf-8') as f:
            codeBFS=f.read()
    
    exec(codeBFS)
    st.write(result)
    st.write('코드:')
    st.code(codeBFS)

with st.expander('DFS'):
    with open('__data/bfs,dfs/DFS.txt','r',encoding='utf-8') as f:
            codeDFS=f.read()
    
    exec(codeDFS)
    st.write(result)
    st.write('코드:')
    st.code(codeDFS)
    






st.subheader('예시 코드')

with st.expander('BFS'):
    st.write('예시코드')
    with open('__data/bfs,dfs/1.txt','r',encoding='utf-8') as f:
            code1=f.read()
    st.code(code1)


with st.expander('DFS'):


    st.write('예시코드')
    with open('__data/bfs,dfs/2.txt','r',encoding='utf-8') as f:
            code2=f.read()
    st.code(code2)


