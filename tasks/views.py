from django.shortcuts import render

# Create your views here.
def get_tasks_list(request):
    return render(request, 'tasks/tasks_list.html')