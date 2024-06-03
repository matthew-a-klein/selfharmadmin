from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import School
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from selfharmadmin.settings import EMAIL_HOST_USER
from .models import School
import json
import uuid
import requests
import os

@csrf_exempt
def send_email_report_view(request):

        # Extract school ID from request data
        if not request.body:
            return HttpResponse("Empty body in request", status=400)
       
        data = json.loads(request.body)
        # Extract school ID from the dictionary
        school_id = data.get('school_id')
        word_of_concern = data.get('concern')
        username = data.get('username')
        time = data.get('time')
        computer = data.get('computer')
        ip = data.get("ip")

        # # Check if school ID is provided
        if school_id is None:
            return HttpResponse("School ID is missing in the request data.", status=400)
        try:
            uuid.UUID(school_id)
        except ValueError:
            return HttpResponse("Invalid school ID format.", status=400)

        # Retrieve the school object or return a 404 error if not found
        school = get_object_or_404(School, id=school_id)
        # If school found send email
        send_email(school.admin_name, school.admin_email, username, word_of_concern, time, computer, ip)
        return HttpResponse("Email sent successfully.", status=200)

    
    
def send_email(admin_name, admin_email, user, word_of_concern, time, computer, ip):
    send_mail(
        subject="Suspicious activity detected",
        message=f"Dear {admin_name},"
           f" at {time}, {user} using {computer} @ {ip} typed {word_of_concern}, which is a suspicious keyword."
           f" This was flagged by the logging software.",
        from_email = EMAIL_HOST_USER,
        recipient_list= [admin_email],
        fail_silently=False
        )
