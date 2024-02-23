import json
import openai

def lambda_handler(event, context):
    user_query = event['currentIntent']['slots']['QuerySlot']  # Assume you have a slot for the user query

    openai.api_key = 'your-openai-api-key'

    response = openai.Completion.create(
        model="text-davinci-003",  # Use an appropriate model
        prompt=user_query,
        temperature=0.7,
        max_tokens=150,
        n=1,
        stop=None
    )

    reply = response.choices[0].text.strip()

    return {
        'dialogAction': {
            'type': 'Close',
            'fulfillmentState': 'Fulfilled',
            'message': {
                'contentType': 'PlainText',
                'content': reply
            }
        }
    }
