app_name = "nacional_suite"
app_title = "Suite"
app_publisher = "Nacional Carnes"
app_description = "Customizações Nacional Suite para Frappe/ERPNext/HRMS"
app_email = "ti@nacionalcarnes.com.br"
app_license = "MIT"

app_logo_url = "/assets/nacional_suite/images/suite-logo.png"

app_include_css = [
    "/assets/nacional_suite/css/nacional_suite.css",
    "/assets/nacional_suite/css/nacional_suite_ai.css"
]
app_include_js = [
    "/assets/nacional_suite/js/nacional_suite.js",
    "/assets/nacional_suite/js/nacional_suite_ai.js"
]

after_install = "nacional_suite.install.after_install"
after_migrate = "nacional_suite.install.apply_branding"
