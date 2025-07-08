import os
import requests
import streamlit as st

# BACKEND_URL="http://localhost:8000/"

# in frontend/streamlit_app.py
BACKEND_URL = "https://research-assistant-jasminbot.uc.r.appspot.com"
# -----------------------------------------------------------------------------
# Config
# -----------------------------------------------------------------------------
# BACKEND_URL = os.getenv(
#     "BACKEND_URL",
#     # "https://research-assistant-jasminbot.uc.r.appspot.com",  # default backend
# )

st.set_page_config(page_title="JasminBot", page_icon="🤖")

# -----------------------------------------------------------------------------
# Helper functions
# -----------------------------------------------------------------------------
@st.cache_data(show_spinner=False)
def post_chat(message: str):
    """Call the backend and return (answer, intent)."""
    try:
        r = requests.post(
            f"{BACKEND_URL}/api/chat",
            json={"message": message},
            timeout=60,
        )
        r.raise_for_status()
        data = r.json()
        # Some back-ends may return intent in different keys or capitalisation
        intent = (
            data.get("intent") or
            data.get("user_intent") or
            data.get("Intent") or
            data.get("userIntent")
        )
        return data.get("response", "No response"), intent
    except Exception as exc:
        return f"❌ Error contacting backend: {exc}", None

# -----------------------------------------------------------------------------
# Session state initialisation
# -----------------------------------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []  # (role, content)
    st.session_state.intent = None

# -----------------------------------------------------------------------------
# Layout
# -----------------------------------------------------------------------------

# ---------------------  WELCOME MESSAGE  ---------------------
if "welcome_shown" not in st.session_state:
    st.session_state.welcome_shown = True
    st.markdown(
        """
**JasminBot — Connecting STEM Innovators with Investors**  
_Specialized in Food & Beverage, Education, and Generative&nbsp;AI sectors_

💡 **Ask me about:**

• **Companies similar to Jasmin Groups** (investor platforms, accelerators)  
  → *Get structured info: legal structure, industry focus, service overlap*

• **Investment opportunities** in **FoodTech, EdTech, and AI** sectors  
  → *Receive market analysis with funding landscape and next steps*

• **Our consulting, mentorship, and due-diligence services**  
  → *Learn capabilities, target audience, and how to get started*
        """,
        unsafe_allow_html=False,
    )

# -------------------------------------------------------------

for idx, (role, content) in enumerate(st.session_state.messages):
    with st.chat_message(role):
        # Show intent tag on the assistant message that originated it (if any)
        if role == "assistant" and idx == len(st.session_state.messages) - 1 and st.session_state.get("intent"):
            st.markdown(
                f"<span style='background:#00a36e;color:white;padding:2px 8px;border-radius:12px;font-size:0.75rem;float:right;'>{st.session_state.intent}</span>",
                unsafe_allow_html=True,
            )
        st.markdown(content)

# -------------------------------------------------------------

# Footer – fixed bottom-right
st.markdown(
    """
    <style>
        .footer-badge {
            position: fixed;
            right: 12px;
            bottom: 60px; /* sit above Streamlit chat input */
            font-size: 0.75rem;
            color: #6c6c6c;
            z-index: 9998;
            pointer-events: none;
        }
    </style>
    <div class="footer-badge">© JasminBot – All rights reserved</div>
    """,
    unsafe_allow_html=True,
)

# Chat input box (Streamlit 1.25+). Fallback to text_input for older versions.
prompt = st.chat_input("Type your question and press Enter …")

if prompt:
    # Show user message immediately
    st.session_state.messages.append(("user", prompt))
    with st.chat_message("user"):
        st.markdown(prompt)

    # Call backend
    with st.spinner("Thinking …"):
        answer, intent = post_chat(prompt)

    # Save assistant reply and intent
    st.session_state.messages.append(("assistant", answer))
    if intent:
        st.session_state.intent = intent  # update badge

    with st.chat_message("assistant"):
        st.markdown(answer)

# --------------- Render fixed intent badge (always) ---------------
if st.session_state.get("intent"):
    st.markdown(
        f"""
        <style>
            .intent-badge {{
                position: fixed;
                top: 12px;
                left: 12px;
                background: #00a36e;
                color: white;
                padding: 6px 14px;
                border-radius: 18px;
                font-weight: 600;
                z-index: 9999;
            }}
        </style>
        <div class="intent-badge">{st.session_state.intent}</div>
        """,
        unsafe_allow_html=True,
    ) 