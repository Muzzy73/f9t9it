# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "f9t9it"
app_title = "F9T9IT"
app_publisher = "9T9IT"
app_description = "9T9IT Setup App for ERPNext"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@9t9it.com"
app_license = "MIT"

after_install = "f9t9it.setup.install.after_install"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/f9t9it/css/f9t9it.css"
# app_include_js = "/assets/f9t9it/js/f9t9it.js"

# include js, css files in header of web template
# web_include_css = "/assets/f9t9it/css/f9t9it.css"
# web_include_js = "/assets/f9t9it/js/f9t9it.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "f9t9it.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "f9t9it.install.before_install"
# after_install = "f9t9it.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "f9t9it.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"f9t9it.tasks.all"
# 	],
# 	"daily": [
# 		"f9t9it.tasks.daily"
# 	],
# 	"hourly": [
# 		"f9t9it.tasks.hourly"
# 	],
# 	"weekly": [
# 		"f9t9it.tasks.weekly"
# 	]
# 	"monthly": [
# 		"f9t9it.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "f9t9it.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "f9t9it.event.get_events"
# }

