from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """A user"""
    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_name = db.Column(db.String, unique = True)
    appointments = db.relationship("Appointment", back_populates="user" )

    def __repr__(self):
        return f"<User user_id={self.user_id} user_name={self.user_name}>"

class Appointment(db.Model):
    """An Appointment"""

    __tablename__= "appointments"

    appointment_id = db.Column(db.Integer, autoincrement =True, primary_key= True)
    appointment_date= db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    user = db.relationship("User", back_populates="appointments" )


    def __repr__(self):
        return f"<Appointment appointment_id={self.appointment_id} appointment_data={self.appointment_date}>"



def connect_to_db(flask_app, db_uri="postgresql:///appointments", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")

if __name__ == '__main__':
    print("create all")
    from server import app
    connect_to_db(app)
    db.create_all()