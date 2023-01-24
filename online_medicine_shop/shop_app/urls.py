
from django.urls import path
# from . import views
from .views import BrandCreateAPIView, BrandRetrieveAPIView, BrandListAPIView, BrandUpdateAPIView, CategoryListAPIView, \
    CategoryRetrieveAPIView, CategoryCreateAPIView, CategoryUpdateAPIView, ProductListAPIView, ProductCreateAPIView, \
    ProductRetrieveAPIView, ProductUpdateAPIView, CartListAPIView, CartCreateAPIView, CartRetrieveAPIView, \
    CartUpdateAPIView, OrderListAPIView, OrderRetrieveAPIView, OrderCreateAPIView, OrderUpdateAPIView, CouponListAPIView, \
    CouponRetrieveAPIView, CouponCreateAPIView, CouponUpdateAPIView, AddressListAPIView, AddressRetrieveAPIView, \
    AddressCreateAPIView, AddressUpdateAPIView, ImageListAPIView, ImageCreateAPIView
urlpatterns = [
    path('brand/create/', BrandCreateAPIView.as_view(), name='brand_create'),
    path('brand/detail/<int:pk>/', BrandRetrieveAPIView.as_view(), name='brand_details'),
    path('brand/list/all/', BrandListAPIView.as_view(), name='all_brands_list'),
    path('brand/update/<int:pk>/', BrandUpdateAPIView.as_view(), name='update_brand'),

    path('category/list/all/', CategoryListAPIView.as_view(), name='all_category'),
    path('category/detail/<int:pk>/', CategoryRetrieveAPIView.as_view(), name='category_detail'),
    path('category/create/', CategoryCreateAPIView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', CategoryUpdateAPIView.as_view(), name='category_update'),

    path('product/list/all/', ProductListAPIView.as_view(), name='product_list'),
    path('product/create/', ProductCreateAPIView.as_view(), name='product_create'),
    path('product/detail/<int:pk>/', ProductRetrieveAPIView.as_view(), name='product_details'),
    path('product/update/<int:pk>/', ProductUpdateAPIView.as_view(), name='update_product'),

    path('cart/list/all/', CartListAPIView.as_view(), name='cart_list'),
    path('cart/create/', CartCreateAPIView.as_view(), name='cart_create'),
    path('cart/detail/<int:pk>/', CartRetrieveAPIView.as_view(), name='cart_detail'),
    path('cart/update/<int:pk>/', CartUpdateAPIView.as_view(), name='update_cart'),

    path('order/list/all/', OrderListAPIView.as_view(), name='order_list'),
    path('order/detail/<int:pk>/', OrderRetrieveAPIView.as_view(), name='order_detail'),
    path('order/create/', OrderCreateAPIView.as_view(), name='order_create'),
    path('order/update/<int:pk>/', OrderUpdateAPIView.as_view(), name='order_update'),

    path('coupon/list/all/', CouponListAPIView.as_view(), name='coupon_list'),
    path('coupon/detail/<int:pk>/', CouponRetrieveAPIView.as_view(), name='coupon_details'),
    path('coupon/create/', CouponCreateAPIView.as_view(), name='coupon_create'),
    path('coupon/update/<int:pk>/', CouponUpdateAPIView.as_view(), name='coupon_update'),

    path('address/list/all/', AddressListAPIView.as_view(), name='address_list'),
    path('address/detail/<int:pk>/', AddressRetrieveAPIView.as_view(), name='detail_address'),
    path('address/create/', AddressCreateAPIView.as_view(), name='create_address'),
    path('address/update/<int:pk>/', AddressUpdateAPIView.as_view(), name='update_address'),


    path('image/list/all/', ImageListAPIView.as_view(), name='image_list'),
    # path('image/create/', ImageCreateViewSet.as_view({'get': 'create'}), name='image_create'),
    path('image/create/', ImageCreateAPIView.as_view(), name='image_create'),


]
