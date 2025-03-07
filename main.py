import streamlit as st
import re

# Page config
st.set_page_config(page_title="PassGuard: Password Strength Analyzer", page_icon="🛡️")

# Title and intro
st.title("🛡️ PassGuard: Password Strength Analyzer")
st.markdown("""
## Unleash the Power of Secure Passwords!  
Welcome to **PassGuard**, your go-to tool for analyzing password strength. Whether you're a casual user or a security enthusiast, this app helps you craft unbreakable passwords with real-time feedback and expert tips.  

Lock it down with a **bulletproof password** today! 🔒
""")

# Password input
password = st.text_input("Enter your password", type="password")

# Function to check password strength
def check_password_strength(password):
    feedback = []
    score = 0

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long!")

    # Uppercase and lowercase check
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should contain both upper and lowercase letters!")

    # Digit check
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Password should contain at least one digit (0-9)!")

    # Special character check
    special_chars = r'[!@#$%&*?]'
    if re.search(special_chars, password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character (e.g., !@#$%&*?)!")

    # Edge case: spaces
    if " " in password:
        feedback.append("Password should not contain spaces!")

    return score, feedback

# Main logic
if password:
    score, feedback = check_password_strength(password)

    # Strength evaluation
    if score == 4:
        st.success("🎉 Your password is **Strong**! You're a security pro!")
    elif score >= 2:
        st.warning("⚠️ Your password is **Medium**. Tweak it with the tips below!")
    else:
        st.error("❌ Your password is **Weak**. Time to level up!")

    # Display feedback
    if feedback:
        st.markdown("### Improvement Tips")
        for tip in feedback:
            st.write(f"- {tip}")

    # Strength meter 
    st.markdown("### Strength Meter")
    strength_percentage = (score / 4) * 100
    st.progress(int(strength_percentage))
else:
    st.info("Drop your password above to see how tough it is!")