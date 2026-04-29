# CUNY Rate My Course

A Streamlit web application for CUNY students to rate and review courses based on difficulty, usefulness, and instructor quality. Supports all CUNY colleges including Lehman College, Hunter College, Queens College, Brooklyn College, City College, Baruch College, York College, and CUNY NYC College of Technology.

## Features

- **CUNY College Selection**: Choose from all CUNY colleges (Lehman, Hunter, Queens, Brooklyn, City, Baruch, York, NYC College of Technology, or Other)
- **Course Information**: Input course code and name
- **Professor Information**: Add professor name (optional) with link to Rate My Professor
- **Multi-Criteria Ratings**: Rate courses on:
  - Difficulty Level (1-5)
  - Usefulness (1-5)
  - Instructor Quality (1-5)
- **Comments Section**: Add detailed feedback about the course
- **Database Integration**: Reviews are persisted in SQLite database
- **Review Display**: View all submitted reviews with ratings, comments, and professor information
- **Search & Filter**: Easily find reviews by course or college

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
├── .streamlit/
│   └── config.toml        # Streamlit theme configuration (blue & white)
├── app.py                 # Main Streamlit application
├── database.py            # Database initialization and queries
├── create_logo.py         # Logo generation script
├── cuny_logo.png          # CUNY logo (auto-generated)
├── requirements.txt       # Python dependencies
├── reviews.db             # SQLite database (created automatically)
└── README.md             # This file
```

## Theme

The app features a professional blue and white color scheme:
- **Primary Color**: Bright Blue (#0066cc)
- **Background**: Clean White (#ffffff)
- **Secondary Background**: Light Blue (#e6f0ff)
- **Text Color**: Dark Gray (#1a1a1a)

## Future Enhancements

- [ ] Display aggregate ratings and statistics by course/college
- [ ] Advanced search and filter by course code or college
- [ ] User authentication and verified student reviews
- [ ] Review moderation system
- [ ] Course recommendations based on ratings
- [ ] Export reviews to CSV
- [ ] Integration with CUNY course catalog API
