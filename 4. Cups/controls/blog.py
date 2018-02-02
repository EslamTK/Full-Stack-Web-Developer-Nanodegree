from controls import *
from core import *
from core.user import check_token, check_ownership
from models.blog import Blog

blogController = Blueprint('blogController', __name__)


def get_user_token(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        kwargs['token'] = request.cookies.get('token', None)
        return func(*args, **kwargs)

    return decorated


@blogController.route('/blogs.json')
def json_api():
    """Json Api which will provide a list of the blogs in all categories stored in the application"""
    result = blogs.get_all()
    return jsonify(blogs=[b.serialize for b in result])


@blogController.route('/')
@blogController.route('/blog')
@blogController.route('/blog/<string:category_name>')
@blogController.route('/<string:category_name>')
@get_user_token
@check_token
def get_blogs(is_logged, request_user, category_name=None):
    """The main root page that displays the blogs in the application in all categories or in a specific category"""

    if category_name:
        result = blogs.get_by_category(category=category_name)
    else:
        result = blogs.get_all()
    return render_template('index.html', blogs=result, categories=categories.get_all(), is_logged=is_logged)


@blogController.route('/blog/<int:blog_id>', methods=['GET'])
@get_user_token
@check_ownership
def get_blog(is_logged, is_owner, request_blog, blog_id):
    """A route to get the content of the blog"""

    return render_template('blog.html', categories=categories.get_all(),
                           blog=request_blog, is_logged=is_logged, is_owner=is_owner)


@blogController.route('/blog/new', methods=['GET', 'POST'])
@get_user_token
@check_token
def add_blog(is_logged, request_user):
    """The route in which the user has the ability to add new blog"""

    if not is_logged:
        abort(401)

    if request.method == 'GET':
        return render_template('new_blog.html', categories=categories.get_all(), blog=None, is_logged=is_logged)

    else:
        title = request.form['title']
        content = request.form['content']
        category_id = request.form['category']

        new_blog = Blog(title=title, content=content, category_id=category_id, user_id=request_user.id)

        blogs.add(new_blog)
        unit_of_work.save()

        return make_response(redirect(url_for('blogController.get_blog', blog_id=new_blog.id)))


@blogController.route('/blog/<int:blog_id>/edit', methods=['GET', 'POST'])
@get_user_token
@check_ownership
def update_blog(is_logged, is_owner, request_blog, blog_id):
    """The route to edit the blog content if the user owns the blog"""

    if not is_owner:
        abort(401)

    if request.method == 'GET':
        return render_template('new_blog.html',
                               categories=categories.get_all(), blog=request_blog, is_logged=is_logged)
    else:
        request_blog.title = request.form['title']
        request_blog.content = request.form['content']
        request_blog.category_id = request.form['category']

        unit_of_work.save()

        return make_response(redirect(url_for('blogController.get_blog', blog_id=request_blog.id)))


@blogController.route('/blog/<int:blog_id>/delete', methods=['GET', 'POST'])
@get_user_token
@check_ownership
def delete_blog(is_logged, is_owner, request_blog, blog_id):
    """The route to delete the blog if the user owns the blog"""

    if not is_owner:
        abort(401)

    if request.method == 'GET':
        return render_template('delete_blog.html', categories=categories.get_all(),
                               blog_id=blog_id, is_logged=is_logged)
    else:
        blogs.delete(request_blog)
        return make_response(redirect(url_for('blogController.get_blogs')))
