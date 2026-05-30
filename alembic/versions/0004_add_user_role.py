"""add user role column

Revision ID: 0004_add_user_role
Revises: 0003_business_logic_core
Create Date: 2026-05-29 00:30:00.000000
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '0004_add_user_role'
down_revision = '0003_business_logic_core'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('role', sa.String(length=20), server_default=sa.text("'USER'"), nullable=False))


def downgrade():
    op.drop_column('users', 'role')
