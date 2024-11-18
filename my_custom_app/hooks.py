app_name = "my_custom_app"
app_title = "My Custom App"
app_publisher = "Your Company"
app_description = "A custom Frappe application"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "your@email.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/my_custom_app/css/my_custom_app.css"
# app_include_js = "/assets/my_custom_app/js/my_custom_app.js"

# include js, css files in header of web template
# web_include_css = "/assets/my_custom_app/css/my_custom_app.css"
# web_include_js = "/assets/my_custom_app/js/my_custom_app.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "my_custom_app/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "my_custom_app.install.before_install"
# after_install = "my_custom_app.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "my_custom_app.uninstall.before_uninstall"
# after_uninstall = "my_custom_app.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# override_doctype_class = {
#     "User": "my_custom_app.overrides.CustomUser"
# }

# Document Events
# ---------------
# doc_events = {
#     "*": {
#         "on_update": "method",
#         "on_cancel": "method",
#         "on_trash": "method"
#     }
# }

# Scheduled Tasks
# ---------------
# scheduler_events = {
#     "all": [
#         "my_custom_app.tasks.all"
#     ],
#     "daily": [
#         "my_custom_app.tasks.daily"
#     ],
#     "hourly": [
#         "my_custom_app.tasks.hourly"
#     ],
#     "weekly": [
#         "my_custom_app.tasks.weekly"
#     ],
#     "monthly": [
#         "my_custom_app.tasks.monthly"
#     ]
# }

# Testing
# -------
# before_tests = "my_custom_app.install.before_tests"