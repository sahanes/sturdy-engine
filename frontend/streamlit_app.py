# import os
# import requests
# import streamlit as st

# # BACKEND_URL="http://localhost:8000/"


# # -----------------------------------------------------------------------------
# # Config
# # -----------------------------------------------------------------------------
# BACKEND_URL = st.secrets.get("BACKEND_URL", "https://fallback-url.com")
# APP_DISPLAY_NAME = st.secrets.get("APP_DISPLAY_NAME", "JasminBot")

# st.set_page_config(page_title="JasminBot", page_icon="🤖")

# # -----------------------------------------------------------------------------
# # Helper functions
# # -----------------------------------------------------------------------------
# @st.cache_data(show_spinner=False)
# def post_chat(message: str):
#     """Call the backend and return (answer, intent)."""
#     try:
#         r = requests.post(
#             f"{BACKEND_URL}/api/chat",
#             json={"message": message},
#             timeout=60,
#         )
#         r.raise_for_status()
#         data = r.json()
#         # Some back-ends may return intent in different keys or capitalisation
#         intent = (
#             data.get("intent") or
#             data.get("user_intent") or
#             data.get("Intent") or
#             data.get("userIntent")
#         )
#         return data.get("response", "No response"), intent
#     except Exception as exc:
#         return f"❌ Error contacting backend: {exc}", None

# # -----------------------------------------------------------------------------
# # Session state initialisation
# # -----------------------------------------------------------------------------
# if "messages" not in st.session_state:
#     st.session_state.messages = []  # (role, content)
#     st.session_state.intent = None

# # -----------------------------------------------------------------------------
# # Layout
# # -----------------------------------------------------------------------------

# # ---------------------  WELCOME MESSAGE  ---------------------
# if "welcome_shown" not in st.session_state:
#     st.session_state.welcome_shown = True
#     st.markdown(
#         """
# **JasminBot — Connecting STEM Innovators with Investors**  
# _Specialized in Food & Beverage, Education, and Generative&nbsp;AI sectors_

# 💡 **Ask me about:**

# • **Companies similar to Jasmin Groups** (investor platforms, accelerators)  
#   → *Get structured info: legal structure, industry focus, service overlap*

# • **Investment opportunities** in **FoodTech, EdTech, and AI** sectors  
#   → *Receive market analysis with funding landscape and next steps*

# • **Our consulting, mentorship, and due-diligence services**  
#   → *Learn capabilities, target audience, and how to get started*
#         """,
#         unsafe_allow_html=False,
#     )

# # -------------------------------------------------------------

# for idx, (role, content) in enumerate(st.session_state.messages):
#     with st.chat_message(role):
#         # Show intent tag on the assistant message that originated it (if any)
#         if role == "assistant" and idx == len(st.session_state.messages) - 1 and st.session_state.get("intent"):
#             st.markdown(
#                 f"<span style='background:#00a36e;color:white;padding:2px 8px;border-radius:12px;font-size:0.75rem;float:right;'>{st.session_state.intent}</span>",
#                 unsafe_allow_html=True,
#             )
#         st.markdown(content)

# # -------------------------------------------------------------

# # Footer – fixed bottom-right
# st.markdown(
#     """
#     <style>
#         .footer-badge {
#             position: fixed;
#             right: 12px;
#             bottom: 60px; /* sit above Streamlit chat input */
#             font-size: 0.75rem;
#             color: #6c6c6c;
#             z-index: 9998;
#             pointer-events: none;
#         }
#     </style>
#     <div class="footer-badge">© JasminBot – All rights reserved</div>
#     """,
#     unsafe_allow_html=True,
# )

# # Chat input box (Streamlit 1.25+). Fallback to text_input for older versions.
# prompt = st.chat_input("Type your question and press Enter …")

# if prompt:
#     # Show user message immediately
#     st.session_state.messages.append(("user", prompt))
#     with st.chat_message("user"):
#         st.markdown(prompt)

#     # Call backend
#     with st.spinner("Thinking …"):
#         answer, intent = post_chat(prompt)

#     # Save assistant reply and intent
#     st.session_state.messages.append(("assistant", answer))
#     if intent:
#         st.session_state.intent = intent  # update badge

#     with st.chat_message("assistant"):
#         st.markdown(answer)

