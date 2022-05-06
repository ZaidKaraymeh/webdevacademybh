from django import forms

from .models import CourseSignUp



class CourseSignUpForm(forms.ModelForm):
    class Meta:
        model = CourseSignUp
        fields = ['full_name', "mobile_number", "email"]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter full name here..."}), 
            'mobile_number': forms.TextInput(attrs={'class': 'form-control','placeholder': "Enter mobile number here..."}),
            'email': forms.TextInput(attrs={'class': 'form-control','placeholder': "Enter email here..."}),
        }

    def __init__(self, *args, **kwargs):
        super(CourseSignUpForm  , self).__init__(*args, **kwargs)

        self.fields['full_name'].widget.attrs['style'] = 'width:100%; height:40px;'
        self.fields['mobile_number'].widget.attrs['style'] = 'width:100%; height:40px;'
        self.fields['email'].widget.attrs['style'] = 'width:100%; height:40px;'
        self.fields['full_name'].widget.attrs['class'] = 'form-control'
        self.fields['mobile_number'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['full_name'].label = ''
        self.fields['mobile_number'].label = ''
        self.fields['email'].label = ''