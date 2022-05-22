from django import forms



from preferences.models import Preference


class PreferenceModelForm(forms.ModelForm):
    class Meta:
        model = Preference
        fields = '__all__'

    def clean(self):
        return super().clean()

    def clean_bio(self):
        bio = self.cleaned_data.get('bio')

        if len(bio) < 10:
            raise forms.ValidationError(
                'Bio must be at least 10 characters long.'
            )

        return bio

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if len(first_name) < 3:
            raise forms.ValidationError(
                'First name must be at least 3 characters long.'
            )

        return first_name

