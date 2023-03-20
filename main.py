import os
import webapp2

app = webapp2.WSGIApplication([
    ('/', 'static.HomePageHandler'),
    ('/about', 'static.AboutPageHandler'),
    ('/contact', 'static.ContactPageHandler'),
    ('/static/(.*)', 'static.StaticFileHandler'),
], debug=True)

config = {
    'webapp2_extras.jinja2': {
        'template_path': 'templates',
        'environment_args': {
            'extensions': [
                'jinja2.ext.autoescape',
                'jinja2.ext.with_',
            ]
        },
    },
}

class StaticFileHandler(webapp2.RequestHandler):
    def get(self, path):
        file_path = os.path.join(os.path.dirname(git@github.com:KrisCorriea/Portfolio-website.git), 'static', path)
        self.response.headers['Content-Type'] = self._get_content_type(path)
        with open(file_path, 'r') as f:
            self.response.write(f.read())

    def _get_content_type(self, path):
        ext = os.path.splitext(path)[1]
        if ext == '.css':
            return 'text/css'
        elif ext == '.js':
            return 'application/javascript'
        else:
            return 'text/plain'

class HomePageHandler(webapp2.RequestHandler):
    def get(self):
        template = webapp2_extras.jinja2.get_jinja2(app=self.app).render_template('index.html')
        self.response.write(template)

class AboutPageHandler(webapp2.RequestHandler):
    def get(self):
        template = webapp2_extras.jinja2.get_jinja2(app=self.app).render_template('about.html')
        self.response.write(template)

class ContactPageHandler(webapp2.RequestHandler):
    def get(self):
        template = webapp2_extras.jinja2.get_jinja2(app=self.app).render_template('contact.html')
        self.response.write(template)
