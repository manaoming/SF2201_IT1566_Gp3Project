from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators, meta
from wtforms.fields import EmailField, DateField, HiddenField, IntegerField
import shelve, datetime, time


class DateAlreadyPast:
    def __init__(self, difference=1, message=None):
        self.difference = difference
        if message:
            self.message = message
        else:
            self.message = f"Please choose a date at least {difference} days after today"

    def __call__(self, form, field):
        if (field.data-datetime.date.today()).days < self.difference:
            raise validators.ValidationError(self.message)


class CreateUserForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    gender = SelectField('Gender', [validators.DataRequired()], choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
    membership = RadioField('Membership', choices=[('F', 'Fellow'), ('S', 'Senior'), ('P', 'Professional')], default='F')
    remarks = TextAreaField('Remarks', [validators.Optional()])


class DestinationForm(Form):
    destination = HiddenField("Destination", [validators.DataRequired()])


class ItineraryForm(Form):
    people = IntegerField("People", [validators.NumberRange(min=1, message="Must specify at least 1 person")])
    start_date = DateField('Date Joined', [validators.InputRequired(), DateAlreadyPast()], )

    duration = IntegerField("Duration in days", [validators.NumberRange(min=1, message="Must specify at least 1 person")])
    accommodation = SelectField("Accommodation", [validators.DataRequired()], choices=[('', 'Select'),
                ('1_1', 'Accommodation 1 for Destination 1'),
                ('1_2', 'Accommodation 2 for Destination 1'),
                ('3_1', 'Accommodation 1 for Destination 3'),
                ('3_2', 'Accommodation 2 for Destination 3')])


class CreateCustomerForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    gender = SelectField('Gender', [validators.DataRequired()], choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
    date_joined = DateField('Date Joined', format='%Y-%m-%d')
    address = TextAreaField('Mailing Address', [validators.length(max=200), validators.DataRequired()])
    membership = RadioField('Membership', choices=[('F', 'Fellow'), ('S', 'Senior'), ('P', 'Professional')], default='F')
    remarks = TextAreaField('Remarks', [validators.Optional()])
