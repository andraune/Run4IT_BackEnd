import enum
from run4it.app.database import (
    Column, SurrogatePK, TimestampedModel, db, reference_col, relationship)


class Profile(SurrogatePK, TimestampedModel):
    __tablename__ = 'user_profiles'

    # id required for primary join
    id = Column(db.Integer, primary_key=True, index=True)
    weight = Column(db.Integer, nullable=True)
    height = Column(db.Integer, nullable=True)
    birth_date = Column(db.Date, nullable=True)
    gender_code = Column(db.SmallInteger, nullable=True)

    user_id = reference_col('users', unique=True, nullable=False, index=True)
    user = relationship('User', backref='profile', uselist=False)

    def __init__(self, user, **kwargs):
        db.Model.__init__(self, user=user, **kwargs)

    @property
    def username(self):
        return self.user.username

    def __repr__(self):
        return '<UserProfile({username!r})>'.format(username=self.username)