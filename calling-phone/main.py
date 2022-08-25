from http import client
import os
from twilio.rest import Client

account_sid = "AC2fc9f21b3bcbb8ebfec4129eb1bd4253"
auth_token = "6ebd8bb60ba92d90bd5da97b74d445b0"

client = Client(account_sid,auth_token)

call = client.calls.create(
                        twiml='<Response><Say>Ahoy, World! Hello Baban bhaiya, this is your well wisher</Say></Response>',
                        to='+16047274226',
                        from_='+15005550006'
                    )

print(call.sid)