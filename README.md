# Student Management System (SMS) - Backend

A Django-based backend for a Student Management System that handles academic operations including department management, lecture scheduling, and class offerings.

## Features

- **Department Management**: Create and manage academic departments with department heads
- **Lecture Management**: Define and organize lectures within departments
- **Semester System**: Manage academic semesters with start and end dates
- **Class Scheduling**: Schedule lectures with specific days and times
- **Professor Assignments**: Assign professors to lecture offerings

## Tech Stack

- **Backend Framework**: Django 4.2+
- **Database**: PostgreSQL (configurable)
- **Containerization**: Docker
- **Package Management**: pip

## Prerequisites

- Python 3.12+
- Docker (for containerized deployment)
- pip (Python package manager)

## Project Structure

```
sms-backend/
├── src/
│   ├── academics/                  # Academic management app
│   │   ├── models/                 # Data models
│   │   │   ├── department.py       # Department model
│   │   │   ├── lectures.py         # Lecture model
│   │   │   ├── smester.py          # Semester model
│   │   │   ├── lectures_offering.py # Lecture offerings model
│   │   │   └── class_schedule.py   # Class scheduling model
│   │   ├── serializers/            # API serializers
│   │   └── ...
│   ├── users/                      # User management app
│   └── manage.py                   # Django management script
├── Dockerfile                      # Docker configuration
└── requirements.txt                # Python dependencies
```

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd sms-backend
   ```

2. **Set up a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root with the following variables:
   ```
   SECRET_KEY=your-secret-key
   DEBUG=True
   DATABASE_URL=postgres://user:password@localhost:5432/sms_db
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

## Running with Docker

1. **Build the Docker image**
   ```bash
   docker build -t sms-backend .
   ```

2. **Run the container**
   ```bash
   docker run -p 8000:8000 sms-backend
   ```

   The application will be available at `http://localhost:8000`

## API Endpoints

### Departments
- `GET /api/departments/` - List all departments
- `POST /api/departments/` - Create a new department
- `GET /api/departments/{id}/` - Get department details

### Lectures
- `GET /api/lectures/` - List all lectures
- `POST /api/lectures/` - Create a new lecture
- `GET /api/lectures/{id}/` - Get lecture details

### Semesters
- `GET /api/semesters/` - List all semesters
- `POST /api/semesters/` - Create a new semester

### Lecture Offerings
- `GET /api/offerings/` - List all lecture offerings
- `POST /api/offerings/` - Create a new lecture offering

### Class Schedules
- `GET /api/schedules/` - List all class schedules
- `POST /api/schedules/` - Create a new class schedule


