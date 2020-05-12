from django.shortcuts import render

from faker import Factory
from django.http import JsonResponse
from django.conf import settings

from twilio.rest import Client
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import (
    SyncGrant,
    ChatGrant
)

def app(request):
    return render(request, 'twilio/index.html')

def token(request):
    fake = Factory.create()
    return generateToken(fake.user_name())

def generateToken(identity):
    # Get credentials from environment variables
    account_sid      = 'AC3474991374127fe13a82f2329a8833ec'
    chat_service_sid = 'ISdcd0797d91454899a6967e188d13130e'
    sync_service_sid = 'IS1a1275f1c8f32d4182a0d276304b3d5e'
    api_sid          = 'SK699b582aa96ec8c9a36629ebbb4a1d52'
    api_secret       = '75EynZWCSYWoWKYlGDhLIOk1cjBBRniT'

    # Create access token with credentials
    token = AccessToken(account_sid, api_sid, api_secret, identity=identity)

    # Create a Sync grant and add to token
    if sync_service_sid:
        sync_grant = SyncGrant(service_sid=sync_service_sid)
        token.add_grant(sync_grant)

    # Create a Chat grant and add to token
    if chat_service_sid:
        chat_grant = ChatGrant(service_sid=chat_service_sid)
        token.add_grant(chat_grant)

    # Return token info as JSON
    return JsonResponse({'identity':identity,'token':token.to_jwt().decode('utf-8')})