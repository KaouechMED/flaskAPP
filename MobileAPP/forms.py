from flask_wtf import FlaskForm
from wtforms import SearchField,PasswordField,SubmitField
from wtforms.validators import Length,EqualTo,Email,DataRequired,ValidationError
from MobileAPP.models import User


class RegisterForm(FlaskForm):
    class Meta:
        csrf = False
    def validate_username(self,username_to_check):
        user=User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('username already exist ! try another')
    
    def validate_email_address(self,email_address_to_check):
        email_address=User.query.filter_by(email=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('email address already exist ! try another')
        
    def validate_cin(self,cin_to_check):
        cin=User.query.filter_by(cin=cin_to_check.data).first()
        if cin:
            raise ValidationError('cin already exist !')
        
    
    username=SearchField(label='Username:',validators=[Length(min=4,max=30),DataRequired()])
    email_address=SearchField(label='email:',validators=[Email(),DataRequired()])
    cin=SearchField(label='cin:',validators=[Length(min=8),DataRequired()])
    password=PasswordField(label='Password:',validators=[Length(min=6),DataRequired()])
    password_confirm=PasswordField(label='Confirm Password:',validators=[EqualTo('password'),DataRequired()])
    submit=SubmitField(label='Create Account')
    
    
class LoginForm(FlaskForm):
    class Meta:
        csrf = False
    username=SearchField(label='Username:',validators=[DataRequired()])
    password=PasswordField(label='Password:',validators=[DataRequired()])
    submit=SubmitField(label='Sign in')
    
