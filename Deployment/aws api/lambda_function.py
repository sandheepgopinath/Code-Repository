import json

def process_string(text):
    ''' The  function takes as input a string and adds a copy right symbol
    after the names of the companies as specified in keywords '''
    
    import re
    keywords=['deliotte','oracle','google','microsoft','amazon']                # List of words which has to be replaced
    response_text=''                                                            # Creating an empty response text
    text=text.split(' ')                                                        # Splitting the string by spaces
    for word in text:                                                           # Recreating the text with new words
        if word.lower() in keywords:                                                
            word=word+'©'
        else:
            pass
        response_text+=word+' '
    return response_text
    

def lambda_handler(event, context):
    """ The lambda function will take a text as input from the user and add the 
    copyrighted symbol after the given keywords. 
    Eg : Google : Google©
         Oracle : Oracle©
         Amazon : Amazon©
         Deloitte: Deloitte©
         Microsoft: Microsoft©
    """

    user_input=event['queryStringParameters']["text"]                            # To get text input from the event handler
    user_output=process_string(user_input)
   
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(user_output)
    }

