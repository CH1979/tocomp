from django.contrib.auth.models import User
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Course, GroupDetail


class ProfileView(DetailView):
    model = User

    def get_object(self):
        return self.model.objects.filter(id=self.request.user.id)


class CourseCreateView(CreateView):
    model = Course
    fields = '__all__'
    success_url = 'group-list'


class CourseUpdateView(UpdateView):
    model = Course
    fields = '__all__'
    success_url = 'group-list'


class CourseDeleteView(DeleteView):
    model = Course
    success_url = 'group-list'


class GroupListView(ListView):
    model = GroupDetail
    context_object_name = 'group_list'
    queryset = GroupDetail.objects.filter(year=2020)


class GroupCreateView(CreateView):
    model = GroupDetail
    fields = '__all__'
