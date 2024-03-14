from webapp import page
import justpy as jp

class Sales(page.Page):

    @classmethod
    def serve(cls, req):

        wp = jp.QuasarPage(tailwind=True)

        header = jp.Div(a=wp, classes="flex justify-around w-screen py-3")
        logo = jp.Div(a=header, classes="flex content-center mx-7")
        jp.H3(a=logo, text="Indian", classes="font-serif py-4 text-xl inline text-yellow-500")
        jp.H3(a=logo, text="Market", classes="font-serif py-4 text-xl inline text-green-600")

        input_box = jp.Input(a=header, placeholder="Type in item you want to look for",
                 classes="m-2 rounded-xl w-3/5 border border-transparent shadow-md focus:outline-none focus:ring-2 focus:ring-blue-600 focus:border-transparent py-2 px-4")
        
        jp.A(a=header, text="View Shopping Cart", classes="mx-7 py-4 hover:text-blue-600 hover:underline")

        #Items
        items = jp.Div(a=wp, classes="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 bg-gray-100")

        for i in range(10):
            wrap = jp.Div(a=items, classes="justify-self-center m-7 px-12 py-6 bg-white")
            jp.P(a=wrap, text="Tomatoes")
            jp.P(a=wrap, text="Add ^ ___ v")
        
        return wp