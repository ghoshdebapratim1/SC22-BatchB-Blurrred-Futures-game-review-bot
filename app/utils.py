import json
import os

def get_base_url(port:int) -> str:
    '''
    Returns the base URL to the webserver if available.
    
    i.e. if the webserver is running on coding.ai-camp.org port 12345, then the base url is '/<your project id>/port/12345/'
    
    Inputs: port (int) - the port number of the webserver
    Outputs: base_url (str) - the base url to the webserver
    '''
    
    try:
        info = json.load(open(os.path.join(os.environ['HOME'], '.smc', 'info.json'), 'r'))
        project_id = info['project_id']
        base_url = f'/{project_id}/port/{port}/'
    except Exception as e:
        print(f'Server is probably running in production, so a base url does not apply: \n{e}')
        base_url = '/'
    return base_url
    
#function to add correct and or comma
def and_syntax(alist):
    if len(alist) == 1:
        alist = "".join(alist)
        return alist
    elif len(alist) == 2:
        alist = " and ".join(alist)
        return alist
    elif len(alist) > 2:
        alist[-1] = "and " + alist[-1]
        alist = ", ".join(alist)
        return alist
    else:
        return
    
    
    
def model_input(game_name,game_genre,game_temperature,game_length,review_sentiment):
    
    game_temperature = str(game_temperature)
    game_length = str(game_length)
    output= 'Game Name: '+game_name+'<br> Game Genre: '+game_genre+'<br> Review Sentiment: '+review_sentiment+ '<br> Temperature(Craziness): ' +game_temperature+ '<br> Review Length: '+game_length+'<br> Review: '

    
    return output 


def print_list(listname):
    sep="<br>--------------------<br>"
    new_list=[]
    for element in listname:
        new_list.append(element+sep)
        
    return ' '.join(new_list)
        
    
def text_list(review_list):
    new_list=[]
    for review in review_list:
        new_list.append('<div id="review"> <br> <div id="headers"> First box </div>' + review + '<br> </div>')
        
        return ' '.join(new_list)