# # --------------- Render fixed intent badge (always) ---------------
# if st.session_state.get("intent"):
#     st.markdown(
#         f"""
#         <style>
#             .intent-badge {{
#                 position: fixed;
#                 top: 12px;
#                 left: 12px;
#                 background: #00a36e;
#                 color: white;
#                 padding: 6px 14px;
#                 border-radius: 18px;
#                 font-weight: 600;
#                 z-index: 9999;
#             }}
#         </style>
#         <div class="intent-badge">{st.session_state.intent}</div>
#         """,
#         unsafe_allow_html=True,
#     ) 
# import os
# import requests
# import streamlit as st
# import time

# # Use environment variable for the backend URL, with a local default
# # BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000/")
# BACKEND_URL = "http://localhost:8000/"
# # BACKEND_URL = "https://research-assistant-jasminbot.uc.r.appspot.com/"

# st.set_page_config(page_title="JasminBot", page_icon="🤖")

# # -----------------------------------------------------------------------------
# # Helper function to call the backend
# # -----------------------------------------------------------------------------
# # Use st.cache_data for functions that return the same output for the same input
# # This is useful for testing but should be used carefully in production chat apps.
# # For now, we will not cache the chat call to ensure it's always live.
# def post_chat(message: str):
#     """Call the backend and return the full response dictionary."""
#     try:
#         start_time = time.time()
#         r = requests.post(
#             f"{BACKEND_URL}/api/chat",
#             json={"message": message},
#             timeout=60,  
#         )
#         end_time = time.time()
        
#         r.raise_for_status()
#         data = r.json()
#         data["response_time"] = end_time - start_time
#         return data
        
#     except Exception as exc:
#         error_response = {
#             "response": f"❌ Error contacting backend: {exc}",
#             "intent": "Error",
#             "response_time": 0
#         }
#         return error_response

# # -----------------------------------------------------------------------------
# # Session state initialization
# # -----------------------------------------------------------------------------
# if "messages" not in st.session_state:
#     # `messages` will store a list of dictionaries for more structured data
#     st.session_state.messages = []

# # -----------------------------------------------------------------------------
# # UI Layout
# # -----------------------------------------------------------------------------

# # Welcome message - shown only once
# if not st.session_state.messages:
#     st.markdown(
#         """
#         **JasminBot — Connecting STEM Innovators with Investors**  
#         _Specialized in Food & Beverage, Education, and Generative AI sectors_

#         💡 **Ask me about:**

#         • **Companies similar to Jasmin Groups** (investor platforms, accelerators)  
#         • **Investment opportunities** in **FoodTech, EdTech, and AI** sectors  
#         • **Our consulting, mentorship, and due-diligence services**
#         """,
#         unsafe_allow_html=False,
#     )

# # Display chat history
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         # ✅ CORRECTED LOGIC: Display the intent badge with its corresponding message
#         if message["role"] == "assistant" and "intent" in message and message["intent"]:
#             st.markdown(
#                 f"<div style='text-align: right; width: 100%;'><span style='background:#00a36e;color:white;padding:2px 8px;border-radius:12px;font-size:0.75rem;'>{message['intent']}</span></div>",
#                 unsafe_allow_html=True,
#             )
#         st.markdown(message["content"])
#         if message["role"] == "assistant" and "response_time" in message and message["response_time"] > 0:
#             st.caption(f"⏱️ Response time: {message['response_time']:.2f} seconds")


# # Chat input
# if prompt := st.chat_input("Ask about startups, investing, or our services..."):
#     # Add user message to state and display it
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.markdown(prompt)

#     # Get bot response
#     with st.chat_message("assistant"):
#         with st.spinner("Thinking..."):
#             full_response = post_chat(prompt)
            
#             # Extract data from the backend response
#             answer = full_response.get("response", "I'm sorry, I encountered an error.")
#             intent = full_response.get("intent", None)
#             response_time = full_response.get("response_time", 0)

#             # Display the intent badge for the new message
#             if intent:
#                 st.markdown(
#                     f"<div style='text-align: right; width: 100%;'><span style='background:#00a36e;color:white;padding:2px 8px;border-radius:12px;font-size:0.75rem;'>{intent}</span></div>",
#                     unsafe_allow_html=True,
#                 )
            
#             st.markdown(answer)
#             if response_time > 0:
#                 st.caption(f"⏱️ Response time: {response_time:.2f} seconds")

#             # Add the complete assistant message to state for history
#             st.session_state.messages.append({
#                 "role": "assistant",
#                 "content": answer,
#                 "intent": intent,
#                 "response_time": response_time
#             })
# import os
# import requests
# import streamlit as st
# import time
# import re

