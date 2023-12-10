from rest_framework.routers import SimpleRouter

from siteSetting.view.admin import GalleryViewSet, HeaderViewSet, FooterViewSet
from siteSetting.view.front import GalleryFrontViewSet, HeaderFrontViewSet, FooterFrontViewSet

router = SimpleRouter()
router.register('gallery', GalleryFrontViewSet)
router.register('header', HeaderFrontViewSet)
router.register('footer', FooterFrontViewSet)

urlpatterns = [] + router.urls
