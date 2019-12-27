import frappe


def after_install():
    _set_website_settings()
    _set_system_settings()
    _set_currency()
    _set_stock_settings()
    _set_global_defaults()


def _set_website_settings():
    website_settings = frappe.get_single('Website Settings')
    website_settings.home_page = 'login'
    website_settings.copyright = '9T9 Information Technology'
    website_settings.hide_footer_signup = True
    website_settings.disable_signup = True
    website_settings.top_bar_items = []
    website_settings.save()


def _set_system_settings():
    system_settings = frappe.get_single('System Settings')
    system_settings.enable_chat = False
    system_settings.use_socketio_to_upload_file = False
    system_settings.save()


def _set_currency():
    bhd_currency = frappe.get_doc('Currency', 'BHD')
    bhd_currency.enabled = True
    bhd_currency.symbol = 'BD.'
    bhd_currency.smallest_currency_fraction_value = 0.001
    bhd_currency.save()


def _set_stock_settings():
    stock_settings = frappe.get_single('Stock Settings')
    stock_settings.item_naming_by = 'Naming Series'
    stock_settings.valuation_method = 'Moving Average'
    stock_settings.save()


def _set_global_defaults():
    global_defaults = frappe.get_single('Global Defaults')
    global_defaults.disable_rounded_total = True
    global_defaults.default_currency = 'BHD'
