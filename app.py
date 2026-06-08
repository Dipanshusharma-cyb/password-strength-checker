import streamlit as st
import re
import random
import string
import base64

st.set_page_config(
    page_title="Password Strength Checker",
    page_icon="🔐",
    layout="centered"
)

def get_base64_image(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

bg_image = get_base64_image("background.jpg")

st.markdown(
    f"""
    <style>

    .stApp {{
        background-image: url("data:image/jpg;base64,{bg_image}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    .block-container {{
        background: rgba(0, 0, 0, 0.70);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0px 0px 25px cyan;
        margin-top: 2rem;
    }}

    h1, h2, h3 {{
        color: #00ffff;
        text-align: center;
    }}

    .stButton > button {{
        width: 100%;
        border-radius: 10px;
        font-weight: bold;
    }}

    </style>
    """,
    unsafe_allow_html=True
)

# Welcome Box
st.markdown("""
<div style="
background: rgba(0,0,0,0.85);
padding:20px;
border-radius:20px;
text-align:center;
font-size:35px;
font-weight:bold;
color:#00ffff;
box-shadow:0 0 20px cyan;
margin-bottom:20px;
">

✨ WELCOME BUDDYYY 😎 ✨

</div>
""", unsafe_allow_html=True)

st.title("🔐 Password Strength Checker")
st.write("### Cyber Security Password Analyzer")

def check_password_strength(password):
    score = 0

    checks = {
        "At least 8 characters": len(password) >= 8,
        "Uppercase letter": bool(re.search(r"[A-Z]", password)),
        "Lowercase letter": bool(re.search(r"[a-z]", password)),
        "Number": bool(re.search(r"\d", password)),
        "Special character": bool(re.search(r"[@$!%*?&]", password))
    }

    for value in checks.values():
        if value:
            score += 1

    return score, checks

def generate_password(length):
    chars = string.ascii_letters + string.digits + "@$!%*?&"
    return ''.join(random.choice(chars) for _ in range(length))

show_password = st.checkbox("👁 Show Password")

if show_password:
    password = st.text_input("Enter Password")
else:
    password = st.text_input("Enter Password", type="password")

length = st.slider(
    "Generated Password Length",
    min_value=8,
    max_value=24,
    value=12
)

if st.button("🔑 Generate Strong Password"):
    generated = generate_password(length)
    st.code(generated)

if password:

    score, checks = check_password_strength(password)

    st.subheader("📊 Password Strength")

    st.progress(score / 5)

    st.metric("Score", f"{score}/5")

    if score <= 2:
        st.error("WEAK ❌")
    elif score <= 4:
        st.warning("MEDIUM ⚠️")
    else:
        st.success("STRONG ✅")

    st.subheader("🔍 Security Checklist")

    for rule, passed in checks.items():
        if passed:
            st.write(f"✅ {rule}")
        else:
            st.write(f"❌ {rule}")

    if score == 5:
        st.balloons()
        st.success("Excellent Password Security! 🔥")

else:
    st.info("Enter a password to begin analysis.")
