from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from datetime import datetime

from django.http import JsonResponse
from django.contrib.auth import login, authenticate
import logging
import json
from django.views.decorators.csrf import csrf_exempt
from .populate import initiate


# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.
"""
Note on the `login_user` and `logout_request` views:
The `login_user` and `logout_request` views are implemented as function-based views.
These views handle the sign-in and sign-out requests from the frontend, respectively.
In both, the current users' authentication details are saved in the window.sessionStorage object.
Once in the session storage, the frontend can access the user's authentication status using the `checkSession()` function.
"""

# Create a `login_request` view to handle sign in request
@csrf_exempt
# When the user logs in:
def login_user(request):
    # Deserialize the request body to a data dictionary
    data = json.loads(request.body)
    # Extract the username and password from the data dictionary
    username = data['userName']
    password = data['password']
    # Try to authenticate user
    user = authenticate(username=username, password=password)
    # Reassign the data dictionary with the username
    data = {"userName": username}
    if user is not None:
        # If user is valid, call login method to login current user
        login(request, user)
        # Add the authentication status to the data dictionary
        data = {"userName": username, "status": "Authenticated"}
        # Return a JSON response, the user data dictionary, to the frontend
    return JsonResponse(data)

# Create a `logout_request` view to handle sign out request
# When the user logs out:
def logout_request(request):
    # Logout user
    logout(request)
    data = {"userName":""}
    # Return a JSON response, a user data dictionary, to the frontend
    return JsonResponse(data)

# Create a `registration` view to handle sign up request
@csrf_exempt
# When the user registers:
def registration(request):
    # Deserialize the request body to a data dictionary
    data = json.loads(request.body)
    # Extract the user data from the data dictionary
    first_name = data['firstName']
    last_name = data['lastName']
    email = data['email']
    username = data['userName']
    password = data['password']

    # Check if the username already exists
    username_already_exists = False
    if User.objects.filter(username=username).exists():
        username_already_exists = True
    else:
        # If the username does not already exist, log the username, for debugging purposes
        logger.debug("{} is new user".format(username))

    # If this is a new username
    if not username_already_exists:
        # Create a new user and save to the database
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            password=password,
        )
        # Log the newly created user in, following the normal login process
        login(request, user)
        # Reassign the data dictionary with the username and authentication status
        data = {"userName":username,"status":"Authenticated"}
        # Return a JSON response, the user data dictionary, to the frontend
        return JsonResponse(data)
    
    # If the username already exists, prevent a duplicate registration
    else:
        # Reassign the data dictionary with the username and an error message
        data = {"userName":username, "error":"Already Registered"}
        # Return a JSON response, the user data dictionary, to the frontend
        return JsonResponse(data)

# # Update the `get_dealerships` view to render the index page with
# a list of dealerships
# def get_dealerships(request):
# ...

# Create a `get_dealer_reviews` view to render the reviews of a dealer
# def get_dealer_reviews(request,dealer_id):
# ...

# Create a `get_dealer_details` view to render the dealer details
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request):
# ...
