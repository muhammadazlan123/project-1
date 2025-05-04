import streamlit as st

def main():
    # Title of the web app
    st.title("Growth Mindset Challenge")
    
    # Introduction section
    st.header("What is a Growth Mindset?")
    st.write(
        "A growth mindset is the belief that abilities and intelligence can be developed "
        "through hard work, perseverance, and learning from mistakes."
    )
    
    # Why adopt a growth mindset?
    st.header("Why Adopt a Growth Mindset?")
    st.markdown("""
    - **Embrace Challenges:** View obstacles as opportunities to learn.
    - **Learn from Mistakes:** Every mistake is a chance to improve.
    - **Persist Through Difficulties:** Stay determined even when things are tough.
    - **Celebrate Effort:** Recognize and reward the effort, not just the result.
    - **Keep an Open Mind:** Stay curious and adaptable.
    """)
    
    # How to practice a growth mindset
    st.header("How Can You Practice a Growth Mindset?")
    st.markdown("""
    - Set learning goals instead of just focusing on grades.
    - Reflect on what you've learned from both successes and failures.
    - Seek feedback and use it to improve.
    - Stay positive and believe in your ability to grow.
    """)
    
    # Interactive section for user input
    st.header("Your Growth Mindset Plan")
    goal = st.text_input("Set a learning goal for yourself:")
    challenge = st.text_area("Describe a recent challenge you faced and what you learned from it:")
    
    if st.button("Submit My Growth Plan"):
        st.success("Great job! Keep pushing forward with a growth mindset!")
        st.write("### Your Plan Summary:")
        st.write(f"- **Learning Goal:** {goal}")
        st.write(f"- **Recent Challenge:** {challenge}")
    
    # Conclusion
    st.header("Keep Growing!")
    st.write("Remember, every step forward is a step toward growth and success!")
    
if __name__ == "__main__":
    main()
