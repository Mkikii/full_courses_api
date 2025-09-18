from marshmallow import Schema, fields, ValidationError, validates_schema

class CourseSchema(Schema):
    """Schema for validating and serializing Course data"""
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=fields.Length(min=1, max=100))
    description = fields.String(validate=fields.Length(max=500))
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class StudentSchema(Schema):
    """Schema for validating and serializing Student data"""
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=fields.Length(min=1, max=100))
    email = fields.Email(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

# Create schema instances
course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)
student_schema = StudentSchema()
students_schema = StudentSchema(many=True)
