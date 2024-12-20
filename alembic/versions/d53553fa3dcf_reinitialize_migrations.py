"""Reinitialize migrations

Revision ID: d53553fa3dcf
Revises: 
Create Date: 2024-12-20 11:22:59.138898
"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'd53553fa3dcf'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    # Creating 'instructors' table
    op.create_table('instructors',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('specialization', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_instructors_id'), 'instructors', ['id'], unique=False)
    
    # Creating 'courses' table with foreign key to 'instructors'
    op.create_table('courses',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('instructor_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['instructor_id'], ['instructors.id']),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_courses_id'), 'courses', ['id'], unique=False)

    # Creating 'assessments' table with foreign key to 'courses'
    op.create_table('assessments',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('course_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['course_id'], ['courses.id']),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_assessments_id'), 'assessments', ['id'], unique=False)

    # Creating 'students' table with optional foreign key to 'courses'
    op.create_table('students',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('course_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['course_id'], ['courses.id']),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_students_id'), 'students', ['id'], unique=False)

    # Creating 'enrollments' table with foreign keys to 'students' and 'courses'
    op.create_table('enrollments',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('student_id', sa.Integer(), nullable=False),
        sa.Column('course_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['course_id'], ['courses.id']),
        sa.ForeignKeyConstraint(['student_id'], ['students.id']),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_enrollments_id'), 'enrollments', ['id'], unique=False)

    # Creating 'performance' table with foreign keys to 'students' and 'assessments'
    op.create_table('performance',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('student_id', sa.Integer(), nullable=False),
        sa.Column('assessment_id', sa.Integer(), nullable=False),
        sa.Column('score', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['assessment_id'], ['assessments.id']),
        sa.ForeignKeyConstraint(['student_id'], ['students.id']),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_performance_id'), 'performance', ['id'], unique=False)
    
    # Drop the old tables if they exist
    op.drop_table('students')
    op.drop_table('instructors')
    op.drop_table('courses')
    op.drop_table('performance')
    op.drop_table('enrollments')
    op.drop_table('assessments')

def downgrade() -> None:
    # Recreate the old tables in the previous schema
    
    # Recreating 'assessments' table
    op.create_table('assessments',
        sa.Column('id', sa.INTEGER(), nullable=True),
        sa.Column('name', sa.TEXT(), nullable=False),
        sa.Column('course_id', sa.INTEGER(), nullable=False),
        sa.ForeignKeyConstraint(['course_id'], ['courses.id']),
        sa.PrimaryKeyConstraint('id')
    )

    # Recreating 'enrollments' table
    op.create_table('enrollments',
        sa.Column('id', sa.INTEGER(), nullable=True),
        sa.Column('student_id', sa.INTEGER(), nullable=False),
        sa.Column('course_id', sa.INTEGER(), nullable=False),
        sa.ForeignKeyConstraint(['course_id'], ['courses.id']),
        sa.ForeignKeyConstraint(['student_id'], ['students.id']),
        sa.PrimaryKeyConstraint('id')
    )

    # Recreating 'performance' table
    op.create_table('performance',
        sa.Column('id', sa.INTEGER(), nullable=True),
        sa.Column('student_id', sa.INTEGER(), nullable=False),
        sa.Column('assessment_id', sa.INTEGER(), nullable=False),
        sa.Column('score', sa.INTEGER(), nullable=False),
        sa.ForeignKeyConstraint(['assessment_id'], ['assessments.id']),
        sa.ForeignKeyConstraint(['student_id'], ['students.id']),
        sa.PrimaryKeyConstraint('id')
    )

    # Recreating 'courses' table
    op.create_table('courses',
        sa.Column('id', sa.INTEGER(), nullable=True),
        sa.Column('name', sa.TEXT(), nullable=False),
        sa.Column('description', sa.TEXT(), nullable=True),
        sa.Column('instructor_id', sa.INTEGER(), nullable=False),
        sa.ForeignKeyConstraint(['instructor_id'], ['instructors.id']),
        sa.PrimaryKeyConstraint('id')
    )

    # Recreating 'instructors' table
    op.create_table('instructors',
        sa.Column('id', sa.INTEGER(), nullable=True),
        sa.Column('name', sa.TEXT(), nullable=False),
        sa.Column('email', sa.TEXT(), nullable=False),
        sa.Column('specialization', sa.TEXT(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )

    # Recreating 'students' table with optional foreign key to 'courses'
    op.create_table('students',
        sa.Column('id', sa.INTEGER(), nullable=True),
        sa.Column('name', sa.TEXT(), nullable=False),
        sa.Column('email', sa.TEXT(), nullable=False),
        sa.Column('course_id', sa.INTEGER(), nullable=True),
        sa.ForeignKeyConstraint(['course_id'], ['courses.id']),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )

    # Drop the new tables created in the upgrade function
    op.drop_index(op.f('ix_performance_id'), table_name='performance')
    op.drop_table('performance')
    op.drop_index(op.f('ix_enrollments_id'), table_name='enrollments')
    op.drop_table('enrollments')
    op.drop_index(op.f('ix_students_id'), table_name='students')
    op.drop_table('students')
    op.drop_index(op.f('ix_assessments_id'), table_name='assessments')
    op.drop_table('assessments')
    op.drop_index(op.f('ix_courses_id'), table_name='courses')
    op.drop_table('courses')
    op.drop_index(op.f('ix_instructors_id'), table_name='instructors')
    op.drop_table('instructors')