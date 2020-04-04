from django import forms

COLOR_CHOICES=(
    ('black', '黒'),
    ('white', '白'),
    (' gray', 'グレー'),
    ('brown', '茶色')
)

class PostForm(forms.Form):
    your_color=forms.ChoiceField(
    label='色',
    choices=COLOR_CHOICES,
    required=True,
    disabled=False,
    widget=forms.Select(attrs={
        'id':'one',}))

    
