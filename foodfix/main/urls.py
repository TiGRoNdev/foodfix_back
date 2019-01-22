from rest_framework import routers

from .views import RestaurantViewSet, OrderViewSet, CustomerViewSet


router = routers.DefaultRouter()

router.register('customer', CustomerViewSet, base_name='customer')
router.register('order', OrderViewSet, base_name='order')
router.register('restaurant', RestaurantViewSet, base_name='restaurant')

urlpatterns = router.urls
