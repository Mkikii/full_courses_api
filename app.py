from flask import Flask
from flask_restful import Api
from extensions import db
from resources import CourseListResource, CourseResource, StudentListResource, StudentResource

def create_app():
    """Create and configure the Flask application"""
    app = Flask(__name__)
    
    # Database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///courses.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize extensions
    db.init_app(app)
    api = Api(app)  # Initialize Flask-RESTful
    
    # Register API resources (these replace routes)
    # Course endpoints
    api.add_resource(CourseListResource, '/api/courses')           # GET, POST /api/courses
    api.add_resource(CourseResource, '/api/courses/<int:course_id>')  # GET, PUT, DELETE /api/courses/1
    
    # Student endpoints  
    api.add_resource(StudentListResource, '/api/students')         # GET, POST /api/students
    api.add_resource(StudentResource, '/api/students/<int:student_id>')  # GET, PUT, DELETE /api/students/1
    
    return app

if __name__ == '__main__':
    app = create_app()
    
    # Create database tables
    with app.app_context():
        db.create_all()
        print("✅ Database tables created successfully!")
    
    print("🚀 Starting Flask-RESTful server...")
    app.run(port=5000, debug=True)