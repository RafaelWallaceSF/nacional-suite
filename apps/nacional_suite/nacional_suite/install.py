import frappe

APP_LOGO = "/assets/nacional_suite/images/suite-logo.png"
APP_NAME = "Nacional Suite"


def after_install():
    apply_branding()


def apply_branding():
    """Aplica branding básico sem alterar o core do Frappe/HRMS."""
    try:
        frappe.db.set_single_value("Navbar Settings", "app_logo", APP_LOGO)
    except Exception:
        frappe.log_error(frappe.get_traceback(), "Nacional Suite branding: Navbar Settings")

    for doctype, field in [
        ("Website Settings", "app_name"),
        ("System Settings", "app_name"),
    ]:
        try:
            frappe.db.set_single_value(doctype, field, APP_NAME)
        except Exception:
            # Campo pode não existir dependendo da versão do Frappe.
            pass

    frappe.db.commit()
