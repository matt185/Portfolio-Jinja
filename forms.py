from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

# WTFforms
class CreateFilterForm(FlaskForm):
    search_field = StringField(render_kw={"placeholder": "Search the project by technology (eg. post => postgresql)"})
    