# # Use environment variable for the backend URL, with a local default
# BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000/")

# st.set_page_config(page_title="JasminBot", page_icon="🤖")

# # -----------------------------------------------------------------------------
# # Helper function to call the backend
# # -----------------------------------------------------------------------------
# def post_chat(message: str):
#     """Call the backend and return the full response dictionary."""
#     try:
#         start_time = time.time()
#         r = requests.post(
#             f"{BACKEND_URL}/api/chat",
#             json={"message": message},
#             timeout=60,  
#         )
#         end_time = time.time()
        
#         r.raise_for_status()
#         data = r.json()
#         data["response_time"] = end_time - start_time
#         return data
        
#     except Exception as exc:
#         error_response = {
#             "response": f"❌ Error contacting backend: {exc}",
#             "intent": "Error",
#             "response_time": 0,
#             "references": "" # Ensure references key exists in error case
#         }
#         return error_response

# # -----------------------------------------------------------------------------
# # Session state initialization
# # -----------------------------------------------------------------------------
# if "messages" not in st.session_state:
#     # Each message is a dictionary containing role, content, and optionally other data
#     st.session_state.messages = []

# # -----------------------------------------------------------------------------
# # UI Layout
# # -----------------------------------------------------------------------------

# # Welcome message
# if not st.session_state.messages:
#     st.markdown(
#         """
#         **JasminBot — Connecting STEM Innovators with Investors**
# Specialized in Food & Beverage, Education, and Generative AI sectors

# 💡 Ask me about:

# • Companies similar to Jasmin Groups (investor platforms, accelerators)
# → Get structured info: legal structure, industry focus, service overlap

# • Investment opportunities in FoodTech, EdTech, and AI sectors
# → Receive market analysis with funding landscape and next steps

# • Our consulting, mentorship, and due-diligence services
# → Learn capabilities, target audience, and how to get started
#         """,
#         unsafe_allow_html=False,
#     )

# # Display chat history from session state
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         # Display the intent badge if it exists for a message
#         if message["role"] == "assistant" and "intent" in message and message["intent"]:
#             st.markdown(
#                 f"<div style='text-align: right; width: 100%; margin-bottom: -20px;'><span style='background:#00a36e;color:white;padding:2px 8px;border-radius:12px;font-size:0.75rem;'>{message['intent']}</span></div>",
#                 unsafe_allow_html=True,
#             )
#         # Render the content, allowing HTML for our clickable links
#         st.markdown(message["content"], unsafe_allow_html=True)
#         if "response_time" in message and message["response_time"] > 0:
#             st.caption(f"⏱️ Response time: {message['response_time']:.2f} seconds")


# # Main chat input and response logic
# if prompt := st.chat_input("Ask about startups, investing, or our services..."):
#     # Add user's message to history and display it
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.markdown(prompt)

#     # Get and display the bot's response
#     with st.chat_message("assistant"):
#         with st.spinner("Thinking..."):
#             full_response = post_chat(prompt)
            
#             answer = full_response.get("response", "I'm sorry, I encountered an error.")
#             intent = full_response.get("intent", None)
#             response_time = full_response.get("response_time", 0)
#             references_text = full_response.get("references", "")
            
#             # This is the crucial logic block for making citations clickable
#             if references_text:
#                 ref_map = {}
#                 for line in references_text.strip().split('\n'):
#                     match = re.match(r'\[(\d+)\]\s*\[(.*?)\]\((.*?)\)', line)
#                     if match:
#                         num, title, url = match.groups()
#                         placeholder = f"[{num}]"
#                         # Using superscript for a cleaner look, with a hover title
#                         full_link = f'<sup><a href="{url}" target="_blank" title="{title}">[{num}]</a></sup>'
#                         ref_map[placeholder] = full_link
                
#                 # Replace all placeholders in the answer with the full HTML links
#                 # for placeholder, link in sorted(ref_map.items(), key=lambda x: len(x[0]), reverse=True):
#                 #     answer = answer.replace(placeholder, link)
#                 # NEW: Handle multiple citations like [1, 4] or [2, 3, 5]
#                 def replace_multiple_citations(text):
#                     pattern = r'\[(\d+(?:,\s*\d+)*)\]'
#                     def replacer(match):
#                         citation_nums = [num.strip() for num in match.group(1).split(',')]
#                         links = []
#                         for num in citation_nums:
#                             if f"[{num}]" in ref_map:
#                                 # Extract just the link part from the ref_map
#                                 link_html = ref_map[f"[{num}]"].replace('<sup>', '').replace('</sup>', '')
#                                 links.append(link_html)
#                             else:
#                                 links.append(f'[{num}]')  # Keep as plain text if no reference found
#                         return '<sup>' + ', '.join(links) + '</sup>'
                    
