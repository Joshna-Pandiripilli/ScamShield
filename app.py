import streamlit as st

st.set_page_config(page_title="ScamShield", page_icon="🛡️")

st.title("🛡️ ScamShield")
st.subheader("Detect Scam Messages Instantly")

st.markdown("---")
st.info("🚨 Protect yourself from phishing & fraud messages")

user_input = st.text_area("Enter Message", height=150)

# 🚨 Scam keywords
scam_keywords = [
    "urgent", "click here", "win money", "free", 
    "otp", "password", "bank", "lottery", "prize",
    "limited time", "offer", "verify account"
]

if st.button("Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter a message!")
    else:
        message = user_input.lower()
        score = 0
        found_keywords = []

        for word in scam_keywords:
            if word in message:
                score += 1
                found_keywords.append(word)

        # Risk calculation
        if score == 0:
            st.success("✅ Low Risk: Looks safe")
        elif score <= 2:
            st.warning("⚠️ Medium Risk: Be cautious")
        else:
            st.error("🚨 High Risk: Possible scam detected")

        # Show reasons
        if found_keywords:
            st.markdown("### 🔍 Suspicious keywords found:")
            for word in found_keywords:
                st.write(f"- {word}")
