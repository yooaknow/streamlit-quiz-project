import streamlit as st
from components import show_header
from data import load_quiz_data, load_result_data


def render():
    show_header()

    questions = load_quiz_data()
    total_questions = len(questions)

    if "current_q" not in st.session_state:
        st.session_state.current_q = 0

    if "answers" not in st.session_state:
        st.session_state.answers = {}

    current_idx = st.session_state.current_q
    q = questions[current_idx]

    st.markdown(
        """
        <style>
        .quiz-wrap {
            max-width:600px;
            margin:0 auto;
        }

        .login-info {
            color:#6B7280;
            font-size:0.85rem;
            margin-bottom:0.8rem;
        }

        .quiz-top {
            display:flex;
            justify-content:space-between;
            align-items:center;
            margin-bottom:0.8rem;
        }

        .quiz-count {
            color:#33412A;
            font-size:0.9rem;
            font-weight:800;
        }

        .quiz-title {
            text-align:center;
            color:#33412A;
            font-weight:900;
            font-size:1.3rem;
            line-height:1.3;
            margin:0.8rem 0 1rem;
            white-space:nowrap;
        }

        div[data-testid="stProgress"] > div > div > div {
            background-color:#8BAA6F !important;
        }

        div[data-testid="stProgress"] > div > div {
            background-color:#EEF3DF !important;
        }

        .quiz-card {
            background:#FFFFFF;
            border:1px solid #E5E7EB;
            border-radius:22px;
            padding:1.4rem 1.2rem 1.2rem;
            box-shadow:0 8px 24px rgba(0,0,0,0.04);
            margin-top:1.2rem;
            margin-bottom:1.2rem;
        }

        div.stButton > button {
            border-radius:999px !important;
            height:2.8rem !important;
            font-weight:800 !important;
            border:1px solid #E5E7EB !important;
            background:#FFFFFF !important;
            color:#33412A !important;
        }

        div.stButton > button:hover {
            border-color:#8BAA6F !important;
            background:#EEF3DF !important;
            color:#33412A !important;
        }

        hr {
            margin:1.8rem 0 1.2rem;
            border-color:#E5E7EB;
        }
        </style>

        <div class="quiz-wrap">
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"<p class='login-info'>👤 {st.session_state.username}님으로 로그인 중</p>",
        unsafe_allow_html=True,
    )

    col_back, col_count = st.columns([1, 1])

    with col_back:
        if st.button("‹ 뒤로", use_container_width=True):
            if current_idx > 0:
                st.session_state.current_q -= 1
                st.rerun()
            else:
                _reset_quiz_progress()
                st.session_state.page = "home"
                st.rerun()

    with col_count:
        st.markdown(
            f"<p class='quiz-count' style='text-align:right;'>{current_idx + 1} / {total_questions}</p>",
            unsafe_allow_html=True,
        )

    st.markdown(
        "<h2 class='quiz-title'>나는 왜 돈이 없을까 테스트</h2>",
        unsafe_allow_html=True,
    )

    st.progress((current_idx + 1) / total_questions)

    st.markdown('<div class="quiz-card">', unsafe_allow_html=True)

    image_path = f"assets/quiz{q['id']}.png"
    st.image(image_path, use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

    for option in q["options"]:
        option_key = option[0]

        if st.button(option, use_container_width=True, key=f"q{q['id']}_{option_key}"):
            st.session_state.answers[q["id"]] = option_key

            if current_idx < total_questions - 1:
                st.session_state.current_q += 1
                st.rerun()
            else:
                _calculate_and_save(questions, st.session_state.answers)
                st.session_state.page = "result"
                st.rerun()

    st.markdown("---")

    if st.button("← 홈으로", use_container_width=True):
        _reset_quiz_progress()
        st.session_state.page = "home"
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)


def _calculate_and_save(questions, answers):
    type_scores = {t: 0 for t in load_result_data().keys()}

    for q in questions:
        selected = answers.get(q["id"])
        if selected and selected in q["scores"]:
            for t, s in q["scores"][selected].items():
                type_scores[t] += s

    st.session_state.scores = type_scores
    st.session_state.result_type = max(type_scores, key=type_scores.get)


def _reset_quiz_progress():
    st.session_state.current_q = 0
    st.session_state.answers = {}
    st.session_state.scores = {}
    st.session_state.result_type = ""