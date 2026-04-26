import streamlit as st
from config import STUDENT_ID, STUDENT_NAME


def show_header():
    st.markdown(
        f"""
        <div style="
            background:#FFFFFF;
            border:1px solid #E5E7EB;
            border-radius:16px;
            padding:1rem 1.3rem;
            margin-bottom:1.8rem;
            display:flex;
            justify-content:space-between;
            align-items:center;
            box-shadow: 0 4px 12px rgba(0,0,0,0.04);
        ">
            <div>
                <p style="
                    margin:0;
                    font-size:0.75rem;
                    color:#9CA3AF;
                    font-weight:600;
                ">
                    제출자 정보
                </p>
                <p style="
                    margin:0;
                    font-weight:800;
                    font-size:0.95rem;
                    color:#111827;
                ">
                    {STUDENT_ID} &nbsp;|&nbsp; {STUDENT_NAME}
                </p>
            </div>
            <div style="
                font-size:1.5rem;
                opacity:0.6;
            ">
                🎓
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )