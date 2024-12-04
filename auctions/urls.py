from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("NewListing", views.createListing, name="newListing"),
    path('listing/item-<str:listingCode>', views.listingPage, name='listingPage'),
    path('watchlist/', views.watchlist, name='watchlistPage'),
    path('categories/', views.categories, name='categoriesPage'),
    path('categories/<str:listingsCategory>', views.filtered, name='filteredPage'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register")
]
