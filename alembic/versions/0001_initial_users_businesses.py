"""initial users and businesses

Revision ID: 0001_initial_users_businesses
Revises: 
Create Date: 2026-05-29 00:00:00.000000
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '0001_initial_users_businesses'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.dialects.postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text('gen_random_uuid()')),
        sa.Column('nombre', sa.String(length=150), nullable=False),
        sa.Column('apellido', sa.String(length=150)),
        sa.Column('email', sa.String(length=320), nullable=False, unique=True),
        sa.Column('telefono', sa.String(length=30)),
        sa.Column('password_hash', sa.Text(), nullable=False),
        sa.Column('fecha_registro', sa.DateTime(timezone=True), server_default=sa.text('now()')),
        sa.Column('activo', sa.Boolean(), server_default=sa.text('true')),
    )

    op.create_table(
        'businesses',
        sa.Column('id', sa.dialects.postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text('gen_random_uuid()')),
        sa.Column('nombre_negocio', sa.String(length=255), nullable=False),
        sa.Column('categoria', sa.String(length=100)),
        sa.Column('email', sa.String(length=320)),
        sa.Column('telefono', sa.String(length=30)),
        sa.Column('direccion', sa.Text()),
        sa.Column('ciudad', sa.String(length=100)),
        sa.Column('latitud', sa.Numeric(9,6)),
        sa.Column('longitud', sa.Numeric(9,6)),
        sa.Column('logo_url', sa.Text()),
        sa.Column('activo', sa.Boolean(), server_default=sa.text('true')),
        sa.Column('fecha_registro', sa.DateTime(timezone=True), server_default=sa.text('now()')),
    )


def downgrade():
    op.drop_table('businesses')
    op.drop_table('users')
