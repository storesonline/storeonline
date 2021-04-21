from django import forms

from .models import Comments, MyOrder

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'body',)

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = ''
        self.fields['body'].label = ''

class MyOrderForm(forms.ModelForm):
    class Meta:
        model = MyOrder
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super(MyOrderForm, self).__init__(*args, **kwargs)
    #     self.fields['name'].label = ''
    #     self.fields['body'].label = ''