"""add packages and orders

Revision ID: 0002_packages_orders
Revises: 0001_initial_users_businesses
Create Date: 2026-05-29 00:05:00.000000
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '0002_packages_orders'
down_revision = '0001_initial_users_businesses'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'surprise_packages',
        sa.Column('id', sa.dialects.postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text('gen_random_uuid()')),
        sa.Column('business_id', sa.dialects.postgresql.UUID(as_uuid=True), sa.ForeignKey('businesses.id', ondelete='CASCADE'), nullable=False),
        sa.Column('titulo', sa.String(length=255), nullable=False),
        sa.Column('descripcion', sa.Text()),
        sa.Column('valor_original', sa.Numeric(12,2)),
        sa.Column('precio_salvio', sa.Numeric(12,2), nullable=False),
        sa.Column('cantidad_disponible', sa.Integer(), server_default='1'),
        sa.Column('hora_inicio', sa.DateTime(timezone=True)),
        sa.Column('hora_fin', sa.DateTime(timezone=True)),
        sa.Column('estado', sa.String(length=50), server_default=sa.text("'Disponible'")),
    )

    op.create_table(
        'orders',
        sa.Column('id', sa.dialects.postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text('gen_random_uuid()')),
        sa.Column('user_id', sa.dialects.postgresql.UUID(as_uuid=True), sa.ForeignKey('users.id', ondelete='SET NULL')),
        sa.Column('package_id', sa.dialects.postgresql.UUID(as_uuid=True), sa.ForeignKey('surprise_packages.id', ondelete='RESTRICT'), nullable=False),
        sa.Column('monto', sa.Numeric(12,2), nullable=False),
        sa.Column('status', sa.String(length=50), server_default=sa.text("'Pendiente'")),
        sa.Column('fecha_compra', sa.DateTime(timezone=True), server_default=sa.text('now()')),
        sa.Column('codigo_retiro', sa.String(length=64)),
    )


def downgrade():
    op.drop_table('orders')
    op.drop_table('surprise_packages')
