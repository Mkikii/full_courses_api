# Flask-RESTful Course Management API

A robust RESTful API built with Flask-RESTful for managing courses and students. This project demonstrates modern API development practices, clean architecture, and comprehensive CRUD operations.

## Features

- RESTful API Design following REST architectural principles
- Complete CRUD operations for courses and students
- Data validation using Marshmallow schemas
- Comprehensive error handling with meaningful responses
- SQLAlchemy ORM with SQLite database
- Clean, maintainable code architecture
- JSON-based communication
- Automatic timestamps for data tracking

## Quick Start

```bash
git clone https://github.com/Mkikii/full_courses_api.git
cd full_courses_api
pip install -r requirements.txt
python app.py
```

The API will be available at `http://127.0.0.1:5000`

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package installer

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Mkikii/full_courses_api.git
   cd full_courses_api
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

## API Endpoints

### Course Management

| Method | Endpoint | Description | Request Body |
|--------|----------|-------------|--------------|
| GET | `/api/courses` | Retrieve all courses | None |
| POST | `/api/courses` | Create new course | `{"name": "string", "description": "string"}` |
| GET | `/api/courses/{id}` | Retrieve specific course | None |
| PUT | `/api/courses/{id}` | Update existing course | `{"name": "string", "description": "string"}` |
| DELETE | `/api/courses/{id}` | Delete course | None |

### Student Management

| Method | Endpoint | Description | Request Body |
|--------|----------|-------------|--------------|
| GET | `/api/students` | Retrieve all students | None |
| POST | `/api/students` | Create new student | `{"name": "string", "email": "string"}` |
| GET | `/api/students/{id}` | Retrieve specific student | None |
| PUT | `/api/students/{id}` | Update existing student | `{"name": "string", "email": "string"}` |
| DELETE | `/api/students/{id}` | Delete student | None |

## Usage Examples

### Create a Course

```bash
curl -X POST http://127.0.0.1:5000/api/courses \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Introduction to Python",
    "description": "Learn Python programming fundamentals"
  }'
```

**Response:**
```json
{
    "success": true,
    "message": "Course created successfully!",
    "data": {
        "id": 1,
        "name": "Introduction to Python",
        "description": "Learn Python programming fundamentals",
        "created_at": "2025-09-18T08:46:00.123456",
        "updated_at": "2025-09-18T08:46:00.123456"
    }
}
```

### Retrieve All Courses

```bash
curl -X GET http://127.0.0.1:5000/api/courses
```

**Response:**
```json
{
    "success": true,
    "message": "Found 1 courses",
    "data": [
        {
            "id": 1,
            "name": "Introduction to Python",
            "description": "Learn Python programming fundamentals",
            "created_at": "2025-09-18T08:46:00.123456",
            "updated_at": "2025-09-18T08:46:00.123456"
        }
    ],
    "count": 1
}
```

### Create a Student

```bash
curl -X POST http://127.0.0.1:5000/api/students \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john.doe@example.com"
  }'
```

### Update a Course

```bash
curl -X PUT http://127.0.0.1:5000/api/courses/1 \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Advanced Python Programming",
    "description": "Advanced Python concepts and techniques"
  }'
```

## Project Structure

```
full_courses_api/
├── app.py                 # Application entry point and configuration
├── extensions.py          # Flask extensions initialization
├── models.py             # Database models
├── schemas.py            # Data validation schemas
├── resources.py          # API endpoint logic
├── requirements.txt      # Python dependencies
├── README.md            # Documentation
├── courses.db           # SQLite database (auto-generated)
└── .gitignore          # Git ignore rules
```

### File Descriptions

- **app.py**: Main application factory with configuration and startup logic
- **extensions.py**: Centralized Flask extensions initialization
- **models.py**: SQLAlchemy database models for Course and Student entities
- **schemas.py**: Marshmallow schemas for request/response validation
- **resources.py**: Flask-RESTful resource classes containing API business logic

## Configuration

### Default Settings

- Database: SQLite (`courses.db`)
- Port: 5000
- Debug Mode: Enabled (development)

### Environment Configuration

Modify configuration in `app.py`:

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///courses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
```

## Response Format

### Success Response

```json
{
    "success": true,
    "message": "Operation completed successfully",
    "data": {},
    "count": 1
}
```

### Error Response

```json
{
    "success": false,
    "error": "Error description",
    "details": {}
}
```

## HTTP Status Codes

- **200 OK**: Successful GET, PUT operations
- **201 Created**: Successful POST operations
- **400 Bad Request**: Invalid input data
- **404 Not Found**: Resource not found
- **500 Internal Server Error**: Server-side errors

## Testing

### Manual Testing with Postman

1. Set base URL to `http://127.0.0.1:5000`
2. Test endpoints in order:
   - Create Course (POST)
   - Get All Courses (GET)
   - Get Single Course (GET)
   - Update Course (PUT)
   - Delete Course (DELETE)

### Testing with curl

```bash
# Test API availability
curl http://127.0.0.1:5000/api/courses

# Create test data
curl -X POST http://127.0.0.1:5000/api/courses \
  -H "Content-Type: application/json" \
  -d '{"name": "Test Course", "description": "Testing purposes"}'
```

## Error Handling

The API implements comprehensive error handling:

- Input validation errors return detailed field-specific messages
- Database errors trigger automatic rollbacks
- Not found errors return appropriate 404 responses
- Server errors return 500 status with error descriptions

## Dependencies

### Core Dependencies

```
Flask==2.2.2
Flask-RESTful==0.3.10
Flask-SQLAlchemy==3.0.3
marshmallow==3.22.0
```

### Development Dependencies

```
Flask-Migrate==4.0.0
pytest==8.3.5
```

Complete dependency list available in `requirements.txt`.

## Development

### Adding New Endpoints

1. Define model in `models.py`
2. Create validation schema in `schemas.py`
3. Implement resource class in `resources.py`
4. Register endpoint in `app.py`

### Code Standards

- Follow PEP 8 style guidelines
- Include comprehensive error handling
- Use descriptive variable and function names
- Add docstrings for all classes and methods

## Deployment

### Development Server

```bash
python app.py
```

### Production Deployment

For production environments:

1. Use production WSGI server (Gunicorn)
2. Configure production database (PostgreSQL/MySQL)
3. Set environment variables for sensitive configuration
4. Implement proper logging
5. Use containerization (Docker)

Example production command:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/new-feature`)
3. Commit changes (`git commit -m 'Add new feature'`)
4. Push to branch (`git push origin feature/new-feature`)
5. Create Pull Request

## License

This project is licensed under the MIT License.

## Author

Developed by [Mkikii](https://github.com/Mkikii)

## Repository

[https://github.com/Mkikii/full_courses_api](https://github.com/Mkikii/full_courses_api)