#                     return re.sub(pattern, replacer, text)
                
#                 answer = replace_multiple_citations(answer)

#             # Display the intent badge for the new message
#             if intent and intent != "Greeting":
#                 st.markdown(
#                     f"<div style='text-align: right; width: 100%; margin-bottom: -20px;'><span style='background:#00a36e;color:white;padding:2px 8px;border-radius:12px;font-size:0.75rem;'>{intent}</span></div>",
#                     unsafe_allow_html=True,
#                 )
            
#             # Display the final, formatted answer (now with HTML links)
#             st.markdown(answer, unsafe_allow_html=True)
#             if response_time > 0:
#                 st.caption(f"⏱️ Response time: {response_time:.2f} seconds")

#             # Add the complete assistant message to the session state for history
#             st.session_state.messages.append({
#                 "role": "assistant",
#                 "content": answer, # Save the version with clickable links
#                 "intent": intent,
#                 "response_time": response_time
#             })
import os
import requests
import streamlit as st
import time
import re

try:
    from streamlit_js_eval import streamlit_js_eval  # type: ignore
except ImportError:
    streamlit_js_eval = None
        
# Use environment variable for the backend URL, with a local default
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000/")

st.set_page_config(page_title="JasminBot", page_icon="🤖")

# -----------------------------------------------------------------------------
# Helper function to call the backend
# -----------------------------------------------------------------------------
# def post_chat(message: str):
#     """Call the backend and return the full response dictionary."""
#     try:
#         start_time = time.time()
#         r = requests.post(
#             f"{BACKEND_URL}/api/chat",
#             json={"message": message},
#             timeout=300,  # 5 minutes for comprehensive research and guidance
#         )
#         end_time = time.time()
        
#         r.raise_for_status()
#         data = r.json()
#         data["response_time"] = end_time - start_time
#         return data
        
#     except Exception as exc:
#         error_response = {
#             "response": f"❌ Error contacting backend: {exc}",
#             "intent": "Error",
#             "response_time": 0,
#             "references": "" # Ensure references key exists in error case
#         }
#         return error_response

# # -----------------------------------------------------------------------------
# # Session state initialization
# # -----------------------------------------------------------------------------
# if "messages" not in st.session_state:
#     # Each message is a dictionary containing role, content, and optionally other data
#     st.session_state.messages = []

# # -----------------------------------------------------------------------------
# # UI Layout
# # -----------------------------------------------------------------------------

# # Welcome message
# if not st.session_state.messages:
#     st.markdown(
#         """
#         **JasminBot — Connecting STEM Innovators with Investors**
# Specialized in Food & Beverage, Education, and Generative AI sectors

# 💡 Ask me about:

# • Companies similar to Jasmin Groups (investor platforms, accelerators)
# → Get structured info: legal structure, industry focus, service overlap

# • Investment opportunities in FoodTech, EdTech, and AI sectors
# → Receive market analysis with funding landscape and next steps

# • Our consulting, mentorship, and due-diligence services
# → Learn capabilities, target audience, and how to get started
#         """,
#         unsafe_allow_html=False,
#     )

# # Display chat history from session state
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         # Display the intent badge if it exists for a message
#         if message["role"] == "assistant" and "intent" in message and message["intent"]:
#             st.markdown(
#                 f"<div style='text-align: right; width: 100%; margin-bottom: -20px;'><span style='background:#00a36e;color:white;padding:2px 8px;border-radius:12px;font-size:0.75rem;'>{message['intent']}</span></div>",
#                 unsafe_allow_html=True,
#             )
#         # Render the content, allowing HTML for our clickable links
#         st.markdown(message["content"], unsafe_allow_html=True)
#         if "response_time" in message and message["response_time"] > 0:
#             st.caption(f"⏱️ Response time: {message['response_time']:.2f} seconds")


# # Main chat input and response logic
# if prompt := st.chat_input("Ask about startups, investing, or our services..."):
#     # Add user's message to history and display it
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.markdown(prompt)

