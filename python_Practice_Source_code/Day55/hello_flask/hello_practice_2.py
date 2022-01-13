from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World!"


# --------------- 高级装饰器函数 ---------------
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(function):
    # 传入可变参数： *name 表示传入数组，**name 表示传入字典
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function()

    return wrapper


def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


new_user = User("Dong")
create_blog_post(new_user)

if __name__ == "__main__":
    app.run(debug=True)
