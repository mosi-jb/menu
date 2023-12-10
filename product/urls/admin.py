from rest_framework.routers import SimpleRouter

from product.view.admin import CategoryViewSet, ProductViewSet

router = SimpleRouter()
router.register('category', CategoryViewSet)
router.register('product', ProductViewSet)

urlpatterns = [] + router.urls
