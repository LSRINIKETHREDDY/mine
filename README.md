# EduHub Flask Platform

EduHub is a real-time, student-first educational platform where learners can freely access high-quality notes, PDFs, projects, and materials for both semester and competitive exams. Students can submit their content for review, and the best resources are published on the website. Notifications and news are summarized for easy access, and a contact form allows users to reach out directly.

## Project Structure

```
mine/
├── app.py                  # Main Flask application
├── templates/              # HTML templates for all pages
│   ├── mainpage.html
│   ├── contact.html
│   ├── aboutme.html
│   ├── thanks.html
│   ├── syllabus.html
│   ├── cse.html
│   ├── ece.html
│   ├── eee.html
│   └── mech.html
├── static/
│   └── style.css           # CSS styles for the platform
├── pyproject.toml          # Poetry dependency file
├── poetry.lock             # Poetry lock file
├── requirements.txt        # pip requirements (for local dev)
├── render.yaml             # Render.com deployment config
└── README.md               # Project documentation
```

## Installation (Local)

1. Clone the repository:
   ```sh
   git clone https://github.com/LSRINIKETHREDDY/mine.git
   cd mine
   ```

2. Install dependencies using Poetry:
   ```sh
   poetry install
   ```

3. Run the application locally:
   ```sh
   poetry run python app.py
   ```

4. Open your web browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to access EduHub.

## Deployment (Render.com)

1. Ensure `render.yaml`, `pyproject.toml`, and `poetry.lock` are at the repo root.
2. Render will use the following start command:
   ```
   poetry run gunicorn app:app
   ```
3. On successful deploy, your app will be available at your Render.com service URL.

## Features

- Home page with summarized notifications and news.
- Contact form that sends messages to the admin's email.
- About page describing EduHub's mission.
- Responsive, modern design with a bluish-purple theme.

## Requirements

Main dependencies (managed by Poetry):

- Flask: A lightweight WSGI web application framework.
- Gunicorn: Production WSGI server for deployment.
- fpdf: PDF generation library.

## Notes

- Place any static files (like images or PDFs) in the `static/` folder.
- Configure your email settings in `app.py` for the contact form to work.
- For AI/chatbot integration or advanced features, see project issues or contact the maintainer.