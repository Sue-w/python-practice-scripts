from flask import Flask, render_template, request


app = Flask(__name__)

# Create some test data - a blog post

posts = {
    0: {
        'id': 'post_id',
        'title': 'Hello, world',
        'content': 'This is my first blog post'
    }
}


# assigning a route to the home page

@app.route('/')
def home():
    return 'Hello, world!'

# assigning a route to the /post/0 page
# the int post id will be replace with the post id in this example post id is 0


# @app.route('/post/<int:post_id>')
# def post(post_id):
#     post = posts.get(post_id)
#     return f" Post: {post['title']}, content: \n\n {post['content']} "

# To render a static html template

# @app.route('/post/<int:post_id>')
# def post(post_id):
#     post = posts.get(post_id)
#     return render_template('post.jinja2')


# to render the html template with dynamic variables that are defined in this app but are used in the HTML template

# @app.route('/post/<int:post_id>')
# def post(post_id):
#     post = posts.get(post_id)
#     return render_template('post.jinja2', post=post)

# the first post in the last bit of code is the post used in the HTML template and the second post is the post defined
# above in the function definition


# a simpler way to do this

# @app.route('/post/<int:post_id>')
# def post(post_id):
#     return render_template('post.jinja2', post=posts.get(post_id))

# add an error message if the post integer entered was 1 or 2 , anything but 0:

@app.route('/post/<int:post_id>')
def post(post_id):
    blog_post = posts.get(post_id)
    if not blog_post:
        return render_template('404.jinja2', message=f'A post with id {post_id} was not found')
    return render_template('post.jinja2', post=blog_post)


# Creating Forms
# create is the file that contains the fields that the user can fill to post a post.

@app.route('/post/form')
def form():
    return render_template('create.jinja2')

# When the form is submitted there's is nowhere to recieve and store or use the data that has been submitted in the form

@app.route('/post/create')
def create():
    title = request.args.get('title')
    content = request.args.get('content')
    post_id = len(posts)
    posts[post_id] = {'id': post_id, 'title': title, 'content': content}

if __name__ == '__main__':
    app.run(debug=True)