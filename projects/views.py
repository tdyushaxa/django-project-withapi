from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from projects.forms import AddProjectForm, CommentCreationForm, EditReviewForm
from projects.models import Project, Tag
from django.db.models import Q
from users.models import Profile

# Create your views here.
class HomePageView(View):
    def get(self, request):
        search_query = ''
        if request.GET.get('q'):
            search_query = request.GET.get('q')
        tag = Tag.objects.filter(name__icontains=search_query)
        owner = Profile.objects.filter(name__icontains=search_query)
        project = Project.objects.distinct().filter(
            Q(title__icontains=search_query) | Q(tags__in=tag) | Q(owner__in=owner))
        page = request.GET.get('page')
        result = 3
        paginator = Paginator(project, result)
        try:
            project = paginator.page(page)
        except PageNotAnInteger:
            page = 1
            project = paginator.page(page)
        except EmptyPage:
            page = paginator.num_pages
            project = paginator.page(page)

        context = {
            'projects': project,
            'search_query': search_query,
            'paginator': paginator

        }
        return render(request, 'home.html', context)


class ProjectDetailPageView(View):
    def get(self, request, pk):
        project = Project.objects.get(pk=pk)
        count = project.review_set.all().count()
        form = CommentCreationForm()
        context = {
            'project': project,
            'form': form,
            'count': count,

        }
        return render(request, 'project/project_view.html', context)

    def post(self, request, pk):
        project = Project.objects.get(pk=pk)
        form = CommentCreationForm(data=request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.owner = request.user.profile
            review.project = project
            review.save()
            return redirect('detail', pk=project.id)
        context = {
            'project': project,
            'form': form
        }
        return render(request, 'project/project_view.html', context)


class EditReviewView(LoginRequiredMixin, View):
    def get(self, request, project_id, review_id):
        project = Project.objects.get(id=project_id)
        review = project.review_set.get(id=review_id)
        form = EditReviewForm(instance=review)
        context = {
            'project': project,
            'form': form,
            'review': review

        }
        return render(request, 'review/update_review.html', context)

    def post(self, request, project_id, review_id):
        project = Project.objects.get(id=project_id)
        review = project.review_set.get(id=review_id)
        form = EditReviewForm(data=request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('detail', pk=project.id)
        context = {
            'project': project,
            'form': form,
            'review': review

        }
        return render(request, 'review/update_review.html', context)


class DeleteReviewView(LoginRequiredMixin, View):
    def get(self, request, project_id, review_id):
        project = Project.objects.get(id=project_id)
        review = project.review_set.get(id=review_id)
        context = {
            'project': project,
            'review': review
        }
        return render(request, 'review/delete_review.html', context)

    def post(self, request, project_id, review_id):
        project = Project.objects.get(id=project_id)
        review = project.review_set.get(id=review_id)
        review.delete()
        return redirect('detail', pk=project.id)


class AddProjectPageView(LoginRequiredMixin, View):
    def get(self, request):
        create_project = AddProjectForm()
        context = {
            'form': create_project
        }
        return render(request, 'project/add_project.html', context)

    def post(self, request):
        user = request.user.profile
        create_project = AddProjectForm(request.POST, request.FILES)
        if create_project.is_valid():
            form = create_project.save(commit=False)
            form.owner = user
            form.save()
            return redirect('home')
        context = {
            'form': create_project
        }
        return render(request, 'project/add_project.html', context)


class UpdateProjectPageView(LoginRequiredMixin, View):
    def get(self, request, pk):
        project = Project.objects.get(id=pk)
        update_form = AddProjectForm(instance=project)
        context = {
            'form': update_form,
            'project': project
        }
        return render(request, 'project/update_project.html', context)

    def post(self, request, pk):
        project = Project.objects.get(id=pk)
        update_form = AddProjectForm(
            request.POST, request.FILES, instance=project)
        if update_form.is_valid():
            update_form.save()
            return redirect('home')
        context = {
            'form': update_form
        }
        return render(request, 'project/update_project.html', context)


class DeleteProjectPageView(LoginRequiredMixin, View):
    def get(self, request, pk):
        project = Project.objects.get(id=pk)
        context = {
            'project': project
        }
        return render(request, 'project/delete.html', context)
    def post(self, request, pk):
        project = Project.objects.get(id=pk)
        project.delete()
        return redirect('account')
