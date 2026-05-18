from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse


def api_root(request):
    return JsonResponse({
        "status": "running",
        "message": "Atul Kumar — Portfolio API",
        "endpoints": {
            "contact_form": "/api/contact/",
            "admin_panel": "/admin/",
        }
    })


urlpatterns = [
    path('', api_root),
    path('admin/', admin.site.urls),
    path('api/contact/', include('contact.urls')),
]