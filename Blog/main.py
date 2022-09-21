from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db

main = Blueprint('main', __name__)

posts = [{"id":1,"title":"First post","desc":"This is first post description"},
        {"id":2,"title":"Second post","desc":"This is Second post description"},
        {"id":3,"title":"Third post","desc":"This is Third post description"},
        {"id":4,"title":"Forth post","desc":"This is 4th post description"},
        {"id":5,"title":"Fifth post","desc":"This is 5th post description"}
        ]

@main.route('/dashboard')
@login_required
def dashboard():
    context = {"name":current_user.name,"posts":posts}
    return render_template('dashboard.html', **context)

@main.route('/detail/<int:id>')
@login_required
def detail(id):
    detail_post = dict()
    for post in posts:
        if int(post['id'])==int(id):
            detail_post['title'] = post['title']
            detail_post['desc'] = post['desc']
    return render_template('detail.html', **detail_post)