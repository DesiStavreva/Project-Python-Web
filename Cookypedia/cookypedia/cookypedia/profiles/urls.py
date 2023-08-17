from django.urls import path, include

from cookypedia.profiles.views import RegisterUserView, \
    LoginUserView, LogoutUserView, ProfileDetailsView, UsersListView, ProfileEditView, ProfileDeleteView

urlpatterns = (
    path('register/', RegisterUserView.as_view(), name='register user'),
    path('login/', LoginUserView.as_view(), name='login user'),
    path('logout/', LogoutUserView.as_view(), name='logout user'),
    path('list/', UsersListView.as_view(), name='profiles list'),
    path('<int:pk>/', include([
        path('', ProfileDetailsView.as_view(), name='profile details'),
        path('edit/', ProfileEditView.as_view(), name='profile edit'),
        path('delete/', ProfileDeleteView.as_view(), name='profile delete'), ]
    ))
)
