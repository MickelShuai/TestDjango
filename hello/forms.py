from django import forms
from hello.models import Publisher
from django.core.exceptions import ValidationError
# class PublisherForm(forms.Form):
#     name = forms.CharField(max_length= 30,label='姓名')
#     address = forms.CharField()
#     city = forms.CharField()
#     state_province = forms.CharField()
#     country = forms.CharField()
#     website = forms.URLField()

def validate_name(value):
    try:
        Publisher.objects.get(name=value)
        raise ValidationError('%s的信息已经存在'%value)
    except Publisher.DoesNotExist:
        pass


class PublisherForm(forms.ModelForm):
    name = forms.CharField(label='名称',validators=[validate_name])
    class Meta:
        model = Publisher
        exclude =('id',)