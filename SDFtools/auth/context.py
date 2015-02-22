__author__ = 'kwhatcher'


__author__ = 'kwhatcher'


"""Provide support for generating auth info for use in templates

"""


from werkzeug.local import LocalProxy
import vars


class Auth(object):

    def __init__(self, app):
        if app is not None:
            self.init_app(app)

    def init_app(self, app, *args, **kwargs):
        app.context_processor(Auth.auth_context_processor)

        self.app = app
        if not hasattr(app, 'extensions'):
            app.extensions = {}




    @staticmethod
    def auth():
        """Backend function for auth proxy

        :return: A list of auth items
        """
        auth_list = {'uri':vars.redirect_uri[0]}

        return auth_list

    @staticmethod
    def auth_context_processor():
        """add variable ''auth'' to template context

        It contains the list of weather entries to render as a widget
        """

        return dict(auth_list=auth_list)





#: A proxy for current weather list.
auth_list = LocalProxy(Auth.auth)