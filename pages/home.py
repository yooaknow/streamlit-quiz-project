import streamlit as st
from components import show_header

def render():
    show_header()

    st.markdown(
        """
        <style>
        .main-wrap {
            max-width: 600px;
            margin: 0 auto;
        }

        .info-card {
            background: linear-gradient(135deg, #EEF3DF 0%, #DDEACB 100%);
            border: 1px solid #D5E4C2;
            border-radius: 22px;
            padding: 1.1rem 1.4rem;
            margin-bottom: 2.2rem;
            color: #3F4A35;
            box-shadow: 0 8px 24px rgba(80, 100, 60, 0.08);
        }

        .info-label {
            font-size: 0.78rem;
            font-weight: 700;
            color: #6F815C;
            margin-bottom: 0.25rem;
        }

        .info-name {
            font-size: 0.95rem;
            font-weight: 800;
        }

        .type-card {
            background: #FFFFFF;
            border: 1px solid #E1E8D5;
            border-radius: 18px;
            padding: 1.1rem;
            min-height: 92px;
            box-shadow: 0 6px 18px rgba(80, 100, 60, 0.06);
        }

        .type-title {
            font-size: 0.95rem;
            font-weight: 800;
            color: #33412A;
            margin-bottom: 0.45rem;
        }

        .type-desc {
            font-size: 0.85rem;
            color: #68725E;
            line-height: 1.5;
        }

        div.stButton > button {
            background: #8BAA6F !important;
            color: white !important;
            border: none !important;
            border-radius: 999px !important;
            height: 3rem !important;
            font-weight: 800 !important;
            box-shadow: 0 8px 18px rgba(139, 170, 111, 0.28);
        }

        div.stButton > button:hover {
            background: #78995E !important;
            color: white !important;
        }

        hr {
            margin: 2rem 0;
            border-color: #E1E8D5;
        }
        </style>

        <div class="main-wrap">
        """,
        unsafe_allow_html=True,
    )


    st.image("assets/main.png", use_container_width=True)

    st.markdown("---")

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown(
            """
            <div class="type-card">
                <div class="type-title">🛍️ 소비 충동형</div>
                <div class="type-desc">통장은 월급 환승역</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="type-card">
                <div class="type-title">📦 쿠팡 VIP형</div>
                <div class="type-desc">집이 곧 물류센터</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)

    col3, col4 = st.columns(2, gap="large")

    with col3:
        st.markdown(
            """
            <div class="type-card">
                <div class="type-title">🍜 소확행 파산형</div>
                <div class="type-desc">작은 행복, 큰 카드값</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col4:
        st.markdown(
            """
            <div class="type-card">
                <div class="type-title">🐢 은근 절약형</div>
                <div class="type-desc">통장을 의외로 잘 지킴</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<br><br>", unsafe_allow_html=True)

    _, col_mid, _ = st.columns([1, 2, 1])
    with col_mid:
        if st.button("테스트 시작하기", use_container_width=True, type="primary"):
            st.session_state.page = "quiz" if st.session_state.logged_in else "login"
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)