"""A HomeController Module."""

from masonite.request import Request
from masonite.response import Response
from masonite.view import View

class HomeController:
    """HomeController Controller Class."""

    def show(self, view: View, request: Request, response: Response):
        return view.render('home', {
            'name': request.param('name') or request.input('name'),
        })
