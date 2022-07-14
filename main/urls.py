from rest_framework.routers import SimpleRouter
from django.contrib import admin
from django.urls import path, include
from food.views import FoodReceptViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = SimpleRouter()
router.register('recepts', FoodReceptViewSet)


schema_view = get_schema_view(
   openapi.Info(
      title="Treasure Trove Of Recipes",
      default_version='ممتع ولذيذ',
      description="Burda senin icin her sey var",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="MY liCENSE"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)



urlpatterns = [

    #SWAGGER
    path(r'', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


    #FOOD
    path('api/', include('food.urls')),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),

    #USER
    path('api/v1/', include('users.urls')),


    #JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
