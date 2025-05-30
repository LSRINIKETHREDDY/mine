# EduHub Flask Platform

EduHub is a real-time, student-first educational platform where learners can freely access high-quality notes, PDFs, projects, and materials for both semester and competitive exams. Students can submit their content for review, and the best resources are published on the website. Notifications and news are summarized for easy access, and a contact form allows users to reach out directly.

## Project Structure

```
project
├── app.py                   # Main Flask application
├── templates
│   ├── mainpage.html        # Home page with notifications/news
│   ├── contact.html         # Contact form
│   ├── aboutme.html         # About page
│   └── thanks.html          # Submission feedback page
├── static
│   ├── style.css            # CSS styles for the platform
│   └── notifications
│       ├── notification1.pdf  # Example notification PDF
│       └── notification2.pdf  # Example notification PDF
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd project
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python app.py
   ```

2. Open your web browser and go to `http://127.0.0.1:5000/` to access EduHub.

3. Browse notifications/news, download PDFs, or use the contact form to reach out.

## Features

- Home page with summarized notifications and news (PDFs and text).
- Contact form that sends messages to the admin's email.
- About page describing EduHub's mission.
- Responsive, modern design with a bluish-purple theme.

## Requirements

The main dependencies are listed in `requirements.txt`:

- Flask: A lightweight WSGI web application framework.
- Flask-Mail: An extension to Flask that provides simple mail sending capabilities.
- Flask-WTF: An extension that integrates WTForms with Flask.
- PyPDF2: A library to read PDF files.
- python-dotenv: A library to manage environment variables.

## Notes

- Place your notification PDFs in `static/notifications/`.
- Configure your email settings in `app.py` for the contact form to work.
- For AI/chatbot integration or advanced features, see project issues or contact the maintainer.