#     # Get and display the bot's response
#     with st.chat_message("assistant"):
#         with st.spinner("Thinking..."):
#             full_response = post_chat(prompt)
            
#             answer = full_response.get("response", "I'm sorry, I encountered an error.")
#             intent = full_response.get("intent", None)
#             response_time = full_response.get("response_time", 0)
#             references_text = full_response.get("references", "")
            
#             # This is the crucial logic block for making citations clickable
#             if references_text:
#                 ref_map = {}
#                 for line in references_text.strip().split('\n'):
#                     match = re.match(r'\[(\d+)\]\s*\[(.*?)\]\((.*?)\)', line)
#                     if match:
#                         num, title, url = match.groups()
#                         placeholder = f"[{num}]"
#                         # Using superscript for a cleaner look, with a hover title
#                         full_link = f'<sup><a href="{url}" target="_blank" title="{title}">[{num}]</a></sup>'
#                         ref_map[placeholder] = full_link
                
#                 # Replace all placeholders in the answer with the full HTML links
#                 # for placeholder, link in sorted(ref_map.items(), key=lambda x: len(x[0]), reverse=True):
#                 #     answer = answer.replace(placeholder, link)
#                 # NEW: Handle multiple citations like [1, 4] or [2, 3, 5]
#                 def replace_multiple_citations(text):
#                     pattern = r'\[(\d+(?:,\s*\d+)*)\]'
#                     def replacer(match):
#                         citation_nums = [num.strip() for num in match.group(1).split(',')]
#                         links = []
#                         for num in citation_nums:
#                             if f"[{num}]" in ref_map:
#                                 # Extract just the link part from the ref_map
#                                 link_html = ref_map[f"[{num}]"].replace('<sup>', '').replace('</sup>', '')
#                                 links.append(link_html)
#                             else:
#                                 links.append(f'[{num}]')  # Keep as plain text if no reference found
#                         return '<sup>' + ', '.join(links) + '</sup>'
                    
#                     return re.sub(pattern, replacer, text)
                
#                 answer = replace_multiple_citations(answer)

#             # Display the intent badge for the new message
#             # if intent and intent != "Greeting":
#             #     st.markdown(
#             #         f"<div style='text-align: right; width: 100%; margin-bottom: -20px;'><span style='background:#00a36e;color:white;padding:2px 8px;border-radius:12px;font-size:0.75rem;'>{intent}</span></div>",
#             #         unsafe_allow_html=True,
#             #     )
            
#             # Display the final, formatted answer (now with HTML links)
#             st.markdown(answer, unsafe_allow_html=True)
#             if response_time > 0:
#                 st.caption(f"⏱️ Response time: {response_time:.2f} seconds")

#             # Add the complete assistant message to the session state for history
#             st.session_state.messages.append({
#                 "role": "assistant",
#                 "content": answer, # Save the version with clickable links
#                 # "intent": intent,
#                 "response_time": response_time
#             })
def post_chat(message: str, thread_id: str):
    """Call the backend and return the full response dictionary."""
    try:
        start_time = time.time()
        payload = {
            "message": message,
            "session_id": thread_id.replace("session_", ""),
        }
        r = requests.post(
            f"{BACKEND_URL}/api/chat",
            json=payload,
            timeout=300,  # 5 minutes for comprehensive research and guidance
        )
        end_time = time.time()
        
        r.raise_for_status()
        data = r.json()
        data["response_time"] = end_time - start_time
        return data
        
    except Exception as exc:
        error_response = {
            "response": f"❌ Error contacting backend: {exc}",
            "intent": "Error",
            "response_time": 0,
            "references": "" # Ensure references key exists in error case
        }
        return error_response

# -----------------------------------------------------------------------------
# Session state initialization
# -----------------------------------------------------------------------------
if "messages" not in st.session_state:
    # Each message is a dictionary containing role, content, and optionally other data
    st.session_state.messages = []

# Ensure persistent thread_id for this browser tab using localStorage (survives hard refresh)
def _get_or_create_thread_id():
    if streamlit_js_eval is None:
        return f"session_{uuid.uuid4().hex[:12]}"
    existing = streamlit_js_eval(js_expressions="localStorage.getItem('thread_id')")
    if existing:
        return existing
    new_id = f"session_{uuid.uuid4().hex[:12]}"
    streamlit_js_eval(js_expressions=f"localStorage.setItem('thread_id', '{new_id}')")
    return new_id

