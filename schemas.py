from marshmallow import Schema, fields

class CourseSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    description = fields.String()

course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)

class StudentSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    email = fields.String(required=True)
    
student_schema = StudentSchema()
students_schema = StudentSchema(many=True)