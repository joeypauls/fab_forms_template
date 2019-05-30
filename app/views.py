from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi, AppBuilder, BaseView, expose, has_access, SimpleFormView
from flask_babel import lazy_gettext as _
from flask import render_template, flash

from app import appbuilder
from . import appbuilder, db
from .forms import SubmissionForm
from .models import ContactGroup, Contact

class SubmissionFormView(SimpleFormView):
    form = SubmissionForm
    form_title = 'User Submission Form'
    message = 'Form Submitted'

    def form_get(self, form):
        form.field1.data = 'Prefilled Text'

    def form_post(self, form):
        # post process form
        flash(self.message, 'info')

appbuilder.add_view(SubmissionFormView, "Form", icon="fa-group", label=_('Form'),
                     category="Forms", category_icon="fa-cogs")


class ContactModelView(ModelView):
    datamodel = SQLAInterface(Contact)

    label_columns = {'contact_group':'Contacts Group'}
    list_columns = ['name','personal_cellphone','birthday','contact_group']

    show_fieldsets = [
        (
            'Summary',
            {'fields': ['name', 'address', 'contact_group']}
        ),
        (
            'Personal Info',
            {'fields': ['birthday', 'personal_phone', 'personal_cellphone'], 'expanded': False}
        ),
    ]

class GroupModelView(ModelView):
    datamodel = SQLAInterface(ContactGroup)
    related_views = [ContactModelView]

db.create_all()
appbuilder.add_view(
    GroupModelView,
    "List Groups",
    icon = "fa-folder-open-o",
    category = "Contacts",
    category_icon = "fa-envelope"
)
appbuilder.add_view(
    ContactModelView,
    "List Contacts",
    icon = "fa-envelope",
    category = "Contacts"
)


class GroupModelApi(ModelRestApi):
    resource_name = 'group'
    datamodel = SQLAInterface(ContactGroup)

appbuilder.add_api(GroupModelApi)
    

"""
    Application wide 404 error handler
"""

@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )

