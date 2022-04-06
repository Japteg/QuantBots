from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from loginmgmt.fyers_login import FyersLogin


@api_view(('GET',))
def home(request):
    logged_in = request.GET.get('logged_in', False)
    text = 'Not logged In'
    if logged_in:
        text = 'Logged In'
    return render(request, 'index.html', context={'text': text})


@api_view(('GET',))
def fyers_login(request):
    return FyersLogin().login(request.GET)


@api_view(('GET',))
def get_user_profile(request):
    profile = FyersLogin.fyers_model.get_profile()
    funds = FyersLogin.fyers_model.funds()
    holdings = FyersLogin.fyers_model.holdings()

    data = {
        'profile': profile,
        'funds': funds,
        'holdings': holdings
    }
    return Response(data)
