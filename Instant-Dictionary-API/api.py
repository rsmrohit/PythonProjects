import justpy as jp
import definition
import json

class Api:
    """
    Handles Requests at /?w=[WORD]
    """

    @classmethod
    def serve(cls, req):
        wp = jp.WebPage()
        word = req.query_params.get('w')
        # jp.Div(a=wp, text=word.title())
        # We only want to return the word

        defined = definition.Definition(word).get()

        response = {
            "word":word,
            "definition": defined
        }

        wp.html = json.dumps(response)

        return wp

