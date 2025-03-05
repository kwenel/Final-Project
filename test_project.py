import pytest
from project import calculate_daily_study_goal, track_learning_progress, suggest_study_sessions

def test_calculate_daily_study_goal():
    assert calculate_daily_study_goal(100, 10) == 10
    assert calculate_daily_study_goal(50, 5) == 10
    assert calculate_daily_study_goal(100, 0) == "Invalid: Days remaining must be greater than 0."

def test_track_learning_progress():
    assert track_learning_progress(5, 10) == 50.0
    assert track_learning_progress(3, 6) == 50.0
    assert track_learning_progress(0, 10) == 0.0
    assert track_learning_progress(5, 0) == "Invalid: Total topics must be greater than 0."

def test_suggest_study_sessions():
    assert suggest_study_sessions(90, "easy") == 3
    assert suggest_study_sessions(120, "hard") == 2
    assert suggest_study_sessions(60, "medium") == 1
    assert suggest_study_sessions(0, "medium") == "Invalid: Time available must be greater than 0."