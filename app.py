from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Function to save uploaded file
def save_file(file):
    if file:
        filename = file.filename
        file_path = os.path.join(app.root_path, 'static', 'img', filename)
        file.save(file_path)
        return filename
    return None

# Fake database for example (including comments)
posts = [
    {'title': 'Пост 1', 'content': 'Содержание первого поста', 'image': 'img/post1.jpg', 'comments': []},
    {'title': 'Пост 2', 'content': 'Содержание второго поста', 'image': 'img/post2.jpg', 'comments': []}
]

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html', posts=posts)

# Route for creating a post
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        image = save_file(request.files['photo'])
        posts.append({'title': title, 'content': content, 'image': 'img/' + image, 'comments': []})
        return redirect(url_for('index'))
    return render_template('create.html')

# Route for adding a comment
@app.route('/add_comment/<int:post_index>', methods=['POST'])
def add_comment(post_index):
    comment = request.form['comment']
    posts[post_index]['comments'].append(comment)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
