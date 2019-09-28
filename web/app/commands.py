import click
from flask.cli import with_appcontext

from app.database import seeder

@click.command('seed-db')
@with_appcontext
def seed_db_command():
  seeder.seed_db()