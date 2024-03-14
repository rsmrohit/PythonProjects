import justpy as jp
from webapp import layout
from webapp import page

class Home(page.Page):
    path = "/home"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)
        
        lay = layout.DefaultLayout(a=wp)

        container = jp.QPageContainer(a=lay)
        
        main = jp.Div(a=container, classes="bg-gray-200 h-screen")

        jp.Div(a=main, text="This is a Home Page", classes="text-4xl m-2")
        jp.Div(a=main, text="""
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Vitae elementum curabitur vitae nunc sed velit dignissim. Leo integer malesuada nunc vel risus. Fermentum dui faucibus in ornare quam viverra orci sagittis eu. Vestibulum lectus mauris ultrices eros. Eu sem integer vitae justo eget magna fermentum iaculis eu. Justo donec enim diam vulputate ut pharetra sit. Lacus viverra vitae congue eu consequat ac felis. Velit scelerisque in dictum non consectetur a erat. Turpis egestas maecenas pharetra convallis posuere.

        """, classes="text-lg")
        return wp