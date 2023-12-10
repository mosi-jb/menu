from rest_framework.routers import SimpleRouter

from product.view.front import CategoryFrontViewSet, ProductFrontViewSet

router = SimpleRouter()
router.register('category', CategoryFrontViewSet)
router.register('product', ProductFrontViewSet)

urlpatterns = [] + router.urls
