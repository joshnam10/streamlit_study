import streamlit as st
import random
import matplotlib.pyplot as plt

# 세션 상태에 점 데이터 저장
if "x1" not in st.session_state:
    st.session_state.x1, st.session_state.y1 = [], []
    st.session_state.x2, st.session_state.y2 = [], []
    st.session_state.result = []

st.title("🎲 Monte Carlo Simulation - π 추정")

for i in range(10000):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 <= 1:
        st.session_state.x1.append(x)
        st.session_state.y1.append(y)
    else:
        st.session_state.x2.append(x)
        st.session_state.y2.append(y)

    number = len(st.session_state.x1) / (
        len(st.session_state.x1) + len(st.session_state.x2)
    ) * 4
    st.session_state.result.append(number)

# 버튼을 누르면 샘플 추가
sample=st.slider("🎯 샘플 추가",0,10000, value=5000)




# 산점도
fig1, ax1 = plt.subplots()
ax1.scatter(st.session_state.x1[:sample], st.session_state.y1[:sample], color="orange", label="Inside")
ax1.scatter(st.session_state.x2[:sample], st.session_state.y2[:sample], color="blue", label="Outside")
ax1.set_aspect("equal", "box")
ax1.legend()
st.pyplot(fig1)

# π 추정값 변화
fig2, ax2 = plt.subplots()
ax2.plot(st.session_state.result[:sample])
ax2.set_title("π")
ax2.axhline(3.14, linestyle='--', color='red')
st.pyplot(fig2)

# 현재 추정값 표시
if st.session_state.result:
    st.metric("현재 π 추정값", f"{st.session_state.result[sample-1]:.5f}")
