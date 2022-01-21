import requests
from post import Post
from flask import Flask, render_template

posts = requests.get("https://api.npoint.io/fccc675bede2c8c54fe1").json()
print(posts)
post_objects = []
for post in posts:
    post_obj = Post(post['id'], post['title'],post['subtitle'], post['body'])
    post_objects.append(post_obj)

print(post_objects)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", all_posts = post_objects)

@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
