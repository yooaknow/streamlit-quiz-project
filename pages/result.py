import streamlit as st

from components import show_header
from data import load_result_data


def render():
    # 👇 결과 진입 시 강제로 새로 시작 느낌 만들기
    if st.session_state.get("scroll_top", False):
        st.session_state.scroll_top = False
        st.empty()  # 강제 리렌더 트릭

    show_header()

    results = load_result_data()
    result_type = st.session_state.result_type
    r = results[result_type]
    scores = st.session_state.scores

    # 결과 이미지
    result_image_map = {
        "impulse": "assets/result2.png",
        "coupang": "assets/result3.png",
        "small_happy": "assets/result1.png",
        "saving": "assets/result4.png",
    }

    st.image(result_image_map[result_type], use_container_width=True)

    # 결과 카드
    with st.container(border=True):
        st.markdown(f"### {r['emoji']} {r['title']}")

        with st.expander("📖 유형 설명 자세히 보기"):
            st.write(r["desc"])

        with st.expander("💡 소비 개선 팁 보기"):
            st.write(r["tip"])

    # =========================
    # 📊 원형 그래프 (CSS)
    # =========================
    st.markdown("### 📊 유형별 점수 분포")

    score_items = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    total_score = sum(scores.values()) if sum(scores.values()) > 0 else 1

    colors = {
        "impulse": "#F6A6B2",
        "coupang": "#8DB7E8",
        "small_happy": "#F3C77B",
        "saving": "#9BBC7D",
    }

    start = 0
    gradient_parts = []

    for t, s in score_items:
        percent = s / total_score * 100
        end = start + percent
        gradient_parts.append(f"{colors[t]} {start:.1f}% {end:.1f}%")
        start = end

    gradient = ", ".join(gradient_parts)

    st.markdown(
        f"""
        <div style="
            max-width:340px;
            height:340px;
            margin:1.2rem auto;
            border-radius:50%;
            background:conic-gradient({gradient});
            position:relative;
            box-shadow:0 8px 24px rgba(0,0,0,0.06);
        ">
            <div style="
                position:absolute;
                width:160px;
                height:160px;
                background:white;
                border-radius:50%;
                top:50%;
                left:50%;
                transform:translate(-50%, -50%);
                display:flex;
                align-items:center;
                justify-content:center;
                font-weight:900;
                color:#33412A;
                text-align:center;
                line-height:1.4;
            ">
                나의<br>소비 유형
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # =========================
    # 📋 점수 카드
    # =========================
    st.markdown("#### 점수 상세")

    for t, s in score_items:
        percent = round(s / total_score * 100)

        st.markdown(
            f"""
            <div style="
                background:#FFFFFF;
                border:1px solid #E5E7EB;
                border-radius:14px;
                padding:0.85rem 1rem;
                margin-bottom:0.6rem;
                display:flex;
                justify-content:space-between;
                align-items:center;
            ">
                <div style="display:flex;align-items:center;gap:0.6rem;">
                    <span style="
                        width:12px;
                        height:12px;
                        border-radius:50%;
                        background:{colors[t]};
                        display:inline-block;
                    "></span>
                    <span style="font-weight:800;color:#33412A;">
                        {results[t]['emoji']} {results[t]['title']}
                    </span>
                </div>
                <span style="font-weight:900;color:#8BAA6F;">
                    {s}점 · {percent}%
                </span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")

    # 버튼
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
    st.session_state.current_q = 0
    st.session_state.answers = {}
    st.session_state.scores = {}
    st.session_state.result_type = ""

    for i in range(1, 6):
        st.session_state.pop(f"q{i}", None)


def _logout():
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.session_state.page = "home"
    st.session_state.current_q = 0
    st.session_state.answers = {}
    st.session_state.scores = {}
    st.session_state.result_type = ""