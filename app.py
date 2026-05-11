# app.py
import streamlit as st
import time

st.set_page_config(page_title="Flower Surprise", page_icon="🌷", layout="centered")

# Session state
if "clicked" not in st.session_state:
    st.session_state.clicked = False

# CSS
st.markdown("""
<style>

html, body, [class*="css"]  {
    background-color: #fffafc;
    overflow: hidden;
}

.title {
    text-align: center;
    font-size: 30px;
    font-weight: bold;
    margin-top: 60px;
    color: #ff4b91;
}

.center-box {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 60px;
}

.flower {
    font-size: 150px;
    animation: bloom 3s ease forwards;
}

@keyframes bloom {
    0% {
        transform: scale(0.2) rotate(-10deg);
        opacity: 0;
    }

    50% {
        transform: scale(1.3) rotate(5deg);
        opacity: 1;
    }

    100% {
        transform: scale(1);
    }
}

.hide-behind {
    position: relative;
    animation: moveAway 3s forwards;
    font-size: 150px;
}

@keyframes moveAway {
    0% {
        left: 0;
        opacity: 1;
    }

    70% {
        left: 220px;
        opacity: 1;
    }

    100% {
        left: 320px;
        opacity: 0;
        transform: scale(0.5);
        filter: blur(8px);
    }
}

.message {
    text-align: center;
    font-size: 28px;
    margin-top: 60px;
    color: #444;
    animation: fadeIn 2s ease;
    line-height: 1.8;
}

.final {
    text-align: center;
    font-size: 38px;
    font-weight: bold;
    color: #ff4b91;
    margin-top: 80px;
    animation: fadeIn 3s ease;
}

.small-flower {
    font-size: 45px;
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }

    to {
        opacity: 1;
        transform: translateY(0px);
    }
}

.stButton {
    display: flex;
    justify-content: center;
}

div.stButton > button {
    background-color: #ff4b91;
    color: white;
    border-radius: 15px;
    border: none;
    padding: 14px 28px;
    font-size: 20px;
    transition: 0.3s;
}

div.stButton > button:hover {
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)

# Giao diện đầu
if not st.session_state.clicked:

    st.markdown(
        "<div class='title'> Bấm zô cái cục kia đi </div>",
        unsafe_allow_html=True
    )

    if st.button("Bấm nè ❤️"):
        st.session_state.clicked = True
        st.rerun()

# Animation
else:

    flower = st.empty()
    text = st.empty()

    # Chỉ hiện hoa
    flower.markdown(
        """
        <div class='center-box'>
            <div class='flower'>💐</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    time.sleep(3)

    # Hoa chạy đi rồi tan biến
    flower.markdown(
        """
        <div class='center-box'>
            <div class='hide-behind'>💐</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    time.sleep(4)

    flower.empty()

    # Lời thoại
    text.markdown(
        """
        <div class='message'>
            "Hoa vốn đã đẹp rồi…<br><br>
            nhưng gặp em xong mới biết thế nào là xinh thật sự 💐"
        </div>
        """,
        unsafe_allow_html=True
    )

    time.sleep(4)

    # Chúc cuối
    text.markdown(
        """
        <div class='final'>
            🌸 Chúc vợ làm việc vui vẻ 🌸
            <div class='small-flower'>🌷</div>
        </div>
        """,
        unsafe_allow_html=True
    )