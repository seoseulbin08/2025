import streamlit as st

st.set_page_config(page_title="🎬 영화 제목 맞추기 (주관식)", layout="centered", page_icon="🍿")

st.title("🍿 이모지로 맞추는 영화 제목 퀴즈 (주관식)")
st.write("아래 이모지 힌트를 보고 영화 제목을 입력하세요!")

quiz_data = [
    {
        "emojis": "🧙‍♂️🧝‍♀️💍🔥",
        "answer": "반지의 제왕",
        "alt_answers": ["반지의 제왕", "lord of the rings", "the lord of the rings"]
    },
    {
        "emojis": "🚀👨‍🚀🌕",
        "answer": "퍼스트 맨",
        "alt_answers": ["퍼스트 맨", "first man"]
    },
    {
        "emojis": "🦁👑🐒",
        "answer": "라이온 킹",
        "alt_answers": ["라이온 킹", "the lion king"]
    },
    {
        "emojis": "👩‍🎤🎤✨",
        "answer": "보헤미안 랩소디",
        "alt_answers": ["보헤미안 랩소디", "bohemian rhapsody"]
    },
    {
        "emojis": "🧟‍♂️🔫🏃‍♂️",
        "answer": "트레인 투 부산",
        "alt_answers": ["트레인 투 부산", "train to busan"]
    },
    {
        "emojis": "👩‍❤️‍👨🌹🚢",
        "answer": "타이타닉",
        "alt_answers": ["타이타닉", "titanic"]
    },
    {
        "emojis": "🕷️🧑‍🎤🕸️",
        "answer": "스파이더맨",
        "alt_answers": ["스파이더맨", "spiderman", "spider-man"]
    },
    {
        "emojis": "👨‍🔬🧪💥",
        "answer": "프랑켄슈타인",
        "alt_answers": ["프랑켄슈타인", "frankenstein"]
    },
    {
        "emojis": "🕵️‍♂️🔍🐍",
        "answer": "셜록 홈즈",
        "alt_answers": ["셜록 홈즈", "sherlock holmes"]
    },
]

# 세션 상태 초기화
if "q_index" not in st.session_state:
    st.session_state.q_index = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "answered" not in st.session_state:
    st.session_state.answered = False
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

def reset_quiz():
    st.session_state.q_index = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.user_input = ""

def normalize_text(text):
    # 소문자 변환, 공백 제거, 특수문자 제거 간단 처리
    return ''.join(e for e in text.lower() if e.isalnum())

def check_answer(user_answer):
    q = quiz_data[st.session_state.q_index]
    normalized_input = normalize_text(user_answer)
    correct_answers = [normalize_text(ans) for ans in q["alt_answers"]]

    if normalized_input in correct_answers:
        st.session_state.score += 1
        st.success("정답입니다! 🎉")
    else:
        st.error(f"오답입니다! 정답은 '{q['answer']}' 입니다.")
    st.session_state.answered = True

# 퀴즈 진행
if st.session_state.q_index < len(quiz_data):
    q = quiz_data[st.session_state.q_index]
    st.markdown(f"### 문제 {st.session_state.q_index + 1} / {len(quiz_data)}")
    st.markdown(f"<h1 style='font-size:60px;'>{q['emojis']}</h1>", unsafe_allow_html=True)

    if not st.session_state.answered:
        user_answer = st.text_input("영화 제목을 입력하세요:", value=st.session_state.user_input)
        st.session_state.user_input = user_answer

        if st.button("제출"):
            if user_answer.strip() == "":
                st.warning("영화 제목을 입력해주세요!")
            else:
                check_answer(user_answer)
    else:
        if st.button("다음 문제"):
            st.session_state.q_index += 1
            st.session_state.answered = False
            st.session_state.user_input = ""
            st.experimental_rerun()

else:
    st.write("---")
    st.write(f"🎉 퀴즈 완료! 당신의 점수는 **{st.session_state.score} / {len(quiz_data)}** 입니다.")
    if st.session_state.score == len(quiz_data):
        st.balloons()
        st.success("🎊 완벽해요! 영화 이모지 마스터!")
    elif st.session_state.score >= len(quiz_data) // 2:
        st.success("👍 잘했어요! 조금만 더 연습해보세요!")
    else:
        st.info("😅 좀 더 노력하면 좋아질 거예요! 다시 도전해보세요!")

    if st.button("처음부터 다시하기"):
        reset_quiz()
        st.experimental_rerun()
