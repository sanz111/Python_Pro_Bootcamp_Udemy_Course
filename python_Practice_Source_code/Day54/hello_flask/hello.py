from flask import Flask

app = Flask(__name__)  # __name__ 可以知道当前运行的程序名。比如此处 __name__ 打印出来值为 __main__

@app.route("/")
def hello_world():
    return "cao,niubi!"

@app.route("/bye")
def say_bye():
    return "Bye bye!"

# 以上便构建了一个最简单的 flask 应用
# 启动方法：
# 在命令行中导出： export FLASK_APP=hello
# 再在命令行中运行：flask run
# 运行后便成功启动了
# 按 ctrl + c 退出当前运行的服务器

if __name__ == "__main__":
    app.run()