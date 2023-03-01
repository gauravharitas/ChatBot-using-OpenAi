from flask import Flask
from twilio.twiml.voice_response import VoiceResponse
from twilio.rest import Client

ch=input("Enter 1 for outgoing call or press any key: ")

if ch=='1':
    account_sid = 'AC718582f0bdeb0381d24b80f4d443eef4'
    auth_token = '047b51ed07b026cbf09603316dfe2f2f'
    client = Client(account_sid, auth_token)
    #messages #body
    #calls #twiml #in call we use resonse and say
    message = client.calls \
        .create( 
             twiml='<Response><Say>This wikiHow teaches you how to get a girlfriend in Grand Theft Auto (GTA) V. Keep in mind that the process of getting a girlfriend in GTA V involves going to a strip club, which contains mature content.</Say></Response>',
             from_='+12017442821',
             to='+917093009470'
         )

    print(message.sid)
    print("Pickup your Phone !!!")

else:
    app=Flask(__name__)
    @app.route("/voice", methods=['GET', 'POST'])

    def voice():
        resp=VoiceResponse()
        resp.say("Hello sir Welcome to GAURAV HARITAS corporation, how may i help you")
        return str(resp)

    if __name__ == "__main__":
        app.run(debug=True)
    
