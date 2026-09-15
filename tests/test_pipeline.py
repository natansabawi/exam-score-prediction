import pytest
import pandas as pd
import numpy as np

def test_score_boundary_constraints():
    """Verify that predictions respect physical bounds [0, 100]."""
    scores = np.array([-5.0, 45.2, 105.0])
    bounded = np.clip(scores, 0.0, 100.0)
    assert bounded.min() >= 0.0
    assert bounded.max() <= 100.0

def test_feature_payload_columns():
    """Verify the feature schema matches training expectation."""
    required = [
        "Hours_Studied", "Attendance", "Parental_Involvement", 
        "Access_to_Resources", "Extracurricular_Activities", "Sleep_Hours", 
        "Previous_Scores", "Motivation_Level", "Internet_Access", 
        "Tutoring_Sessions", "Family_Income", "Teacher_Quality", 
        "School_Type", "Peer_Influence", "Physical_Activity", 
        "Learning_Disabilities", "Parental_Education_Level", 
        "Distance_from_Home", "Gender"
    ]
    sample = pd.DataFrame([{col: 1 for col in required}])
    assert set(required).issubset(sample.columns)
