import justpy as jp

class DefaultLayout(jp.QLayout):
        
        def __init__(self, view="hHh lpR fFf", **kwargs):
            super().__init__(view=view, **kwargs)

            header = jp.QHeader(a=self)
            toolbar = jp.QToolbar(a=header)

            drawer = jp.QDrawer(a=self, show_if_above=True, v_model="left", bordered=True)

            scroller = jp.QScrollArea(a=drawer, classes="fit")
            qList = jp.QList(a=scroller)
            a_classes = "p-2 m-2 text-lg text-blue-400 hover:text-blue-700"
            jp.A(a=qList, text="Home", href="/home", classes=a_classes)
            jp.Br(a=qList)
            jp.A(a=qList, text="Dictionary", href="/dictionary", classes=a_classes)
            jp.Br(a=qList)
            jp.A(a=qList, text="About", href="/about", classes=a_classes)
            jp.Br(a=qList)

            jp.QBtn(a=toolbar, dense=True, flat=True, round=True, icon="menu", click=self.move_drawer, drawer=drawer)
            jp.QToolbarTitle(a=toolbar, text="Instant Dictionary")

        @staticmethod
        def move_drawer(widget, msg):
            widget.drawer.value = not widget.drawer.value