from django import forms


class CreatePostForm(forms.Form):
    location_name = forms.CharField(max_length=100, label="穴場スポットの名前")
    address = forms.CharField(max_length=200, label="住所")
    category = forms.ChoiceField(label="ジャンル")
    contents = forms.CharField(max_length=1000, label="共有したい内容", widget=forms.Textarea)
