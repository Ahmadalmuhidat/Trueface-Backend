# TrueFace

TrueFace is an advanced attendance management software leveraging facial recognition technology to streamline the process of tracking attendance. This project is designed to offer a seamless and automated solution, utilizing real-time facial recognition to identify individuals and record attendance accurately.

## Features

- **Face Recognition:** Automated attendance recording using face recognition technology.
- **Real-Time Tracking:** Capture and process attendance in real-time.
- **FastAPI Integration:** API built with FastAPI to manage and interact with attendance data.
- **Docker Support:** Easy deployment using Docker with automated build and deployment to DockerHub.
- **Customizable Database Connection:** Easily configurable database connection for flexibility.

## Getting Started

### Prerequisites

- **Python 3.9+**: Make sure you have Python installed.
- **FastAPI**: The API is built using FastAPI, which needs to be installed.
- **Docker**: Required for containerization and deployment.
- **MySQL**: The system uses a MySQL database for storing attendance data.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/TrueFace.git
   cd TrueFace
   ```

2. Set up the environment:

    Install the required Python packages:
    
    ```bash
    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt
    ```

3. Navigate to config/DB/database.py and update the database connection details

4. Run the FastAPI server:

    ```bash
    uvicorn app.main:app --reload
    ```
    Access the API documentation at http://localhost:8000/docs.




### Docker Deployment

To deploy TrueFace using Docker:

1. Build and run the Docker container locally:

    ```bash
    docker build -t trueface .
    docker run -p 8000:8000 trueface
    ```

2. To automate the process of building and pushing the Docker image to DockerHub, use the updater.sh script. This script automates the following:

    - Builds the Docker image.
    - Tags it with the appropriate version.
    - Pushes the image to your DockerHub repository.

    ```bash
        ./updater.sh
    ```
    Make sure to modify the updater.sh file to include your DockerHub credentials and repository information.

