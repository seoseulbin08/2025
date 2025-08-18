import streamlit as st

st.set_page_config(page_title="인물 맞추기 퀴즈", page_icon="🧩", layout="centered")

st.title("🧠 인물 맞추기 퀴즈")
st.write("아래 인물의 이름을 맞춰보세요!")

# 문제 데이터: 사진 URL + 정답 인물 이름 + 선택지(인물 이름 4개)
quiz_data = [
    {
        "image": "https://upload.wikimedia.org/wikipedia/commons/1/1e/Elon_Musk_Royal_Society_%28crop2%29.jpg",
        "answer": "Elon Musk",
        "choices": ["Elon Musk", "Jeff Bezos", "Bill Gates", "Steve Jobs"]
    },
    {
        "image": "https://upload.wikimedia.org/wikipedia/commons/4/48/Emma_Watson_2013.jpg",
        "answer": "Emma Watson",
        "choices": ["Emma Watson", "Scarlett Johansson", "Natalie Portman", "Jennifer Lawrence"]
    },
    {
        "image": "https://upload.wikimedia.org/wikipedia/commons/5/57/Barack_Obama_official_portrait_2012_cropped.jpg",
        "answer": "Barack Obama",
        "choices": ["Barack Obama", "Joe Biden", "Donald Trump", "George Bush"]
    },
]

# 세션 상태 초기화
if "q_index" not in st.session_state:
    st.session_state.q_index = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "answered" not in st.session_state:
    st.session_state.answered = False

def reset_quiz():
    st.session_state.q_index = 0
    st.session_state.score = 0
    st.session_state.answered = False

def check_answer(selected):
    correct = quiz_data[st.session_state.q_index]["answer"]
    if selected == correct:
        st.session_state.score += 1
        st.success("정답입니다! 🎉")
    else:
        st.error(f"오답입니다! 정답은 {correct} 입니다.")
    st.session_state.answered = True

# 퀴즈 진행
if st.session_state.q_index < len(quiz_data):
    q = quiz_data[st.session_state.q_index]

    st.image(q["image"], width=300)
    st.write(f"**문제 {st.session_state.q_index + 1} / {len(quiz_data)}**: 이 인물의 이름은 무엇일까요?")

    if not st.session_state.answered:
        choice = st.radio("선택하세요:", q["choices"])
        if st.button("제출"):
            check_answer(choice)
    else:
        if st.button("다음 문제"):
            st.session_state.q_index += 1
            st.session_state.answered = False
            st.experimental_rerun()

else:
    st.write("---")
    st.write(f"🎉 퀴즈 완료! 당신의 점수는 **{st.session_state.score} / {len(quiz_data)}** 입니다.")

    if st.session_state.score == len(quiz_data):
        st.balloons()
        st.success("🎊 완벽해요! 당신은 인물 퀴즈 마스터!")
    elif st.session_state.score >= len(quiz_data) // 2:
        st.success("👍 잘했어요! 조금만 더 연습해보세요!")
    else:
        st.info("😅 좀 더 노력하면 좋아질 거예요! 다시 도전해보세요!")

    if st.button("처음부터 다시하기"):
        reset_quiz()
        st.experimental_rerun()
