def send_message(self_number, client, destinations, message, img_url):
    for destination in destinations:
        client.messages \
            .create(
                body=message,
                media_url= [img_url],
                from_=self_number,
                to=destination
            )