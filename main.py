# env var access
from functions.image_scraper import get_noaa_image_url
from functions.message_builder import build_message
from functions.sms import send_message
from twilio.rest import Client
from dotenv import dotenv_values


def send_update(numbers):
    # config will be a dictionary of the variables
    config = dotenv_values(".env") 

    # get image url
    page_url = config['NOAA_PAGE_URL']
    image_url = get_noaa_image_url(page_url)
    message_body = build_message(page_url)

    # send messages
    client = Client( config["TWILIO_SID"], config['TWILIO_TOKEN'])

    send_message(
        config['TWILIO_NUMBER'],
        client,
        numbers,
        message_body,
        image_url
    )


if __name__ == "__main__":
    send_update([
        "+19542538660"
    ])