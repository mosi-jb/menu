from rest_framework.routers import SimpleRouter

from siteSetting.view.admin import GalleryViewSet, HeaderViewSet, FooterViewSet

router = SimpleRouter()
router.register('gallery', GalleryViewSet)
router.register('header', HeaderViewSet)
router.register('footer', FooterViewSet)

urlpatterns = [] + router.urls
