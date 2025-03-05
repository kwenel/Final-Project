# Personalized Study Planner & Progress Tracker
## Video: 

## Overview
The **Personalized Study Planner & Progress Tracker** is a web-based tool built using **Streamlit** to help students create study plans, track progress, and optimize their study sessions. This application enables students to calculate their daily study goals, visualize learning progress, and receive recommendations on study sessions based on available time and difficulty level.

This project was developed as a final assignment, adhering to the following requirements:
- Implemented in **Python**.
- Uses **Streamlit** for the user interface.
- Includes a **main function** and three additional custom functions.
- Contains **unit tests** using `pytest`.
- All dependencies are listed in `requirements.txt`.

## Features
- **Daily Study Goal Calculator**: Determines how much material a student should study daily based on total material and time available.
- **Progress Tracker**: Computes and visually displays learning progress using a pie chart.
- **Study Session Planner**: Suggests study sessions based on available time and difficulty level.

## Project Structure
This repository contains the following files:

### `project.py`
This is the main application file that contains:
1. **`calculate_daily_study_goal(total_material, days_remaining)`**
   - Calculates how much study material needs to be covered each day.
   - Returns an error if `days_remaining` is zero or negative.

2. **`track_learning_progress(completed_topics, total_topics)`**
   - Computes the percentage of study progress.
   - If `total_topics` is zero, returns an error message.
   - Displays a **pie chart** visualization using `matplotlib` to show completed vs. remaining topics.

3. **`suggest_study_sessions(time_available, difficulty_level)`**
   - Determines how many study sessions a student can fit into their available time.
   - Supports different difficulty levels: `easy`, `medium`, `hard`.
   - Returns an error if `time_available` is zero or negative.

4. **`main()`**
   - Implements the **Streamlit UI**, allowing users to input data and view their study plan, progress, and suggested sessions interactively.
   - Uses `st.pyplot()` to render the progress pie chart.

### `test_project.py`
Contains **unit tests** for verifying the functionality of the three core functions:
- **`test_calculate_daily_study_goal()`**: Ensures correct division of study material and handles edge cases.
- **`test_track_learning_progress()`**: Verifies progress calculations and ensures invalid inputs are handled.
- **`test_suggest_study_sessions()`**: Checks session suggestions for various difficulty levels and input values.

### `requirements.txt`
Lists required Python libraries:
```
streamlit
pytest
matplotlib
```
These dependencies must be installed before running the application using:
```
pip install -r requirements.txt
```

## Design Decisions
### **Why Streamlit?**
Streamlit was chosen for its simplicity in building interactive data-driven applications. Unlike Flask or Django, it allows rapid prototyping without needing frontend development expertise.

### **Why Add Graphical Representations?**
Originally, the progress tracking was implemented using only percentages. However, to improve **user experience** and **visual clarity**, a **pie chart** was added using `matplotlib`. This makes it easier for students to see their progress at a glance.

### **Why Three Study Difficulty Levels?**
The `suggest_study_sessions` function uses **three difficulty levels** (`easy`, `medium`, `hard`) to ensure flexibility in session planning. This allows students to adjust their study sessions based on their subject's complexity and available time.

## Academic Integrity Notice
For this final project, the use of AI-based software ChatGPT, GitHub Copilot, Bing Chat as a **productivity-enhancing tool**. However, the **essence of the work must still be OUR own**. These tools were used to **amplify** productivity rather than replace personal effort.

## How to Run the Project

1. Navigate into the project directory:
   ```
   cd study-planner
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```
   streamlit run project.py
   ```

## Conclusion
The **Personalized Study Planner & Progress Tracker** is designed to help students manage their study plans efficiently. With interactive features, graphical progress tracking, and study session suggestions, it serves as a practical tool for anyone looking to improve their study habits. Future improvements could include **AI-based study recommendations** and **real-time collaboration features**. 

This project meets all rubric requirements while offering a user-friendly interface to support student productivity. 🚀

