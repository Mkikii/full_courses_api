from flask import Blueprint, request, jsonify
from extensions import db
from models import Course
from schemas import course_schema, courses_schema

courses_bp = Blueprint('courses', __name__)

@courses_bp.route('/courses', methods=['GET'])
def get_all_courses():
    all_courses = Course.query.all()
    result = courses_schema.dump(all_courses)
    return jsonify(result)

@courses_bp.route('/courses', methods=['POST'])
def create_course():
    data = request.get_json()
    new_course = Course(name=data['name'], description=data.get('description'))
    db.session.add(new_course)
    db.session.commit()
    return course_schema.jsonify(new_course), 201

@courses_bp.route('/courses/<int:id>', methods=['GET'])
def get_course(id):
    course = Course.query.get_or_404(id)
    return course_schema.jsonify(course)

@courses_bp.route('/courses/<int:id>', methods=['PUT'])
def update_course(id):
    course = Course.query.get_or_404(id)
    data = request.get_json()
    for key, value in data.items():
        setattr(course, key, value)
    db.session.commit()
    return course_schema.jsonify(course)

@courses_bp.route('/courses/<int:id>', methods=['DELETE'])
def delete_course(id):
    course = Course.query.get_or_404(id)
    db.session.delete(course)
    db.session.commit()
    return jsonify({"message": "Course deleted successfully."}), 200