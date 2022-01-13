from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1 style='text-align:center'>Hello World</h1>" \
           "<p>This is a paragraph</p>" \
           "<img src='https://giphy.com/embed/K1wjOn6HImv7y'>"


@app.route("/bye")
def bye():
    return "Bye bye!"


# URL 传值
@app.route("/username/<name>")
def greet(name):
    return f"Hello there {name + '12'}"


# URL 传多个值
@app.route("/somevalue/<name>/<int:number>")
def print_multi_value(name, number):
    return f"Hello {name}, You are {number} years old."


# 子路由全部传入
@app.route("/path/<path:sub_path>")
def print_sub_path(sub_path):
    return f"Sub_path is : {sub_path}"


# ----------------- demo -----------------
# 使用 @decorator 的方式来生成 html 格式

def make_bold(function):  # 加粗
    def wrapper_function():
        return f"<b>{function()}</b>"

    return wrapper_function


def make_emphasis(function):  # 强调
    def wrapper_function():
        return f"<em>{function()}</em>"

    return wrapper_function


def make_underlined(function):  # 下划线
    def wrapper_function():
        return f"<ul>{function()}</ul>"

    return wrapper_function


@app.route("/html")
@make_bold
@make_emphasis
@make_underlined
def make_html():
    return f"niubi!"


if __name__ == "__main__":
    app.run(debug=True)  # 打开 debug 模式
