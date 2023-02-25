from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from .forms import EditProfileForm, AddSkillsForm, EditSkillsForm, RegsiterPageForm,SendMassegesForm
from users.models import Profile


# Create your views here.


class UserLoginPage(View):
    def get(self, request):
        form = AuthenticationForm()
        context = {
            'form': form
        }
        return render(request, 'users/login.html', context)

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'you have succesfully register')
            return redirect('home')
        context = {
            'form': form
        }

        return render(request, 'users/login.html', context)


class RegisterPageView(View):
    def get(self, request):
        form = RegsiterPageForm()
        context = {
            "form": form
        }
        return render(request, 'users/register.html', context)

    def post(self, request):
        form = RegsiterPageForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'you have succesfully register')
            return redirect('home')

        context = {
            "form": form
        }
        return render(request, 'users/register.html', context)


class LogoutPageView(LoginRequiredMixin,View):
    def get(self, request):
        logout(request)
        return redirect('home')


class ProfilePageView(View):
    def get(self, request):
        profiles = Profile.objects.all()
        context = {
            "profiles": profiles
        }
        return render(request, 'profile/devolopers.html', context)
class ProfileDetailPageView(View):
    def get(self, request, pk):
        profiles = Profile.objects.get(id=pk)
        topskills = profiles.skills_set.exclude(description__exact='')
        otherskill = profiles.skills_set.filter(description="")
        context = {
            "profiles": profiles,
            'topskills': topskills,
            'otherskill': otherskill
        }
        return render(request, 'profile/devoloper_detail.html', context)


class UserAccountPageView(LoginRequiredMixin,View):
    def get(self, request):
        profiles = request.user.profile
        skills = profiles.skills_set.all()
        context = {
            "profiles": profiles,
            'skills': skills
        }

        return render(request, 'users/account.html', context)


class ProfileEditPageView(LoginRequiredMixin,View):
    def get(self, request):
        user = request.user.profile
        form = EditProfileForm(instance=user)
        context = {'form': form}
        return render(request, 'users/edit-profile.html', context)

    def post(self, request):
        user = request.user.profile
        form = EditProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('account')
        context = {'form': form}
        return render(request, 'users/edit-profile.html', context)


class AddSkillsPageView(LoginRequiredMixin,View):
    def get(self, request):
        form = AddSkillsForm()
        context = {"form": form}
        return render(request, 'users/add-skill.html', context)

    def post(self, request):
        profile = request.user.profile
        form = AddSkillsForm(data=request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            return redirect('account')
        context = {"form": form}
        return render(request, 'users/add-skill.html', context)


class EditSkillsPageView(LoginRequiredMixin,View):
    def get(self, request, pk):
        profile = request.user.profile
        skill = profile.skills_set.get(id=pk)
        form = EditSkillsForm(instance=skill)
        context = {"form": form,'skill':skill}
        return render(request, 'users/edit-skill.html', context)

    def post(self, request,pk):
        profile = request.user.profile
        skill = profile.skills_set.get(id=pk)
        form = EditSkillsForm(data=request.POST,instance=skill)
        if form.is_valid():
            form.save()
            return redirect('account')
        context = {"form": form}
        return render(request, 'users/edit-skill.html', context)
    
    
    
class DeleteSkillsPageView(LoginRequiredMixin,View):
    def get(self, request, pk):
        profile = request.user.profile
        skill = profile.skills_set.get(id=pk)
        context = {'skill':skill}
        return render(request, 'users/delete-skill.html', context)

    def post(self, request,pk):
        profile = request.user.profile
        skill = profile.skills_set.get(id=pk)
        skill.delete()
        return redirect('account')



class InboxPageView(LoginRequiredMixin,View):
    def get(self,request):
        profile = request.user.profile
        messages = profile.messages.all()
        unread_messages = messages.filter(is_read=False).count()
        context = {
            'messages':messages,
            'unread_messages':unread_messages
        }
        return render(request, 'users/inbox.html', context)


class MessagesPageView(LoginRequiredMixin,View):
    def get(self,request,pk):
        profile = request.user.profile
        message = profile.messages.get(id=pk)
        if message.is_read == False:
            message.is_read = True
            message.save()
        context = {
            'message': message
        }

        return render(request,'users/messages__view.html',context)
    
    
class SendMessagesPageView(LoginRequiredMixin,View):
    def get(self,request,pk):
        recipeent = Profile.objects.get(id=pk)
        sender = request.user.profile
        form = SendMassegesForm()
        context ={"form":form,"profile":recipeent}
        return render(request,'users/send_messages.html',context)
    
    def post(self,request,pk):
        recipeent = Profile.objects.get(id=pk)
        sender = request.user.profile
        form = SendMassegesForm(data=request.POST)
        if form.is_valid():
            send = form.save(commit=False)
            send.recipient = recipeent
            send.sender = sender
            if sender:
                send.name = sender.name
                send.email = send.email
            send.save()
            return redirect('profile-detail',pk=recipeent.id)
        context ={"form":form,"profile":recipeent}
        return render(request,'users/send_messages.html',context)
    
    
    
    