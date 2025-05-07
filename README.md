# Chenghao Wang (Caelan) - Portfolio Website

A personal portfolio website built with Streamlit to showcase my education, skills, projects, and experience.

## Features

- Clean, responsive UI design
- Multiple sections: Home, Projects, Resume, Contact
- Interactive elements and modern styling
- Professional presentation of educational background, skills, and work experience
- Project showcase with descriptions and images
- Contact form for potential employers or collaborators

## Prerequisites

- Python 3.7+
- pip (Python package installer)

## Installation

1. Clone this repository:

```bash
git clone https://github.com/your-username/portfolio-website.git
cd portfolio-website
```

2. Create a virtual environment (optional but recommended):

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

## Running the Application

To launch the portfolio website:

```bash
streamlit run app.py
```

The application will start and automatically open in your default web browser. If it doesn't open automatically, you can access it at [http://localhost:8501](http://localhost:8501).

## Customization

- To update personal information, edit the relevant sections in `app.py`
- To add new projects, modify the `projects_page()` function in `app.py`
- To change styling, modify the CSS in the `local_css()` function
- To add profile images or project images, place them in the `assets` directory and update the image paths in the code

## Deployment

This Streamlit app can be deployed on platforms like:

- [Streamlit Cloud](https://streamlit.io/cloud)
- [Heroku](https://heroku.com)
- [Render](https://render.com)

## License

MIT

## Author

Chenghao Wang (Caelan) 