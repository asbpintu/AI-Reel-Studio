"""Create script, scene, video, and reel tables

Revision ID: d0f9a8b7c6e5
Revises: 2f995b6e6796
Create Date: 2026-07-12 00:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd0f9a8b7c6e5'
down_revision: Union[str, Sequence[str], None] = '2f995b6e6796'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'Scripts',
        sa.Column('ScriptId', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('PublicId', sa.String(length=36), nullable=False),
        sa.Column('ProjectId', sa.Integer(), nullable=False),
        sa.Column('Prompt', sa.Text(), nullable=False),
        sa.Column('Keywords', sa.String(length=500), nullable=True),
        sa.Column('DurationSeconds', sa.Integer(), nullable=True),
        sa.Column('Language', sa.String(length=100), nullable=True),
        sa.Column('ReelType', sa.String(length=100), nullable=True),
        sa.Column('VoiceType', sa.String(length=100), nullable=True),
        sa.Column('Style', sa.String(length=100), nullable=True),
        sa.Column('GeneratedScript', sa.Text(), nullable=True),
        sa.Column('Status', sa.String(length=50), nullable=False),
        sa.Column('CreatedAt', sa.DateTime(), nullable=False),
        sa.Column('UpdatedAt', sa.DateTime(), nullable=False),
        sa.Column('CreatedBy', sa.Integer(), nullable=True),
        sa.Column('UpdatedBy', sa.Integer(), nullable=True),
        sa.Column('IsDeleted', sa.Boolean(), nullable=False),
        sa.ForeignKeyConstraint(['ProjectId'], ['Projects.ProjectId'], ),
        sa.PrimaryKeyConstraint('ScriptId'),
        sa.UniqueConstraint('PublicId')
    )
    op.create_table(
        'Scenes',
        sa.Column('SceneId', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('PublicId', sa.String(length=36), nullable=False),
        sa.Column('ScriptId', sa.Integer(), nullable=False),
        sa.Column('SceneNumber', sa.Integer(), nullable=False),
        sa.Column('Narration', sa.Text(), nullable=False),
        sa.Column('ImagePrompt', sa.Text(), nullable=False),
        sa.Column('DurationSeconds', sa.Integer(), nullable=False),
        sa.Column('ImageUrl', sa.String(length=500), nullable=True),
        sa.Column('ImageStatus', sa.String(length=50), nullable=False),
        sa.Column('AudioUrl', sa.String(length=500), nullable=True),
        sa.Column('AudioStatus', sa.String(length=50), nullable=True),
        sa.Column('CreatedAt', sa.DateTime(), nullable=False),
        sa.Column('UpdatedAt', sa.DateTime(), nullable=False),
        sa.Column('CreatedBy', sa.Integer(), nullable=True),
        sa.Column('UpdatedBy', sa.Integer(), nullable=True),
        sa.Column('IsDeleted', sa.Boolean(), nullable=False),
        sa.ForeignKeyConstraint(['ScriptId'], ['Scripts.ScriptId'], ),
        sa.PrimaryKeyConstraint('SceneId'),
        sa.UniqueConstraint('PublicId')
    )
    op.create_table(
        'Videos',
        sa.Column('VideoId', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('ScriptId', sa.Integer(), nullable=False),
        sa.Column('VideoUrl', sa.String(length=500), nullable=True),
        sa.Column('Status', sa.String(length=50), nullable=False),
        sa.Column('DurationSeconds', sa.Integer(), nullable=True),
        sa.Column('CreatedAt', sa.DateTime(), nullable=False),
        sa.Column('UpdatedAt', sa.DateTime(), nullable=False),
        sa.Column('CreatedBy', sa.Integer(), nullable=True),
        sa.Column('UpdatedBy', sa.Integer(), nullable=True),
        sa.Column('IsDeleted', sa.Boolean(), nullable=False),
        sa.ForeignKeyConstraint(['ScriptId'], ['Scripts.ScriptId'], ),
        sa.PrimaryKeyConstraint('VideoId'),
        sa.UniqueConstraint('ScriptId')
    )
    op.create_table(
        'Reels',
        sa.Column('ReelId', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('ProjectId', sa.Integer(), nullable=False),
        sa.Column('Title', sa.String(length=200), nullable=False),
        sa.Column('Prompt', sa.String(length=3000), nullable=False),
        sa.Column('Status', sa.String(length=50), nullable=False),
        sa.Column('CreatedAt', sa.DateTime(), nullable=False),
        sa.Column('UpdatedAt', sa.DateTime(), nullable=False),
        sa.Column('CreatedBy', sa.Integer(), nullable=True),
        sa.Column('UpdatedBy', sa.Integer(), nullable=True),
        sa.Column('IsDeleted', sa.Boolean(), nullable=False),
        sa.ForeignKeyConstraint(['ProjectId'], ['Projects.ProjectId'], ),
        sa.PrimaryKeyConstraint('ReelId')
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('Reels')
    op.drop_table('Videos')
    op.drop_table('Scenes')
    op.drop_table('Scripts')
