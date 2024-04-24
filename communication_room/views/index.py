from django.shortcuts import render, redirect
from communication_room.models import CommunicationRoom


def index(request):
    if request.method == 'POST' and request.POST['channels_id']:
        get_room_obj = CommunicationRoom.objects.filter(pk=request.POST['channels_id']).last()
        if get_room_obj:
            number = get_room_obj.allow_users
            if int(number) < 2:
                return redirect(f"/communication/{number}/join/")
        else:
            create = CommunicationRoom.objects.create(pk=request.POST['channels_id'], allow_users="1")
            if create:
                return redirect(f"/communication/{request.POST['channels_id']}/created/")
    context = {}
    return render(request, "home_index.html", context)