if "thread_id" not in st.session_state:
    st.session_state.thread_id = _get_or_create_thread_id()

# We let backend assign user_id if not provided

# -----------------------------------------------------------------------------
# UI Layout
# -----------------------------------------------------------------------------

# Welcome message
if not st.session_state.messages:
    st.markdown(
        """
        **JasminBot — Connecting STEM Innovators with Investors**
Specialized in Food & Beverage, Education, and Generative AI sectors

💡 Ask me about:

• Companies similar to Jasmin Groups (investor platforms, accelerators)
→ Get structured info: legal structure, industry focus, service overlap

• Investment opportunities in FoodTech, EdTech, and AI sectors
→ Receive market analysis with funding landscape and next steps

• Our consulting, mentorship, and due-diligence services
→ Learn capabilities, target audience, and how to get started
        """,
        unsafe_allow_html=False,
    )

# Display chat history from session state
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        # Display the intent badge if it exists for a message
        if message["role"] == "assistant" and "intent" in message and message["intent"]:
            st.markdown(
                f"<div style='text-align: right; width: 100%; margin-bottom: -20px;'><span style='background:#00a36e;color:white;padding:2px 8px;border-radius:12px;font-size:0.75rem;'>{message['intent']}</span></div>",
                unsafe_allow_html=True,
            )
        # Render the content, allowing HTML for our clickable links
        st.markdown(message["content"], unsafe_allow_html=True)
        if "response_time" in message and message["response_time"] > 0:
            st.caption(f"⏱️ Response time: {message['response_time']:.2f} seconds")


# Main chat input and response logic
if prompt := st.chat_input("Ask about startups, investing, or our services..."):
    # Add user's message to history and display it
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get and display the bot's response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            full_response = post_chat(prompt, st.session_state.thread_id)
            
            answer = full_response.get("response", "I'm sorry, I encountered an error.")
            intent = full_response.get("intent", None)
            response_time = full_response.get("response_time", 0)
            references_text = full_response.get("references", "")
            
            # This is the crucial logic block for making citations clickable
            if references_text:
                ref_map = {}
                for line in references_text.strip().split('\n'):
                    match = re.match(r'\[(\d+)\]\s*\[(.*?)\]\((.*?)\)', line)
                    if match:
                        num, title, url = match.groups()
                        placeholder = f"[{num}]"
                        # Using superscript for a cleaner look, with a hover title
                        full_link = f'<sup><a href="{url}" target="_blank" title="{title}">[{num}]</a></sup>'
                        ref_map[placeholder] = full_link
                
                # Replace all placeholders in the answer with the full HTML links
                # for placeholder, link in sorted(ref_map.items(), key=lambda x: len(x[0]), reverse=True):
                #     answer = answer.replace(placeholder, link)
                # NEW: Handle multiple citations like [1, 4] or [2, 3, 5]
                def replace_multiple_citations(text):
                    pattern = r'\[(\d+(?:,\s*\d+)*)\]'
                    def replacer(match):
                        citation_nums = [num.strip() for num in match.group(1).split(',')]
                        links = []
                        for num in citation_nums:
                            if f"[{num}]" in ref_map:
                                # Extract just the link part from the ref_map
                                link_html = ref_map[f"[{num}]"].replace('<sup>', '').replace('</sup>', '')
                                links.append(link_html)
                            else:
                                links.append(f'[{num}]')  # Keep as plain text if no reference found
                        return '<sup>' + ', '.join(links) + '</sup>'
                    
                    return re.sub(pattern, replacer, text)
                
                answer = replace_multiple_citations(answer)

            # Display the intent badge for the new message
            # if intent and intent != "Greeting":
            #     st.markdown(
            #         f"<div style='text-align: right; width: 100%; margin-bottom: -20px;'><span style='background:#00a36e;color:white;padding:2px 8px;border-radius:12px;font-size:0.75rem;'>{intent}</span></div>",
            #         unsafe_allow_html=True,
            #     )
            
            # Display the final, formatted answer (now with HTML links)
            st.markdown(answer, unsafe_allow_html=True)
            if response_time > 0:
                st.caption(f"⏱️ Response time: {response_time:.2f} seconds")

            # Add the complete assistant message to the session state for history
            st.session_state.messages.append({
                "role": "assistant",
                "content": answer, # Save the version with clickable links
                # "intent": intent,
                "response_time": response_time
            })
