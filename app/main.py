# Run by typing python3 main.py

# **IMPORTANT:** only collaborators on the project where you run
# this can access this web server!

"""
    Bonus points if you want to have internship at AI Camp
    1. How can we save what user built? And if we can save them, like allow them to publish, can we load the saved results back on the home page? 
    2. Can you add a button for each generated item at the frontend to just allow that item to be added to the story that the user is building? 
    3. What other features you'd like to develop to help AI write better with a user? 
    4. How to speed up the model run? Quantize the model? Using a GPU to run the model? 
"""
# import basics
import os

# import stuff for our web server
from flask import Flask, request, redirect, url_for, render_template, session
from utils import get_base_url,model_input,text_list,print_list
# import stuff for our models
from aitextgen import aitextgen

# load up a model from memory. Note you may not need all of these options.
ai_pos = aitextgen(model_folder="pos_model/", to_gpu=False)
ai_neg = aitextgen(model_folder="neg_model/", to_gpu=False)

#ai = aitextgen(model="distilgpt2", to_gpu=False)

# setup the webserver
# port may need to be changed if there are multiple flask servers running on same server
port = 12345
base_url = get_base_url(port)


# if the base url is not empty, then the server is running in development, and we need to specify the static folder so that the static files are served
if base_url == '/':
    app = Flask(__name__)
else:
    app = Flask(__name__, static_url_path=base_url+'static')

app.secret_key = os.urandom(64)

# set up the routes and logic for the webserver


@app.route(f'{base_url}')
def home():
    return render_template('writer_home.html', generated=None)


@app.route(f'{base_url}', methods=['POST'])
def home_post():
    return redirect(url_for('results'))


@app.route(f'{base_url}/results/')
def results():
    if 'data' in session:
        data = session['data']
        return render_template('Write-your-story-with-AI.html', generated=data)
    else:
        return render_template('Write-your-story-with-AI.html', generated=None)


@app.route(f'{base_url}/generate_text/', methods=["POST"])

def generate_text():
    """
    view function that will return json response for generated text. 
    """
    genre = request.form['genre']
    sentiment = request.form['sentiment']
    prompt = request.form['prompt']
    length = int(request.form['length'])
    temp = round(float(request.form['temp']),1)
    review_number = int(request.form['review_number'] )
    
    input=model_input(prompt,genre,sentiment)
    
    if sentiment == 'Positive':
        generated = ai_pos.generate(
             n=review_number,
             batch_size=3,
             prompt=str(input),
             max_length=length,
             repitition_penalty=1.5,
             top_p=1,
             temperature=temp,
             return_as_list=True)
        data = {'generated_ls': generated}
        #session['data'] = '<font color="#0096FF">'+ print_list(generated)
        session['data'] = '<font color="#0096FF">'+'<div class="grid-wrapper">' + text_list(generated)+'</div>'+'</font>'
        #session['data'] = '<font color="#0096FF">'+str(length)+'</font>'
        return redirect(url_for('results'))

    else:
        generated = ai_neg.generate(
            n=review_number,
            batch_size=3,
            prompt=str(input),
            max_length=length,
            repitition_penalty=1.5,
            top_p=1,
            temperature=temp,
            return_as_list=True)
        data = {'generated_ls': generated}
        session['data'] = '<font color="#0096FF">'+'<div class="grid-wrapper"><br>' + text_list(generated)+'<br></div>'+'</font>'
        #session['data'] = '<font color="#0096FF">'+str(length)+'</font>'
        return redirect(url_for('results'))

# define additional routes here
# for example:
# @app.route(f'{base_url}/team_members')
# def team_members():
#     return render_template('team_members.html') # would need to actually make this page


if __name__ == '__main__':
    # IMPORTANT: change url to the site where you are editing this file.
    website_url = 'cocalc6.ai-camp.dev'

    print(f'Try to open\n\n    https://{website_url}' + base_url + '\n\n')
    app.run(host='0.0.0.0', port=port, debug=True)
    