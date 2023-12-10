from rest_framework import viewsets

from siteSetting.models import Gallery, Header, Footer
from siteSetting.serializers.front import GalleryFrontSerializer, HeaderFrontSerializer, FooterFrontSerializer


class GalleryFrontViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GalleryFrontSerializer


class HeaderFrontViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Header.objects.all()
    serializer_class = HeaderFrontSerializer


class FooterFrontViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Footer.objects.all()
    serializer_class = FooterFrontSerializer
