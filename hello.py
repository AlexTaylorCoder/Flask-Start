from flask import Flask
from random import choice
from random_route import RandomRoute

app = Flask(__name__)

#Decorators with params must have another outer function

def make_bold(function):
    print(function)
    def change_style():
        text = function()
        htmlText = f"<b> {text} </b>"
        return htmlText
    return change_style

def make_emphasis(function):
    def change_style():
        text = function()
        htmlText = f"<e> {text} </e>"
        return htmlText
    change_style.__name__ = function.__name__
    return change_style


def make_underlined(function):
    def change_style():
        text = function()
        htmlText = f'<u style = "font-size:22px"> {text} </u>'
        return htmlText
    return change_style

@app.route("/")
@make_bold
def home():
    return "Enter a random URL from 1-10!"

colors = ["red","blue","green","yellow","purple"]

#Generate all path as class instances
routes = []
for i in range(1,10):
    newRoute = RandomRoute(choice(colors),i)
    routes.append(newRoute)


#Match route to class instance
#If want to wrap with style decoration need to still pass path arg down through decoration make_bold, need to add additional wrapper and change underlying flask functionality
#Seems overly complicated and not correct architecture to construct websites, not worth figuring out, will learn proper method first (Guessing it's through inheritance)

@app.route("/<int:num>")
def get_instance_by_num(num):
    route_data = routes[num-1]
    return style_data(route_data)


def style_data(route_data):
    return f'<h1 style = color:{route_data.color}>{route_data.text}</h1><img src="https://i0.wp.com/images.onwardstate.com/uploads/2015/05/oie_14175751vZSQRLEn.gif?fit=650%2C408&ssl=1"/>'

#See if path matches randint

#Probably has to inherit from flask class


if __name__ == "__main__":
    app.run(debug=True)
