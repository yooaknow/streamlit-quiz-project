import time
import streamlit as st
from components import show_header
from config import USERS


def render():
    show_header()

    st.markdown(
        """
        <style>
        .login-title {
            text-align:center;
            color:#111827;
            font-weight:900;
            margin-top:0.5rem;
        }

        .login-sub {
            text-align:center;
            color:#6B7280;
            margin-bottom:1.5rem;
        }

        .login-wrap {
            max-width:600px;
            margin:0 auto;
        }

        div[data-testid="stVerticalBlockBorderWrapper"] {
            background:#FFFFFF;
            border:1px solid #E5E7EB !important;
            border-radius:18px !important;
            box-shadow:0 6px 18px rgba(0,0,0,0.04);
            padding:0.8rem;
        }

        div[data-testid="stTextInput"] label {
            color:#111827 !important;
            font-weight:700 !important;
        }

        div[data-testid="stTextInput"] input {
            border-radius:12px !important;
            border:1px solid #E5E7EB !important;
        }

        div.stButton > button {
            border-radius:999px !important;
            height:2.8rem !important;
            font-weight:800 !important;
        }

        div.stButton > button[kind="primary"] {
            background:#8BAA6F !important;
            color:white !important;
            border:none !important;
            box-shadow:0 6px 16px rgba(139,170,111,0.25);
        }

        div.stButton > button[kind="primary"]:hover {
            background:#78995E !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <h2 class="login-title">🔐 로그인</h2>
        <p class="login-sub">테스트를 시작하려면 로그인이 필요합니다.</p>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="login-wrap">', unsafe_allow_html=True)

    with st.container(border=True):
        username = st.text_input("아이디", placeholder="student / admin / test")
        password = st.text_input("비밀번호", type="password", placeholder="비밀번호 입력")
        st.caption("🔑 테스트 계정: student/1234  |  admin/admin  |  test/test")

        if st.button("로그인", use_container_width=True, type="primary"):
            if username in USERS and USERS[username] == password:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.session_state.page = "quiz"
                st.success(f"환영합니다, {username}님! 🎉")
                time.sleep(0.8)
                st.rerun()
            else:
                st.error("❌ 아이디 또는 비밀번호가 올바르지 않습니다.")

    if st.button("← 홈으로", use_container_width=True):
        st.session_state.page = "home"
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)