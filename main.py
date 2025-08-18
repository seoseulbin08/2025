import streamlit as st
from streamlit_lottie import st_lottie
import requests
import random

# --- 페이지 설정 ---
st.set_page_config(
    page_title="💼 MBTI 직업 추천기",
    page_icon="🌟",
    layout="centered"
)

# --- CSS 스타일 적용 ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%);
        color: #333333;
        font-family: 'Arial', sans-serif;
    }
    .header-title {
        font-size: 60px;
        text-align: center;
        color: #5f27cd;
        font-weight: bold;
        margin-bottom: 0.5em;
    }
    .header-subtitle {
        font-size: 24px;
        text-align: center;
        color: #576574;
        margin-bottom: 1em;
    }
    .info-box {
        background-color: #ffffffcc;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 20px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# --- Lottie 로딩 함수 ---
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# --- Lottie 애니메이션 ---
lottie_url = "https://assets2.lottiefiles.com/packages/lf20_nlwjnm9o.json"  # 직업 관련 애니메이션
lottie_json = load_lottieurl(lottie_url)

# --- 타이틀 출력 ---
st.markdown('<div class="header-title">🚀 나에게 딱 맞는 직업은?</div>', unsafe_allow_html=True)
st.markdown('<div class="header-subtitle">MBTI로 알아보는 찰떡 진로 추천 💡</div>', unsafe_allow_html=True)

# --- 애니메이션 표시 ---
st_lottie(lottie_json, height=250)

# --- MBTI 선택 ---
mbti_list = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

mbti_descriptions = {
    "INTJ": "🧠 전략가형: 독립적이고 혁신적인 리더",
    "INFP": "🎨 중재자형: 이상적이며 창의적인 힐러",
    "ENTP": "💡 변론가형: 에너지 넘치고 아이디어가 풍부한 혁신가",
    "ISFJ": "🛡️ 수호자형: 헌신적이고 따뜻한 조력자",
    "ENFP": "🎉 활동가형: 열정 넘치는 사람 중심의 낙천가",
    "ESTJ": "📋 경영자형: 실용적이고 책임감 강한 리더",
    # 필요에 따라 추가 가능
}

career_recommendations = {
    "INTJ": ["🔬 데이터 과학자", "📊 전략 컨설턴트", "🤖 AI 연구원"],
    "INFP": ["✍️ 작가", "🎨 디자이너", "🧠 심리상담가"],
    "ENTP": ["📢 마케터", "🚀 스타트업 창업자", "🎤 콘텐츠 크리에이터"],
    "ISFJ": ["👩‍⚕️ 간호사", "👨‍🏫 교사", "🤝 사회복지사"],
    "ENFP": ["🎬 영화 감독", "🌍 NGO 활동가", "📚 교육 컨설턴트"],
    "ESTJ": ["🏢 경영 관리자", "📈 프로젝트 매니저", "🧑‍⚖️ 행정공무원"],
}

# --- 선택 박스 ---
selected_mbti = st.selectbox("👇 당신의 MBTI를 선택하세요!", mbti_list, index=mbti_list.index("INFP"))

# --- 결과 출력 박스 ---
if selected_mbti:
    st.markdown('<div class="info-box">', unsafe_allow_html=True)

    st.subheader(f"📌 {selected_mbti} 유형 설명")
    st.info(mbti_descriptions.get(selected_mbti, "설명이 준비 중입니다. 🌱"))

    st.subheader("🌟 어울리는 직업 추천")
    for job in career_recommendations.get(selected_mbti, ["추천 직업이 아직 준비 중이에요. 😢"]):
        st.success(job)

    st.markdown('</div>', unsafe_allow_html=True)

# --- 푸터 ---
st.markdown("---")
st.markdown("🧠 만든이: 당신의 이름 | © 2025 MBTI 진로추천", unsafe_allow_html=True)
st.caption("💬 MBTI는 참고용입니다. 실제 적성과 가치관을 함께 고려하세요!")
