import streamlit as st
import pandas as pd

st.set_page_config(page_title="Rate My Course", layout="centered")

st.title("📚 Rate My Course")
st.write("Share your course experience and help other students choose!")

# Sidebar for course input
with st.sidebar:
    st.header("Course Information")
    
    # Subject category selection
    subject_category = st.radio(
        "Subject Category",
        options=["STEM", "Liberal Arts"],
        help="STEM courses are generally harder, Liberal Arts are generally easier"
    )
    
    # Course number (difficulty level)
    course_number = st.selectbox(
        "Course Number (Difficulty Level)",
        options=[100, 200, 300, 400],
        format_func=lambda x: f"{x}s - {'Easiest' if x == 100 else 'Easy' if x == 200 else 'Difficult' if x == 300 else 'Most Difficult'}"
    )
    
    st.divider()
    st.caption("100s = Easiest | 400s = Most Difficult")

# Main content area
col1, col2 = st.columns(2)

with col1:
    st.metric("Subject Category", subject_category)
    
with col2:
    st.metric("Course Level", f"{course_number}s")

st.divider()

# Course details form
st.subheader("Course Details")

col1, col2 = st.columns(2)

with col1:
    course_code = st.text_input("Course Code (e.g., CS101, BIO201)")
    
with col2:
    course_name = st.text_input("Course Name")

# Rating section
st.subheader("Your Rating")

col1, col2, col3 = st.columns(3)

with col1:
    difficulty = st.slider("Difficulty Level", 1, 5, 3, help="1 = Very Easy, 5 = Very Hard")
    
with col2:
    usefulness = st.slider("Usefulness", 1, 5, 3, help="1 = Not Useful, 5 = Very Useful")
    
with col3:
    instructor_quality = st.slider("Instructor Quality", 1, 5, 3, help="1 = Poor, 5 = Excellent")

# Comments
comments = st.text_area("Additional Comments", placeholder="Share your thoughts about this course...")

# Submit button
if st.button("Submit Review", type="primary", use_container_width=True):
    if course_code and course_name:
        st.success("✅ Review submitted successfully!")
        st.json({
            "course_code": course_code,
            "course_name": course_name,
            "subject_category": subject_category,
            "course_level": f"{course_number}s",
            "difficulty": difficulty,
            "usefulness": usefulness,
            "instructor_quality": instructor_quality,
            "comments": comments if comments else "No comments"
        })
    else:
        st.error("❌ Please fill in Course Code and Course Name")

st.divider()

# Display existing courses (placeholder)
st.subheader("Recent Reviews")
st.info("Reviews will appear here as they're submitted. This feature will be connected to a database soon.")
