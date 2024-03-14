import justpy as jp
#Tailwind CSS

@jp.SetRoute("/p")
def home():
    wp = jp.QuasarPage(tailwind=True)
    main = jp.Div(a=wp, classes="bg-gray-200 h-screen")
    top = jp.Div(a=main, classes="grid grid-cols-3 gap-4 p-4")
    
    in_1 = jp.Input(a=top, placeholder="Enter First Value", classes="form-input")
    in_2 = jp.Input(a=top, placeholder="Enter Second Value", classes="form-input")

    d = jp.Div(a=top, text="Result Goes Here", classes="text-gray-600")

    jp.Div(a=top, text="Just Another Div", classes="text-gray-600")
    jp.Div(a=top, text="Yet Another Div", classes="text-gray-600")
    
    bot = jp.Div(a=main, classes="grid grid-cols-2 gap-4")
    jp.Button(a=bot, text="Calculate", classes="border border-blue-500 m-2 px-4 py-1 rounded hover:bg-red-500 hover:text-white", click=sum_up, in1=in_1, in2=in_2, d_output=d)
    jp.Div(a=bot, text="Just Another Div", classes="text-gray-600 hover:bg-red-500 hover:text-white", mouseenter=mouse_enter, mouseleave=mouse_leave)
    return wp

def sum_up(widget, msg):
    sum = float(widget.in1.value)+float(widget.in2.value)
    widget.d_output.text = sum

def mouse_enter(widget, msg):
    widget.text = "MOUSE IS IN HEEERE"

def mouse_leave(widget,msg):
    widget.text = "Whew, mouse isnt inside"



if __name__ == "__main__":
    # jp.Route("/", home)
    jp.justpy()