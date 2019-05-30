from flask_appbuilder import IndexView

class LandingPageView(IndexView):
    index_template = 'index.html'