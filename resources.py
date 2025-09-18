from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from extensions import db
from models import Course, Student
from schemas import course_schema, courses_schema, student_schema, students_schema

class CourseListResource(Resource):
    """Handle operations on the course collection"""
    
    def get(self):
        """GET /api/courses - Get all courses"""
        try:
            courses = Course.query.all()
            result = courses_schema.dump(courses)
            
            return {
                'success': True,
                'data': result,
                'count': len(result),
                'message': f'Retrieved {len(result)} courses'
            }, 200
            
        except Exception as e:
            return {
                'success': False,
                'error': f'Failed to retrieve courses: {str(e)}'
            }, 500
    
    def post(self):
        """POST /api/courses - Create a new course"""
        try:
            # Get and validate JSON data
            json_data = request.get_json()
            
            if not json_data:
                return {
                    'success': False,
                    'error': 'No JSON data provided'
                }, 400
            
            # Validate using schema
            validated_data = course_schema.load(json_data)
            
            # Create new course
            new_course = Course(
                name=validated_data['name'],
                description=validated_data.get('description', '')
            )
            
            # Save to database
            db.session.add(new_course)
            db.session.commit()
            
            # Return created course
            result = course_schema.dump(new_course)
            return {
                'success': True,
                'message': 'Course created successfully',
                'data': result
            }, 201
            
        except ValidationError as e:
            return {
                'success': False,
                'error': 'Validation failed',
                'details': e.messages
            }, 400
            
        except Exception as e:
            db.session.rollback()
            return {
                'success': False,
                'error': f'Failed to create course: {str(e)}'
            }, 500

class CourseResource(Resource):
    """Handle operations on individual courses"""
    
    def get(self, course_id):
        """GET /api/courses/<id> - Get a specific course"""
        try:
            course = Course.query.get_or_404(course_id)
            result = course_schema.dump(course)
            
            return {
                'success': True,
                'data': result
            }, 200
            
        except Exception as e:
            return {
                'success': False,
                'error': 'Course not found'
            }, 404
    
    def put(self, course_id):
        """PUT /api/courses/<id> - Update a specific course"""
        try:
            course = Course.query.get_or_404(course_id)
            json_data = request.get_json()
            
            if not json_data:
                return {
                    'success': False,
                    'error': 'No JSON data provided'
                }, 400
            
            # Validate data (partial=True allows updating only some fields)
            validated_data = course_schema.load(json_data, partial=True)
            
            # Update fields
            if 'name' in validated_data:
                course.name = validated_data['name']
            if 'description' in validated_data:
                course.description = validated_data['description']
            
            db.session.commit()
            
            result = course_schema.dump(course)
            return {
                'success': True,
                'message': 'Course updated successfully',
                'data': result
            }, 200
            
        except ValidationError as e:
            return {
                'success': False,
                'error': 'Validation failed',
                'details': e.messages
            }, 400
            
        except Exception as e:
            db.session.rollback()
            return {
                'success': False,
                'error': f'Failed to update course: {str(e)}'
            }, 500
    
    def delete(self, course_id):
        """DELETE /api/courses/<id> - Delete a specific course"""
        try:
            course = Course.query.get_or_404(course_id)
            course_name = course.name
            
            db.session.delete(course)
            db.session.commit()
            
            return {
                'success': True,
                'message': f'Course "{course_name}" deleted successfully'
            }, 200
            
        except Exception as e:
            db.session.rollback()
            return {
                'success': False,
                'error': f'Failed to delete course: {str(e)}'
            }, 500

class StudentListResource(Resource):
    """Handle operations on the student collection"""
    
    def get(self):
        """GET /api/students - Get all students"""
        try:
            students = Student.query.all()
            result = students_schema.dump(students)
            
            return {
                'success': True,
                'data': result,
                'count': len(result),
                'message': f'Retrieved {len(result)} students'
            }, 200
            
        except Exception as e:
            return {
                'success': False,
                'error': f'Failed to retrieve students: {str(e)}'
            }, 500
    
    def post(self):
        """POST /api/students - Create a new student"""
        try:
            json_data = request.get_json()
            
            if not json_data:
                return {
                    'success': False,
                    'error': 'No JSON data provided'
                }, 400
            
            validated_data = student_schema.load(json_data)
            
            new_student = Student(
                name=validated_data['name'],
                email=validated_data['email']
            )
            
            db.session.add(new_student)
            db.session.commit()
            
            result = student_schema.dump(new_student)
            return {
                'success': True,
                'message': 'Student created successfully',
                'data': result
            }, 201
            
        except ValidationError as e:
            return {
                'success': False,
                'error': 'Validation failed',
                'details': e.messages
            }, 400
            
        except Exception as e:
            db.session.rollback()
            return {
                'success': False,
                'error': f'Failed to create student: {str(e)}'
            }, 500

class StudentResource(Resource):
    """Handle operations on individual students"""
    
    def get(self, student_id):
        """GET /api/students/<id> - Get a specific student"""
        try:
            student = Student.query.get_or_404(student_id)
            result = student_schema.dump(student)
            
            return {
                'success': True,
                'data': result
            }, 200
            
        except Exception as e:
            return {
                'success': False,
                'error': 'Student not found'
            }, 404
    
    def put(self, student_id):
        """PUT /api/students/<id> - Update a specific student"""
        try:
            student = Student.query.get_or_404(student_id)
            json_data = request.get_json()
            
            if not json_data:
                return {
                    'success': False,
                    'error': 'No JSON data provided'
                }, 400
            
            validated_data = student_schema.load(json_data, partial=True)
            
            if 'name' in validated_data:
                student.name = validated_data['name']
            if 'email' in validated_data:
                student.email = validated_data['email']
            
            db.session.commit()
            
            result = student_schema.dump(student)
            return {
                'success': True,
                'message': 'Student updated successfully',
                'data': result
            }, 200
            
        except ValidationError as e:
            return {
                'success': False,
                'error': 'Validation failed',
                'details': e.messages
            }, 400
            
        except Exception as e:
            db.session.rollback()
            return {
                'success': False,
                'error': f'Failed to update student: {str(e)}'
            }, 500
    
    def delete(self, student_id):
        """DELETE /api/students/<id> - Delete a specific student"""
        try:
            student = Student.query.get_or_404(student_id)
            student_name = student.name
            
            db.session.delete(student)
            db.session.commit()
            
            return {
                'success': True,
                'message': f'Student "{student_name}" deleted successfully'
            }, 200
            
        except Exception as e:
            db.session.rollback()
            return {
                'success': False,
                'error': f'Failed to delete student: {str(e)}'
            }, 500