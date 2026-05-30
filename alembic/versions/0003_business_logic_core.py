"""business logic core

Revision ID: 0003_business_logic_core
Revises: 0002_packages_orders
Create Date: 2026-05-29 00:10:00.000000
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '0003_business_logic_core'
down_revision = '0002_packages_orders'
branch_labels = None
depends_on = None


def upgrade():
    # categories
    op.create_table(
        'categories',
        sa.Column('id', sa.dialects.postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text('gen_random_uuid()')),
        sa.Column('nombre', sa.String(length=100), nullable=False, unique=True),
    )

    # package_statuses
    op.create_table(
        'package_statuses',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('nombre', sa.String(length=50), nullable=False, unique=True),
    )

    # commissions
    op.create_table(
        'commissions',
        sa.Column('id', sa.dialects.postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text('gen_random_uuid()')),
        sa.Column('order_id', sa.dialects.postgresql.UUID(as_uuid=True), sa.ForeignKey('orders.id', ondelete='CASCADE'), nullable=False),
        sa.Column('porcentaje', sa.Numeric(5,2), nullable=False),
        sa.Column('monto_comision', sa.Numeric(12,2), nullable=False),
        sa.Column('fecha', sa.DateTime(timezone=True), server_default=sa.text('now()')),
    )

    # pickup_codes
    op.create_table(
        'pickup_codes',
        sa.Column('id', sa.dialects.postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text('gen_random_uuid()')),
        sa.Column('order_id', sa.dialects.postgresql.UUID(as_uuid=True), sa.ForeignKey('orders.id', ondelete='CASCADE'), nullable=False),
        sa.Column('qr_code', sa.Text()),
        sa.Column('usado', sa.Boolean(), server_default=sa.text('false')),
        sa.Column('fecha_uso', sa.DateTime(timezone=True)),
    )

    # metrics_daily
    op.create_table(
        'metrics_daily',
        sa.Column('fecha', sa.Date(), primary_key=True),
        sa.Column('ventas_totales', sa.Numeric(14,2), server_default='0'),
        sa.Column('paquetes_rescatados', sa.Integer(), server_default='0'),
        sa.Column('usuarios_activos', sa.Integer(), server_default='0'),
        sa.Column('negocios_activos', sa.Integer(), server_default='0'),
        sa.Column('comisiones', sa.Numeric(14,2), server_default='0'),
    )


def downgrade():
    op.drop_table('metrics_daily')
    op.drop_table('pickup_codes')
    op.drop_table('commissions')
    op.drop_table('package_statuses')
    op.drop_table('categories')
