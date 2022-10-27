from model import db, User, Appointment

def create_user(user_name):
    user = User(user_name = user_name)
    return user

def get_user_by_user_name(user_name):
    return User.query.filter(User.user_name == user_name).first()

def get_user_by_id(user_id):
    return User.query.get(user_id)

def create_appointment(user, appointment_date):
    appointment = Appointment(
        user=user,
        appointment_date = appointment_date

    )

    return appointment

def get_appointment_by_user(user_id):
    return Appointment.query.filter(Appointment.user_id ==user_id)

def get_appointment_by_id(appointment_id):
    return Appointment.query.get(appointment_id)