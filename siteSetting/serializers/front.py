from rest_framework import serializers

from siteSetting.models import Gallery, Header, Footer


class GalleryFrontSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'


class HeaderFrontSerializer(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = '__all__'


class FooterFrontSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = '__all__'
