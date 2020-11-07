#!/usr/bin/python

import cgi, os
import cgitb
cgitb.enable()

print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<title>Hello World</title>'
print '</head>'
print '<body>'



form = cgi.FieldStorage()
if "name" not in form:
        displayName = "World"
else:
        displayName = form["name"].value


print '<h2>Hello ' + displayName + '!</h2>'


print '</body>'
print '</html>'
