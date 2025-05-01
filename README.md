# TrueFace

TrueFace is an advanced attendance management software leveraging facial recognition technology to streamline the process of tracking attendance. This project is designed to offer a seamless and automated solution, utilizing real-time facial recognition to identify individuals and record attendance accurately.

## Features

- **Face Recognition:** Automated attendance recording using face recognition technology.
- **Real-Time Tracking:** Capture and process attendance in real-time.
- **Django Integration:** API built with Django to manage and interact with attendance data.
- **Docker Support:** Easy deployment using Docker with automated build and deployment to DockerHub.
- **Customizable Database Connection:** Easily configurable database connection for flexibility.

## Getting Started

### Prerequisites

- **Python 3.9+**: Make sure you have Python installed.
- **Docker**: Required for containerization and deployment.
- **MySQL**: The system uses a MySQL database for storing attendance data.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Trueface-Backend.git
   cd TrueFace
   ```

2. Set up the environment:

    Install the required Python packages:
    
    ```bash
    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt
    ```

3. Navigate to settings.py and update the database connection details

4. Run the server:

    ```bash
    python manage.py runserver
    ```
