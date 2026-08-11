app_name = "nacional_suite"
app_title = "Nacional Suite"
app_publisher = "Nacional Carnes"
app_description = "Customizações Nacional Suite para Frappe/ERPNext/HRMS"
app_email = "ti@nacionalcarnes.com.br"
app_license = "MIT"

app_logo_url = "/assets/nacional_suite/images/suite-logo.png"

add_to_apps_screen = [
    {
        "name": "nacional_suite",
        "logo": "/assets/nacional_suite/images/suite-logo.png",
        "title": "Nacional Suite",
        "route": "/app",
        "has_permission": "nacional_suite.permissions.has_app_permission",
        "sequence_id": 1,
    }
]

after_install = "nacional_suite.install.after_install"
after_migrate = "nacional_suite.install.apply_branding"
