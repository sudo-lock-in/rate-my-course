import streamlit as st
import pandas as pd
from PIL import Image
from database import init_db, add_review, get_all_reviews, get_course_stats, get_college_stats, get_college_reviews

# Initialize database
init_db()

st.set_page_config(page_title="CUNY Rate My Course", layout="wide")

# Header with logo
col1, col2, col3 = st.columns([1, 4, 1])

with col1:
    try:
        logo = Image.open("cunylogo.jpg")
        st.image(logo, width=400)
    except:
        st.write("📚")

with col2:
    st.title("CUNY Rate My Course")
    st.write("Help your fellow CUNY students choose the best courses!")
st.divider()

# Course Information Section
st.subheader("📋 Course Information")
col1, col2, col3 = st.columns(3)

with col1:
    college = st.selectbox(
        "CUNY College",
        options=["Lehman College", "CUNY NYC College of Technology", "Hunter College", "Queens College", "Brooklyn College", "City College", "Baruch College", "York College", "Other"],
        help="Select your CUNY college"
    )

with col2:
    course_code = st.text_input("Course Code", placeholder="e.g., CS101")

with col3:
    course_name = st.text_input("Course Name", placeholder="e.g., Intro to Python")

st.divider()

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
comments = st.text_area("Additional Comments", placeholder="Share your thoughts about this course...", height=120)

st.divider()

# Submit button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Submit Review", type="primary", use_container_width=True):
        if course_code and course_name:
            # Add review to database
            add_review(
                college=college,
                course_code=course_code,
                course_name=course_name,
                difficulty=difficulty,
                usefulness=usefulness,
                instructor_quality=instructor_quality,
                comments=comments if comments else "No comments"
            )
            st.success("✅ Review submitted successfully!")
        else:
            st.error("❌ Please fill in Course Code and Course Name")

st.divider()

# Display recent reviews from database
st.subheader("📖 Recent Reviews from CUNY Students")

# Get all reviews
all_reviews = get_all_reviews()

if not all_reviews.empty:
    # Display stats
    st.write(f"**Total Reviews: {len(all_reviews)}**")
    
    # Show reviews in a nice format
    for idx, review in all_reviews.head(10).iterrows():
        with st.container():
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(f"**{review['course_code']} - {review['course_name']}**")
                st.write(f"*{review['college']}*")
                st.write(f"📝 {review['comments']}")
            with col2:
                st.metric("Difficulty", review['difficulty'], delta=None)
                st.metric("Usefulness", review['usefulness'], delta=None)
                st.metric("Instructor", review['instructor_quality'], delta=None)
            st.divider()
else:
    st.info("No reviews yet. Be the first to submit a review!")
