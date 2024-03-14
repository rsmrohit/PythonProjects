import justpy as jp

class About:
    path = "/about"

    def serve(self):
        wp = jp.WebPage()
        main = jp.Div(a=wp, classes="bg-gray-200 h-screen")

        jp.Div(a=main, text="Instant Dictionary API", classes="text-4xl m-2")
        jp.Div(a=main, text="""
                Get definition of views:
        """, classes="text-lg")
        jp.Hr(a=main)
        jp.Div(a=main, text="www.example.com/api?w=moon")
        jp.Hr(a=main)
        jp.Div(a=main, text="""
            {
               "word": "moon",
                "definition": ["A natural satellite of a planet.", "A month, particularly a lunar month (approximately 28 days).", "To fuss over adoringly or with great affection.", "Deliberately show ones bare ass (usually to an audience, or at a place, where this is not expected or deemed appropriate).", "To be lost in phantasies or be carried away by some internal vision, having temorarily lost (part of) contact to reality."]
            }
        """)
        return wp