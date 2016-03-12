from sqlalchemy import *
from migrate import *

meta = MetaData()

teams = Table(
    'teams', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('manager_id', Integer),
    Column('name', String(40)),
)

users = Table(
    'users', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(40)),
    Column('email', String(40)),
    Column('passwd', String(40)),
    Column('role', String(40)),
    Column('start_date', Date),
    Column('end_date', Date),
    Column('pto_hours', Integer),
    Column('per_year', Integer),
    Column('active', Boolean),
)

requests = Table(
    'requests', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('type', String(40)),
    Column('user_id', Integer),
    Column('start_date', Date),
    Column('end_date', Date),
    Column('hours', Integer),
    Column('status', Integer),
)

request_status = Table(
    'request_status', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('state', String(40)),
    Column('note', Text),
    Column('date', Date),
)

settings = Table(
    'settings', meta,
    Column('yearly_rollover', Boolean),
    Column('sick_is_pto', Boolean),
)


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    teams.create()
    users.create()
    requests.create()
    request_status.create()
    settings.create()


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    teams.drop()
    users.drop()
    requests.drop()
    request_status.drop()
    settings.drop()
