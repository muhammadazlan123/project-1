import streamlit as st
import re

def password_strength(password):
    strength = 0
    
    # Length check
    if len(password) >= 8:
        strength += 1
    
    # Upper and lower case check
    if re.search("[a-z]", password) and re.search("[A-Z]", password):
        strength += 1
    
    # Digit check
    if re.search("\d", password):
        strength += 1
    
    # Special character check
    if re.search("[@$!%*?&]", password):
        strength += 1
    
    return strength

def main():
    st.title("🔐PASSWORD STRENGTH METER 👨‍🏫")
    st.write("Enter a password to check its strength!")
    
    password = st.text_input("Please Enter your password ✍️", type="password")
    
    if password:
        strength = password_strength(password)
        
        if strength == 4:
            st.success("✅ Strong Password ➡️ Very Good👍")
        elif strength == 3:
            st.warning("⚠️ Moderate Password ➡️ Just Addind Key Feature📈")
        else:
            st.error("❌ Weak Password ➡️ Try Strong Password All The Best💪")
        
        st.progress(strength / 4)

if __name__ == "__main__":
    main()
