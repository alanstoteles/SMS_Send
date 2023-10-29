def main(service):
  if service == 'twilio':
    from twilio.rest import Client
  
    # Your Twilio account SID and Auth Token
    ACCOUNT_SID = 'AC5b14dac2113b441171ad1af1f650be05'
    AUTH_TOKEN = 'fbd993578367bf817b1176b897cfe052'
  
    # Create a client
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
  
    # Send the SMS
    message = client.messages.create(
        body="Hello from Twilio!",  # Your message content
        from_="+12512701257",  # Your Twilio phone number
        to="+491xxxxxxxxxx"  # The recipient's phone number
    )
  
    print(f"Message sent with SID: {message.sid}")
  else:
    pass
    
if __name__=='__main__':
  #main('twilio')
  main('ntfy')
