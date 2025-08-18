import streamlit as st
import random

# --- 기본 설정 ---
st.set_page_config(page_title="MBTI 직업 추천", layout="centered", page_icon="💼")

# --- CSS 스타일 ---
st.markdown("""
    <style>
    body {
        background-color: #fef6ff;
    }
    .stApp {
        background-image: linear-gradient(to right, #fbc2eb, #a6c1ee);
        color: #000000;
    }
    .title {
        font-size: 48px;
        font-weight: bold;
        color: #6a0572;
        text-align: center;
        padding: 10px;
    }
    .subtitle {
        font-size: 24px;
        color: #333;
        text-align: center;
    }
    .mbti-box {
        background-color: #ffffffaa;
        padding: 20px;
        border-radius: 15px;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 타이틀 ---
st.markdown('<div class="title">💡 MBTI 기반 진로 추천 웹 앱</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">당신의 성격 유형에 맞는 직업을 찾아보세요!</div>', unsafe_allow_html=True)

st.markdown('<div class="mbti-box">', unsafe_allow_html=True)

# --- MBTI 리스트 ---
mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

mbti_descriptions = {
    "INTJ": "전략가형 - 독창적이고 분석적인 성향",
    "INFP": "중재자형 - 이상주의적이고 창의적인 성향",
    "ENTP": "변론가형 - 재치 있고 호기심 많은 성향",
    "ISFJ": "수호자형 - 헌신적이고 책임감 있는 성향",
    # 필요한 만큼 추가 가능
}

career_recommendations = {
    "INTJ": ["데이터 과학자", "전략 컨설턴트", "AI 연구원"],
    "INFP": ["작가", "디자이너", "심리상담가"],
    "ENTP": ["기획자", "스타트업 창업자", "마케터"],
    "ISFJ": ["간호사", "교사", "사회복지사"],
    # 나머지 MBTI는 비슷하게 추가 가능
}

# --- 사용자 입력 ---
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", mbti_types)

# --- 추천 결과 출력 ---
if selected_mbti:
    st.subheader(f"🧠 {selected_mbti} 유형 설명")
    st.info(mbti_descriptions.get(selected_mbti, "아직 준비 중인 설명입니다."))

    st.subheader("✨ 추천 직업")
    recommended_jobs = career_recommendations.get(selected_mbti, ["추천 직업 정보가 아직 없습니다."])
    for job in recommended_jobs:
        st.success(f"✅ {job}")

st.markdown('</div>', unsafe_allow_html=True)

# --- 바닥글 ---
st.markdown("---")
st.markdown("© 2025 MBTI 진로 추천 웹 앱 | 만든이: 당신의 이름", unsafe_allow_html=True)
