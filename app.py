import streamlit as st

st.set_page_config(page_title="ScamShield", page_icon="🛡️")

st.title("🛡️ ScamShield")
st.subheader("Detect Scam Messages Instantly")

st.markdown("---")
st.info("🚨 Protect yourself from phishing & fraud messages")

user_input = st.text_area("Enter Message", height=150)

if st.button("Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter a message!")
    else:
        st.progress(75)
        st.error("⚠️ High Risk: This looks like a scam message")
        
        st.markdown("### 🔍 Reasons:")
        st.write("- Contains urgent language")
        st.write("- Possible suspicious link")
        st.write("- Requests sensitive information")
