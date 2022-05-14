from django import forms
from .models import Article

# class ArticleForm(forms.ModelForm):
#     class Meta:
#         model = Article
#         fields = ['title', 'content']
class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    # def clean_title(self):
    #     cleaned_data = self.cleaned_data # dictionary
    #     print("cleaned data: ", cleaned_data)
        
    #     title = cleaned_data.get('title')
    #     # some conditions for cleaning data
    #     if title.lower().strip() == "the office": 
    #         raise forms.ValidationError('This is title is taken.')

    #     print("title: ", title)
    #     return title

    def clean(self):
        cleaned_data = self.cleaned_data
        print("all cleaned data: ", cleaned_data)

        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        # some conditions for cleaning data
        if title.lower().strip() == "the office": 
            self.add_error('title', 'this title is taken.') # the same with raise error
            # raise forms.ValidationError('This is title is taken.')

        if "fuck" in content.lower() or title.lower():
            self.add_error('content', "F*** cannot be in content.")
            raise forms.ValidationError('F*** is not allowed')
        return cleaned_data