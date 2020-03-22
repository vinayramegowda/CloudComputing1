#!/usr/bin/env python

# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START imports]
import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
# [END imports]

DEFAULT_USER_NAME = 'admin'


# We set a parent key on the 'Greetings' to ensure that they are all
# in the same entity group. Queries across the single entity group
# will be consistent. However, the write rate should be limited to
# ~1/second.

def login_key(login_ID=DEFAULT_USER_NAME):

    return ndb.Key('Login', login_ID)


class User(ndb.Model):
    """A main model for representing an individual Guestbook entry."""
    #userID = ndb.StringProperty(indexed=True)
    password=ndb.StringProperty(indexed=False)
    name = ndb.StringProperty(indexed=False)

# [END greeting]


# [START main_page]
class MainPage(webapp2.RequestHandler):
    def get(self):
        #login_ID = self.request.get('login_ID',
                                        #  DEFAULT_USER_NAME)

        #login_query = user_information(parent=login_key(login_ID))

        #user = users.get_current_user()
        #if user:
            #url = users.create_logout_url(self.request.uri)
            #url_linktext = 'Logout'
        #else:
            #url = users.create_login_url(self.request.uri)
            #url_linktext = 'Login'
        User(password='qwerty',name='Vinay').put()
        template_values = {
            'userer': User
        }

        template = JINJA_ENVIRONMENT.get_template('login.html')
        self.response.write(template.render(template_values))
# [END main_page]


# [START guestbook]
class Login(webapp2.RequestHandler):

    def post(self):
        # We set the same parent key on the 'Greeting' to ensure each
        # Greeting is in the same entity group. Queries across the
        # single entity group will be consistent. However, the write
        # rate to a single entity group should be limited to
        # ~1/second.
        login_ID = self.request.get('login_ID',
                                         DEFAULT_USER_NAME)
        user = User(parent=login_key(login_ID))

        # if users.get_current_user():
        #     greeting.author = Author(
        #             identity=users.get_current_user().user_id(),
        #             #country=users.get_current_user().country(),
        #             email=users.get_current_user().email())
        # greeting.country=self.request.get('country')
        # greeting.content = self.request.get('content')
        # greeting.put()
        #
         #query_params = {'guestbook_name': guestbook_name}
        # self.redirect('/?' + urllib.urlencode(query_params))
# [END guestbook]


# [START app]
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign', Login),
], debug=True)
# [END app]
