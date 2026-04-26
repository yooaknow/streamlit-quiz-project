import streamlit as st
from components import show_header
from data import load_result_data


def render():
    show_header()

    results = load_result_data()
    result_type = st.session_state.result_type
    r = results[result_type]
    scores = st.session_state.scores

    # 결과 타입별 이미지 매핑
    result_image_map = {
        "impulse": "assets/result2.png",
        "coupang": "assets/result3.png",
        "small_happy": "assets/result1.png",
        "saving": "assets/result4.png",
    }

    # 결과 이미지 출력
    st.image(result_image_map[result_type], use_container_width=True)

    # 유형 설명
    with st.container(border=True):
        st.markdown(f"### {r['emoji']} {r['title']}")
        st.markdown(f"**📖 유형 설명**\n\n{r['desc']}")
        st.markdown(f"\n{r['tip']}")

    # 점수 분포
    st.markdown("### 📊 유형별 점수 분포")
    max_score = max(scores.values()) if max(scores.values()) > 0 else 1

    for t, s in sorted(scores.items(), key=lambda x: x[1], reverse=True):
        emoji = results[t]["emoji"]
        st.markdown(f"{emoji} **{results[t]['title']}**")
        st.progress(s / max_score, text=f"{s}점")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("다시 테스트하기", use_container_width=True, type="primary"):
            _reset_quiz()
            st.session_state.page = "quiz"
            st.rerun()

    with col2:
        if st.button("홈으로", use_container_width=True):
            _reset_quiz()
            st.session_state.page = "home"
            st.rerun()

    st.markdown("")

    if st.button("로그아웃", use_container_width=True):
        _logout()
        st.rerun()


def _reset_quiz():
    """퀴즈 결과와 진행 상태를 초기화합니다."""
    st.session_state.current_q = 0
    st.session_state.answers = {}
    st.session_state.scores = {}
    st.session_state.result_type = ""

    for i in range(1, 6):
        st.session_state.pop(f"q{i}", None)


def _logout():
    """로그아웃 처리: 세션 전체를 초기화합니다."""
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.session_state.page = "home"
    st.session_state.current_q = 0
    st.session_state.answers = {}
    st.session_state.scores = {}
    st.session_state.result_type = ""