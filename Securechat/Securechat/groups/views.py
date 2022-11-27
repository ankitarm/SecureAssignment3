
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Group, Message

@login_required
def groups(request):
    groups = Group.objects.all()

    return render(request, 'groups/groups.html', {'groups': groups})

@login_required
def group(request, slug):
    group = Group.objects.get(slug=slug)
    messages = Message.objects.filter(group=group)[0:25]

    return render(request, 'groups/group.html', {'group': group, 'messages': messages})