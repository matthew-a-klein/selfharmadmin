from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import School
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

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
        # # Check if school ID is provided
        if school_id is None:
            return HttpResponse("School ID is missing in the request data.", status=400)
        try:
            uuid.UUID(school_id)
        except ValueError:
            return HttpResponse("Invalid school ID format.", status=400)

        # Retrieve the school object or return a 404 error if not found
        school = get_object_or_404(School, id=school_id)
        
        #If school found send email
        status_code = send_email(school.admin_name, school.admin_email, username, word_of_concern, time)
        if status_code == requests.codes.ok:
            return HttpResponse("Email sent successfully.", status=200)
        else: 
            return HttpResponse("Error sending email.", status=400 )
    
    
def send_email(admin_name, admin_email, user, word_of_concern, time):

    api_key = os.environ.get("SMTP2GO_API_KEY")
    server_email = os.environ.get("SERVER_EMAIL")
    payload = {
        "api_key": api_key,
        "to": [
            f"{admin_name} <{admin_email}>"
        ],
        "sender": f"<{server_email}>",
        "subject": "Suspicious word or phrase typed",
        "text_body": f"Dear {admin_name},"
           " at {time}, {user} typed {word_of_concern}."
           " This was flagged by the logging software." }
    headers = { "Content-Type": "application/json" }

    res = requests.post("https://api.smtp2go.com/v3/email/send", headers=headers, data=json.dumps(payload))
    return res.status_code