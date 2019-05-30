from wtforms import Form, StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired
from flask_appbuilder.fieldwidgets import BS3TextFieldWidget, BS3TextAreaFieldWidget, Select2Widget
from flask_appbuilder.forms import DynamicForm

# list of tuples for selecter widget
selector_choices = [('choice1', 'Choice1'), ('choice2', 'Choice 2')]

class SubmissionForm(DynamicForm):
    field1 = StringField(('Field1'),
        description= ('Description'),
        validators = [DataRequired()], widget=BS3TextFieldWidget())
    select1 = SelectField(('Selector1'),
        description=('Description'),
        validators = [DataRequired()], 
        widget = Select2Widget(),
        choices = selector_choices)
    field2 = StringField(('Field2'),
        description=('Description'),
        validators = [DataRequired()], widget=BS3TextFieldWidget())
    field3 = TextAreaField(('Field3'),
        description=('Description'),
        validators = [DataRequired()], widget=BS3TextAreaFieldWidget())