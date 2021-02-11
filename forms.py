from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SelectField,SubmitField
from wtforms.validators import DataRequired


class AddForm(FlaskForm):
    gender = SelectField('Gender: ',choices=[('Male', 'Male'), ('Female', 'Female')])
    relevant_experience = SelectField('Relevant Data Science Experience: ',choices=[('Has relevant experience', 'Has relevant experience'), ('No relevant experience', 'No relevant experience')])
    education_level = SelectField('Education: ',choices=[('Graduate', 'Graduate'), ('Masters', 'Masters'), ('Phd', 'Phd')])
    major_discipline = SelectField('Major: ',choices=[('Arts', 'Arts'), ('Business Degree', 'Business Degree'), ('STEM', 'STEM'), ('No Major', 'No Major'),('Humanities', 'Humanities'), ('Other', 'Other')])
    company_type = SelectField('Industry: ',choices=[('Early Stage Startup', 'Early Stage Startup'), ('Funded Startup', 'Funded Startup'), ('NGO', 'NGO'), ('Other', 'Other'), ('Public Sector', 'Public Sector'),('Pvt Ltd', 'Pvt Ltd')])
    company_size = SelectField('Company Size: ',choices=[('0-49', '0-49'), ('50-99', '50-99'), ('100-499', '100-499'), ('500-999', '500-999'), ('1000', '4999'),('5000', '9999'),('10000+', '10000+')])
    submit = SubmitField('Submit')

class DelForm(FlaskForm):
    id = IntegerField("Enter ID of person to remove: ")
    submit = SubmitField("Clear Record")


    