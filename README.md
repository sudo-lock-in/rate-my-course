# Rate My Course

A Streamlit web application that helps students rate and review courses based on difficulty, usefulness, and instructor quality.

## Features

- **Subject Category Selection**: Choose between STEM (harder) or Liberal Arts (easier) courses
- **Course Level Selection**: Select course difficulty levels (100s through 400s)
- **Course Information**: Input course code and name
- **Multi-Criteria Ratings**: Rate courses on:
  - Difficulty Level (1-5)
  - Usefulness (1-5)
  - Instructor Quality (1-5)
- **Comments Section**: Add detailed feedback about the course

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd rate-my-course
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Project Structure

```
rate-my-course/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Future Enhancements

- [ ] Connect to a database to persist reviews
- [ ] Display aggregate ratings and statistics
- [ ] Search and filter courses
- [ ] User authentication
- [ ] Review moderation system
- [ ] Course recommendations based on ratings
