import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("🩺 생활습관 기반 질병 위험도 예측기")
st.write("학습 목적으로 제작된 간단한 위험도 계산기입니다. 실제 의료 진단이 아닙니다.")

st.sidebar.header("📋 사용자 정보 입력")
age = st.sidebar.slider("나이", 10, 80, 25)
bmi = st.sidebar.slider("체질량지수 (BMI)", 10.0, 40.0, 22.0)
bp = st.sidebar.slider("수축기 혈압 (mmHg)", 80, 200, 120)
exercise = st.sidebar.slider("주당 운동 시간 (시간)", 0, 20, 3)
sugar = st.sidebar.slider("일일 당 섭취량 (g)", 0, 300, 50)

# ✅ 가중치를 키워서 점수 변화폭이 커지도록 조정
risk_score = (
    (age - 20) * 0.05 +      # 나이
    (bmi - 22) * 0.3 +       # 체질량지수
    (bp - 120) * 0.02 -      # 혈압
    (exercise * 0.2) +       # 운동
    (sugar - 50) * 0.01      # 당 섭취
)

# ✅ 점수를 0~10 사이로 클리핑
risk_score = np.clip(risk_score, 0, 10)

# ✅ 위험도 카테고리 (4단계)
if risk_score < 3:
    category = "낮음 😊"
elif risk_score < 6:
    category = "보통 😐"
elif risk_score < 8:
    category = "높음 ⚠️"
else:
    category = "위험 🚨"

# ✅ 결과 출력
st.subheader("📊 결과")
st.metric(label="예측된 생활습관병 위험도 점수", value=f"{risk_score:.1f} / 10")
st.write(f"예상 위험 단계: **{category}**")

# ✅ 원형 그래프 (10점 만점 기준)
labels = ["Risk Score", "Remaining"]
sizes = [risk_score, 10 - risk_score]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f', startangle=90)  # ✅ 영어로 변경
ax.axis("equal")
st.pyplot(fig)

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f점', startangle=90)  # % → '점' 표시
ax.axis("equal")
st.pyplot(fig)

st.info(
    """
    ⚠️ 이 결과는 **실제 진단이 아님**을 유의하세요.  
    생활습관 관리(운동, 식습관 개선 등)가 위험도 감소에 도움이 될 수 있습니다.
    """
)
