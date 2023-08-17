
from django.contrib.auth.decorators import login_required

from django.contrib.auth import views as auth_views, login, authenticate, get_user_model
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import mixins as auth_mixins
from django.templatetags.static import static
from django.utils.translation import gettext, gettext_lazy as _

from cookypedia.profiles.forms import RegisterUserForm
from cookypedia.profiles.models import CustomUser
from cookypedia.recipe.models import RecipeModel


UserModel = get_user_model()


class RegisterUserView(views.CreateView):
    template_name = 'profiles/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)

        return result


class LoginUserView(auth_views.LoginView):
    template_name = 'profiles/login.html'


class LogoutUserView(auth_views.LogoutView):
    pass


@login_required
def func_view(request):
    pass


class UsersListView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = UserModel
    template_name = 'profiles/profiles-list.html'


class ProfileDetailsView(views.DetailView):
    template_name = 'profiles/profile-details.html'
    model = UserModel

    profile_image = static('images/default.jpg')

    def get_profile_image(self):
        if self.object.profile_image is not None:
            return self.object.profile_image
        return self.profile_image

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['profile_image'] = self.get_profile_image()

        return context


class ProfileEditView(views.UpdateView):
    template_name = 'profiles/profile-edit.html'
    model = CustomUser
    fields = ['profile_image', 'email', 'first_name', 'last_name', 'age']
    success_url = reverse_lazy('index')


class ProfileDeleteView(views.DeleteView):
    template_name = 'profiles/profile-delete.html'
    model = CustomUser
    success_url = reverse_lazy('index')