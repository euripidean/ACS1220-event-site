"""Create database models to represent tables."""
from events_app import db
from sqlalchemy.orm import backref

class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(255))
    phone = db.Column(db.String(20))
    events_attending = db.relationship('Event', secondary='guest_event', back_populates='guests')

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    date_and_time = db.Column(db.DateTime)
    event_type = db.Column(db.Enum('Party','Music','Social Event','Film'))
    guests = db.relationship('Guest', secondary='guest_event', back_populates='events_attending')

guest_event_table = db.Table('guest_event',
    db.Column('event_id', db.Integer, db.ForeignKey('event.id')),
    db.Column('guest_id', db.Integer, db.ForeignKey('guest.id'))
)
