from app.models import articles
from flask import render_template
from app import app
from .request import get_articles, get_sources


# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    general_sources = get_sources('general')
    news_business = get_sources('business')
    technology_sources = get_sources('technology')
    entertainment_sources = get_sources('entertainment')
    science_sources =get_sources('science')
    health_sources = get_sources('health')
    sports_sources = get_sources('sports')
    # print(general_news)
    title = 'Home - Welcome to The best News Review Website Online'
    return render_template('index.html', title = title,general = general_sources,business=news_business,technology =technology_sources,enternainment= entertainment_sources,sports =sports_sources,science = science_sources,health= health_sources)


@app.route('/source/<source_id>')
def artcicles(source_id):

    '''
    View news page function that returns the news details page and its data
    '''
    
    return render_template('index.html',id = source_id)

@app.route('/source/<int:id>')
def source(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    source = get_sources(id)
    title = f'{source.title}'

    return render_template('news.html',title = title,source= source)    


@app.route('/articles/<id>')
def article(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    article = get_articles(id)
    title = f'{id}'

    return render_template('news.html',title = title,article= article)        