from django.urls import path

from users.views import UserLoginPage, RegisterPageView, ProfilePageView, ProfileDetailPageView, LogoutPageView, \
    UserAccountPageView, ProfileEditPageView, AddSkillsPageView, EditSkillsPageView, DeleteSkillsPageView, \
    InboxPageView,MessagesPageView,SendMessagesPageView

urlpatterns = [

    path('login/', UserLoginPage.as_view(), name='login'),
    path('logout/', LogoutPageView.as_view(), name='logout'),
    path('register/', RegisterPageView.as_view(), name='register'),
    path('inbox/', InboxPageView.as_view(), name='inbox'),
    path('send_messages/<str:pk>/', SendMessagesPageView.as_view(), name='send_messages'),
    path('message/<int:pk>/', MessagesPageView.as_view(), name='message'),
    path('devolopers/', ProfilePageView.as_view(), name='profile'),
    path('devolopers/<int:pk>', ProfileDetailPageView.as_view(), name='profile-detail'),
    path('account/', UserAccountPageView.as_view(), name='account'),
    path('edit-profile/', ProfileEditPageView.as_view(), name='edit-profile'),
    path('add-skill/', AddSkillsPageView.as_view(), name='add-skill'),
    path('edit-skill/<int:pk>/', EditSkillsPageView.as_view(), name='edit-skill'),
    path('delete-skill/<int:pk>/', DeleteSkillsPageView.as_view(), name='delete-skill'),
]
