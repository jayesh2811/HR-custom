app_name = "hr_customization"
app_title = "HR Customization"
app_publisher = "jayesh"
app_description = "Custom HR App"
app_email = "jayesh.patil@techonsy.com"
app_license = "mit"


required_apps = []

add_to_apps_screen = [
	{
		"name": "hr_customization",
		"logo": "/assets/hr_customization/logo.png",
		"title": "HR Customization",
		"route": "/hr_customization",
		"has_permission": "hr_customization.api.permission.has_app_permission"
	}
]


app_include_css = "/assets/hr_customization/css/hr_customization.css"
app_include_js = "/assets/hr_customization/js/hr_customization.js"

web_include_css = "/assets/hr_customization/css/hr_customization.css"
web_include_js = "/assets/hr_customization/js/hr_customization.js"

website_theme_scss = "hr_customization/public/scss/website"


webform_include_js = {"doctype": "public/js/doctype.js"}
webform_include_css = {"doctype": "public/css/doctype.css"}


page_js = {"page" : "public/js/file.js"}


doctype_js = {"doctype" : "public/js/doctype.js"}
doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}



app_include_icons = "hr_customization/public/icons.svg"



home_page = "login"

role_home_page = {
	"Role": "home_page"
}


website_generators = ["Web Page"]

jinja = {
	"methods": "hr_customization.utils.jinja_methods",
	"filters": "hr_customization.utils.jinja_filters"
}



before_install = "hr_customization.install.before_install"
after_install = "hr_customization.install.after_install"



before_uninstall = "hr_customization.uninstall.before_uninstall"
after_uninstall = "hr_customization.uninstall.after_uninstall"


before_app_install = "hr_customization.utils.before_app_install"
after_app_install = "hr_customization.utils.after_app_install"


before_app_uninstall = "hr_customization.utils.before_app_uninstall"
after_app_uninstall = "hr_customization.utils.after_app_uninstall"


notification_config = "hr_customization.notifications.get_notification_config"



permission_query_conditions = {
	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
}

has_permission = {
	"Event": "frappe.desk.doctype.event.event.has_permission",
}


override_doctype_class = {
	"ToDo": "custom_app.overrides.CustomToDo"
}


doc_events = {
	"*": {
		"on_update": "method",
		"on_cancel": "method",
		"on_trash": "method"
	}
}



scheduler_events = {
	"all": [
		"hr_customization.tasks.all"
	],
	"daily": [
		"hr_customization.tasks.daily"
	],
	"hourly": [
		"hr_customization.tasks.hourly"
	],
	"weekly": [
		"hr_customization.tasks.weekly"
	],
	"monthly": [
		"hr_customization.tasks.monthly"
	],
}



before_tests = "hr_customization.install.before_tests"


override_whitelisted_methods = {
	"frappe.desk.doctype.event.event.get_events": "hr_customization.event.get_events"
}


override_doctype_dashboards = {
	"Task": "hr_customization.task.get_dashboard_data"
}


auto_cancel_exempted_doctypes = ["Auto Repeat"]



ignore_links_on_delete = ["Communication", "ToDo"]


before_request = ["hr_customization.utils.before_request"]
after_request = ["hr_customization.utils.after_request"]


before_job = ["hr_customization.utils.before_job"]
after_job = ["hr_customization.utils.after_job"]

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]



auth_hooks = [
	"hr_customization.auth.validate"
]

export_python_type_annotations = True

default_log_clearing_doctypes = {
	"Logging DocType Name": 30  # days to retain logs
}

