from django import forms


class SearcherGoogle(forms.Form):
    package_name = forms.CharField(label='Package name ', max_length=100,widget=forms.TextInput(attrs={'placeholder': 'cn.xender&hl=en'}))


class SearcherApp(forms.Form):
    name = forms.CharField(label='Name', max_length=100 ,widget = forms.TextInput(attrs={'placeholder':'Rowan McPaddles'}))
    appl_id = forms.CharField(label='Application ID', max_length=100, widget = forms.TextInput(attrs={'placeholder':'1237067595'}))


