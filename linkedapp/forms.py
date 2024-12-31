from django import forms
from django.utils.safestring import mark_safe

class SearchForm(forms.Form):

    country = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control country-search-input',
            'placeholder': 'Search country...',
            'autocomplete': 'off'
        }),
        label='Country'
    )

    job_title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        initial='Data scientist',
        required=False,
        label='Job title'
    )

    show_similar = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        label='Show similar jobs?'
    )

    include_keywords = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        initial='machine learning',
        required=False,
        label='Location or keywords to include'
    )

    exclude_keywords = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        initial='junior',
        required=False,
        label='Keywords to exclude'
    )

    education = forms.ChoiceField(
        choices=[
            ('', 'All candidates'),
            ('Bachelor', 'Bachelor'),
            ('Master', 'Master'),
            ('PhD', 'PhD')
        ],
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Education'
    )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['country'].widget.attrs.update({
            'data-country-dropdown': True,
            'id': 'country-input'
        })

    # @property
    # def media(self):
    #     css = {
    #         'all': ('css/custom-form.css',),
    #     }
    #     return forms.Media(css=css)


    # def render_country_field(self):
    #     country_input = self.fields['country']
    #     html = '<div class="country-search-wrapper">'
    #     html += f'<input type="text" name="{country_input.name}"'
    #     html += '</div>'
    #     return mark_safe(html)

    # def render_education_field(self):
    #     education_select = self.fields['education']
    #     html = '<select name="{}">'.format(education_select.name)
    #     for choice, display in education_select.choices:
    #         selected = choice if self.data.get(education_select.name) == choice else ''
    #         html += '<option value="{}" {}>{}</option>'.format(choice, 'selected' if selected else '', display)
    #     html += '</select>'
    #     return mark_safe(html)

    # def render_form(self):
    #     html = '<div class="card">'
    #     html += '<h3 class="h3 mb-4">Easily use Google to search profiles on LinkedIn</h3>'
    #     html += '<form id="searchForm" class="mb-4">'
        
    #     html += self.render_country_field()
    #     html += self.render_education_field()
        
    #     html += '</form></div>'
    #     return mark_safe(html)