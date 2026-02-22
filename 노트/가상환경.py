import streamlit as st

st.set_page_config(page_title="개발환경 설명", page_icon="🚀", layout="wide")

st.title("🚀 개발환경 & 가상환경 쉽게 이해하기")

st.markdown("""
### 🛰 나사 우주선 비유
- 우주선에는 부품이 15만 개
- 규격이 정확히 맞아야 함
- 시간이 지나면 설계도(버전)가 바뀜
- 예전 부품은 새 설계도에 안 맞을 수도 있음

👉 소프트웨어도 똑같다!
""")

st.divider()

# ✅ 탭 생성
tabs = st.tabs([
    "개발환경이란?",
    "Python venv",
    "Anaconda",
    "WSL",
    "Virtual Machine",
    "Docker(Container)",
    "차이 정리"
])

# 1️⃣ 개발환경
with tabs[0]:
    st.header("💻 개발환경이란?")
    st.write("""
    프로그램은 여러 부품으로 이루어져 있음:
    - 파이썬 버전
    - 라이브러리 버전
    - 프레임워크
    - 운영체제(OS)

    서로 다른 프로젝트가 다른 버전을 요구하면 충돌이 발생함.
    그래서 가상환경이 필요함.
    """)

# 2️⃣ venv
with tabs[1]:
    st.header("🐍 Python 기본 가상환경 (venv)")
    st.code("python -m venv myenv", language="bash")
    st.write("""
    ✔ 파이썬 기본 기능  
    ✔ 가볍고 간단  
    ✔ 프로젝트 단위 관리  
    """)

# 3️⃣ Anaconda
with tabs[2]:
    st.header("🐍📦 Anaconda")
    st.code("""
conda create -n myenv python=3.10
conda activate myenv
""", language="bash")
    st.write("""
    ✔ 데이터 분석에 강함  
    ✔ 라이브러리 관리 잘함  
    ❌ 용량이 큼  
    """)

# 4️⃣ WSL
with tabs[3]:
    st.header("🖥 WSL (Windows Subsystem for Linux)")
    st.write("""
    윈도우 안에서 리눅스를 실행하는 환경.

    ✔ 서버와 동일한 리눅스 환경 테스트 가능  
    ✔ 개발자들이 많이 사용  
    """)

# 5️⃣ VM
with tabs[4]:
    st.header("🖥 Virtual Machine")
    st.code("""
내 컴퓨터
 └── 가짜 컴퓨터
        └── OS
              └── 프로그램
""")
    st.write("""
    ✔ 완전 독립  
    ✔ 안전  
    ❌ 무거움 (RAM 많이 사용)  
    """)

    st.image('https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FYigVb%2Fbtq8ivFV8P1%2FAAAAAAAAAAAAAAAAAAAAALa9lNw8Ses5hcFdulAZ26o78cwmszoX_lNdKlkKLeSs%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1772290799%26allow_ip%3D%26allow_referer%3D%26signature%3DkupXXtO6xotIV98gG1IGmMtycCY%253D')
    
# 6️⃣ Docker
with tabs[5]:
    st.header("🐳 Docker (컨테이너)")
    st.code("""
OS 공유
 └── 여러 컨테이너
""")
    st.write("""
    ✔ 빠름  
    ✔ 가벼움  
    ✔ 배포용으로 많이 사용  
    """)
    st.image('https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2F2NDbU%2Fbtq8gxRKwDY%2FAAAAAAAAAAAAAAAAAAAAAN2fwBRZYpY3OABSOW3_I-BnU3qAIc1znblo4YiTtrxc%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1772290799%26allow_ip%3D%26allow_referer%3D%26signature%3DHutmcM781vapnigSaIgmlvMbIyA%253D')

# 7️⃣ 차이 정리
with tabs[6]:
    st.header("📊 전체 비교")

    st.table({
        "종류": ["venv", "Anaconda", "WSL", "VM", "Docker"],
        "무게": ["가벼움", "중간~무거움", "중간", "매우 무거움", "가벼움"],
        "주 용도": [
            "파이썬 프로젝트",
            "데이터 분석",
            "리눅스 환경 테스트",
            "완전 독립 환경",
            "배포 및 협업"
        ]
    })

st.divider()
st.caption("🎯 핵심: 가상환경은 프로젝트 충돌을 막기 위한 독립 공간이다.")

