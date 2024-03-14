import justpy as jp
import definition
import requests
from webapp import layout
from webapp import page

class Dictionary(page.Page):
    path = "/dictionary"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)
        lay = layout.DefaultLayout(a=wp)

        container = jp.QPageContainer(a=lay)
        
        main = jp.Div(a=container, classes="bg-gray-200 h-screen")

        jp.Div(a=main, text="Instant English Dictionary", classes="text-4xl m-2")
        jp.Div(a=main, text="Get the definition of any English word instantly as you type.", classes="text-lg")


        input_div = jp.Div(a=main, classes="grid grid-cols-2")

        output_div = jp.Div(a=main, classes="m-2 p-2 text-lg border-2 border-gray-400 h-40")

        input_box = jp.Input(a=input_div, placeholder="Type in the word here...",
                 classes="m-2 rounded w-64 focus:bg-white focus:outline-none focus:border-purple-500 " 
                 "py-2 px-4", outputdiv=output_div)
        input_box.on('input', cls.get_definition)

        return wp
    

    # Use static method because class method recquires class
    #and without anything program requires self (current instance of class)
    #static methds do not need self because it its functions arent specific to
    #the current instance

    #So static methods are JUST for organization purposes it should actually just
    # belong in the method above
    @staticmethod
    def get_definition(widget, msg):
        request = requests.get(f"http://127.0.0.1:8000/api?w={widget.value}")
        data = request.json()

        # defined = definition.Definition(widget.value).get()
        widget.outputdiv.text = " ".join(data['definition'])