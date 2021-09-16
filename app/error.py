from flask import render_template
from app import app

@app.errorhandler(404)
def four_Ow_four(error):
    '''
    An error page to render the function of 404
    '''
    return render_template('fourOwfour.html'),404