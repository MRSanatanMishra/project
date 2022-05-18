from django import forms
from .models import Profile,NFT

class ProfileForm(forms.ModelForm):
    """Form definition for Profile."""

    class Meta:
        """Meta definition for Profileform."""

        model = Profile
        fields = ('name','email','profilepic','location','about',)


class NFTForm(forms.ModelForm):
    """Form definition for NFT."""

    class Meta:
        """Meta definition for NFTform."""

        model = NFT
        fields = ('title','worthInD','owner','image','token','category','summary','currency')


