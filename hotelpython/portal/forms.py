from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class NewHotelForm(FlaskForm):
    """
    I want to make this better by sending the number of floors to
    the server and bounce the user across that many new forms to 
    give more control to the user when creating floors because
    it would not be so uniform in the real world. But first I want
    to make a generally functioning project before major upgrades
    """
    street = StringField("* Street", validators=[DataRequired()])
    city = StringField("* City", validators=[DataRequired()])
    state = StringField("* State", validators=[DataRequired()])
    zip = StringField("* Zip Code", validators=[DataRequired()])
    hotel = StringField("* Hotel Name", validators=[DataRequired()])
    floors = IntegerField("* Floors", validators=[DataRequired()])
    rpf = IntegerField("* Rooms Per Floor", validators=[DataRequired()])
    submit = SubmitField(label="Submit")


class NewRoleForm(FlaskForm):
    role = StringField("Role", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    submit = SubmitField(label="Submit")


class NewEmployeeForm(FlaskForm):
    """
    Also need other employee related forms:
    - UpdateInformation
    """
    f_name = StringField("First Name", validators=[DataRequired()])
    m_name = StringField("Middle Name", validators=[DataRequired()])
    l_name = StringField("Last Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    # role = select field for all roles
    phone = StringField("Phone Number", validators=[DataRequired()])
    street = StringField("Street", validators=[DataRequired()])
    city = StringField("City", validators=[DataRequired()])
    state = StringField("State", validators=[DataRequired()])
    zip = StringField("Zip Code", validators=[DataRequired()])
    submit = SubmitField(label="Submit")
    # hotel select field

class WeeklyScheduleForm(FlaskForm):
    pass


class PopulateHotelRooms(FlaskForm):
    pass