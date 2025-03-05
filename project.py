import streamlit as st
import matplotlib.pyplot as plt

def calculate_daily_study_goal(total_material, days_remaining):
    if days_remaining <= 0:
        return "Invalid: Days remaining must be greater than 0."
    return total_material / days_remaining

def track_learning_progress(completed_topics, total_topics):
    if total_topics <= 0:
        return "Invalid: Total topics must be greater than 0."
    return (completed_topics / total_topics) * 100

def suggest_study_sessions(time_available, difficulty_level):
    if time_available <= 0:
        return "Invalid: Time available must be greater than 0."
    
    session_lengths = {"easy": 30, "medium": 45, "hard": 60}
    session_time = session_lengths.get(difficulty_level, 45)
    return time_available // session_time

def plot_progress(completed, total):
    fig, ax = plt.subplots()
    labels = ['Completed', 'Remaining']
    sizes = [completed, total - completed]
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#4CAF50', '#FFC107'])
    ax.axis('equal')
    st.pyplot(fig)

def main():
    st.title("📚 Personalized Study Planner & Progress Tracker")
    
    st.header("Daily Study Goal Calculator")
    total_material = st.number_input("Enter total study material (pages, chapters, etc.):", min_value=1)
    days_remaining = st.number_input("Enter days remaining:", min_value=1)
    if st.button("Calculate Daily Study Goal"):
        daily_goal = calculate_daily_study_goal(total_material, days_remaining)
        st.write(f"You need to study **{daily_goal:.2f}** units per day.")
    
    st.header("Track Learning Progress")
    completed_topics = st.number_input("Enter completed topics:", min_value=0)
    total_topics = st.number_input("Enter total topics:", min_value=1)
    if st.button("Check Progress"):
        progress = track_learning_progress(completed_topics, total_topics)
        st.write(f"You have completed **{progress:.2f}%** of your study plan.")
        plot_progress(completed_topics, total_topics)
    
    st.header("Study Session Suggestion")
    time_available = st.number_input("Enter available study time (minutes):", min_value=1)
    difficulty_level = st.selectbox("Select difficulty level:", ["easy", "medium", "hard"])
    if st.button("Get Study Session Plan"):
        sessions = suggest_study_sessions(time_available, difficulty_level)
        st.write(f"You can fit **{sessions}** study sessions in your available time.")

if __name__ == "__main__":
    main()
