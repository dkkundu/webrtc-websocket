from django.shortcuts import render


def communication(request, room_id, created):
    context = {
        "created": created,
        "room_id": room_id
    }
    return render(request, "home_communication.html", context)