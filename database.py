import sqlite3
import pandas as pd
from datetime import datetime
import os

DB_PATH = "reviews.db"

def init_db():
    """Initialize the database with reviews table."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            college TEXT NOT NULL,
            course_code TEXT NOT NULL,
            course_name TEXT NOT NULL,
            difficulty INTEGER NOT NULL,
            usefulness INTEGER NOT NULL,
            instructor_quality INTEGER NOT NULL,
            comments TEXT,
            submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

def add_review(college, course_code, course_name, difficulty, usefulness, instructor_quality, comments):
    """Add a new review to the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO reviews 
        (college, course_code, course_name, difficulty, usefulness, instructor_quality, comments)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (college, course_code, course_name, difficulty, usefulness, instructor_quality, comments))
    
    conn.commit()
    conn.close()

def get_all_reviews():
    """Get all reviews from the database."""
    conn = sqlite3.connect(DB_PATH)
    query = "SELECT * FROM reviews ORDER BY submitted_at DESC"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def get_course_reviews(course_code):
    """Get all reviews for a specific course."""
    conn = sqlite3.connect(DB_PATH)
    query = "SELECT * FROM reviews WHERE course_code = ? ORDER BY submitted_at DESC"
    df = pd.read_sql_query(query, conn, params=(course_code,))
    conn.close()
    return df

def get_college_reviews(college):
    """Get all reviews for a specific college."""
    conn = sqlite3.connect(DB_PATH)
    query = "SELECT * FROM reviews WHERE college = ? ORDER BY submitted_at DESC"
    df = pd.read_sql_query(query, conn, params=(college,))
    conn.close()
    return df

def get_course_stats(course_code):
    """Get average ratings for a specific course."""
    conn = sqlite3.connect(DB_PATH)
    query = '''
        SELECT 
            COUNT(*) as total_reviews,
            ROUND(AVG(difficulty), 2) as avg_difficulty,
            ROUND(AVG(usefulness), 2) as avg_usefulness,
            ROUND(AVG(instructor_quality), 2) as avg_instructor_quality
        FROM reviews 
        WHERE course_code = ?
    '''
    df = pd.read_sql_query(query, conn, params=(course_code,))
    conn.close()
    return df

def get_college_stats(college):
    """Get average ratings for a specific college."""
    conn = sqlite3.connect(DB_PATH)
    query = '''
        SELECT 
            COUNT(*) as total_reviews,
            ROUND(AVG(difficulty), 2) as avg_difficulty,
            ROUND(AVG(usefulness), 2) as avg_usefulness,
            ROUND(AVG(instructor_quality), 2) as avg_instructor_quality
        FROM reviews 
        WHERE college = ?
    '''
    df = pd.read_sql_query(query, conn, params=(college,))
    conn.close()
    return df

if __name__ == "__main__":
    init_db()
    print("Database initialized!")
