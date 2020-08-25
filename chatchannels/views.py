from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.utils.safestring import mark_safe
import django.contrib.sessions
from .models import Chat, Message
import json


@login_required
def room(request, room_name):

    room_name = mark_safe(json.dumps(room_name))
    room_name_fixed = room_name.replace("\"","")
    room_name_int = int(room_name_fixed)
    username = mark_safe(json.dumps(request.user.username))
    chat = get_object_or_404(Chat, pk=room_name_int)
    
    context = {
    'room_name_json' : room_name,
    'username': username,
    'chat' : chat,
    }

    
    return render(request, 'chatchannels/room.html', context)

def last_10_messages(chat):
    
    return Message.objects.order_by('timestamp').filter(chat=chat)[:10]



