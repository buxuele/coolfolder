from twilio.rest import Client


account_id = 'A***6319ca7c'
token = '194***de83fd37a22f'

client = Client(account_id, token)
text = 'anything you want 。。。 '


client.messages.create(
    to='+8***603',
    from_='+1***494',
    body=text
)



