import my_app as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="AIzaSyA_ylfWr7QGgqeEFK3ef68uf63UBFkwdfE")

model = genai.GenerativeModel('gemini-2.0-flash') # or 'gemini-2.0-pro'

# Initialize chat history
if "memory" not in st.session_state:
    st.session_state.memory = []

# Title
st.title("🤱 Mom Friend Chatbot")

# Input form
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("You:", placeholder="Ask me anything about pregnancy...")
    submit = st.form_submit_button("Send")

# Handle input
if submit and user_input:
    st.session_state.memory.append(f"User: {user_input}")

    prompt = (
        "You are a supportive, loving, slightly humorous 'Mom Friend' for a pregnant woman. "
        "You talk like a real mom would — warm, honest, and emotionally supportive. "
        "Keep your answers short, sweet, and helpful.\n\n"
        + "\n".join(st.session_state.memory) +
        "\nAI:"
    )

    response = model.generate_content(prompt)
    ai_reply = response.text.strip()

    st.session_state.memory.append(f"AI: {ai_reply}")

# Display chat history
for msg in st.session_state.memory:
    if msg.startswith("User:"):
        st.markdown(f"**👩 You:** {msg[6:]}")
    elif msg.startswith("AI:"):
        st.markdown(f"**🤱 Mom Friend:** {msg[4:]}")
