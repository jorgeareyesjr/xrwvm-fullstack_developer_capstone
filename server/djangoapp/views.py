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

# Create a `login_request` view to handle sign in request
@csrf_exempt
def login_user(request):
    # Get username and password from request.POST dictionary
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    # Try to check if provide credential can be authenticated
    user = authenticate(username=username, password=password)
    # Assign the username to `data`, overriding the previous value of `data`
    data = {"userName": username}
    if user is not None:
        # If user is valid, call login method to login current user
        login(request, user)
        # Add the username authentication status to `data`
        data = {"userName": username, "status": "Authenticated"}
        # Return a JSON response, the username and authentication status, to the frontend
        """
        The frontend will store this returned data to the browser window.sessionStorage.
        Once the window.sessionStorage data is set, the frontend now has the username and authentication status ready for use.
        The frontend uses `checkSession` to check if the user is authenticated.
        """
    return JsonResponse(data)

# Create a `logout_request` view to handle sign out request
def logout_request(request):
    # Logout user
    logout(request)
    data = {"userName":""}
    # Return a JSON response, an empty username and omitted authentication status, to the frontend
    """
    The frontend will clear the window.sessionStorage username data once the JSON response is received.
     The frontend uses `checkSession` to check if the user is authenticated.
    """
    return JsonResponse(data)

# Create a `registration` view to handle sign up request
# @csrf_exempt
# def registration(request):
# ...

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
