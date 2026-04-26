import streamlit as st
from pages import home, login, quiz, result


def init_session():
    """세션 상태 초기값을 설정합니다."""
    defaults = {
        "logged_in": False,
        "username": "",
        "page": "home",   # home | login | quiz | result
        "answers": {},
        "scores": {},
        "result_type": "",
        "current_q": 0,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def main():
    st.set_page_config(
        page_title="금융 소비 습관 유형 테스트",
        page_icon="📚",
        layout="centered",
    )

    init_session()

    # 페이지 라우팅
    page = st.session_state.page

    if page == "home":
        home.render()
    elif page == "login":
        login.render()
    elif page == "quiz":
        # 로그인 없이 quiz 접근 시 login으로 리다이렉트
        if not st.session_state.logged_in:
            st.session_state.page = "login"
            st.rerun()
        quiz.render()
    elif page == "result":
        result.render()


if __name__ == "__main__":
    main()
