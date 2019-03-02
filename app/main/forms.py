from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, SelectField, RadioField
from wtforms.validators import Required

class CommentsForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    vote=RadioField('default field arguments', choices=[('1', 'UpVote'), ('1', 'DownVote')])
    submit = SubmitField('SUBMIT')  

class UpdateProfile(FlaskForm):
    bio = TextAreaField('we need your comment.',validators = [Required()])
    submit = SubmitField('Submit') 

class PitchForm(FlaskForm):
    category_id = SelectField('Select Category', choices=[('1', 'Story'), ('2', 'picking'), ('3', 'publicity'),('4','selling products')])
    content = TextAreaField('YOUR PITCH')
    submit = SubmitField('Create Pitch')

class UpvoteForm(FlaskForm):
    
    
    submit = SubmitField('Upvote')
    
 