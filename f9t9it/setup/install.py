import frappe


def after_install():
    _set_website_settings()
    _set_naming_series()
    _set_system_settings()
    _set_currency()
    _set_stock_settings()
    _set_global_defaults()


def _set_website_settings():
    print('Setting up Website Settings...')
    website_settings = frappe.get_single('Website Settings')
    website_settings.home_page = 'login'
    website_settings.copyright = '9T9 Information Technology'
    website_settings.hide_footer_signup = True
    website_settings.disable_signup = True
    website_settings.top_bar_items = []
    website_settings.save()


def _set_naming_series():
    print('Setting up Naming Series...')
    naming_series = [
        ('Item', 'I.######'),
        ('Employee', 'EP-'),
        ('Journal Entry', 'JV.YY.-.######'),
        ('Landed Cost Voucher', 'LV.YY.-.######'),
        ('Payment Entry', 'PE.YY.-.######'),
        ('Purchase Invoice', 'PI.YY.-.######'),
        ('Purchase Order', 'PO.YY.-.######'),
        ('Purchase Receipt', 'PR.YY.-.######'),
        ('Quotation', 'QT.YY.-.######'),
        ('Sales Order', 'SO.YY.-.######'),
        ('Stock Entry', 'SE.YY.-.######'),
        ('Sales Invoice', 'SI.YY.-.######'),
        ('Material Request', 'MR-.YY.-.######')
    ]

    for single_naming_series in naming_series:
        doctype, series = single_naming_series
        naming_series_doc = frappe.get_single('Naming Series')
        naming_series_doc.select_doc_for_series = doctype
        naming_series_doc.set_options = series
        naming_series_doc.update_series()


def _set_system_settings():
    print('Setting up System Settings...')
    system_settings = frappe.get_single('System Settings')
    system_settings.enable_chat = False
    system_settings.use_socketio_to_upload_file = False
    system_settings.currency_precision = 3
    system_settings.save()


def _set_currency():
    print('Setting up Currency...')
    bhd_currency = frappe.get_doc('Currency', 'BHD')
    bhd_currency.enabled = True
    bhd_currency.symbol = 'BD.'
    bhd_currency.smallest_currency_fraction_value = 0.001
    bhd_currency.save()


def _set_stock_settings():
    print('Setting up Stock Settings...')
    stock_settings = frappe.get_single('Stock Settings')
    stock_settings.item_naming_by = 'Naming Series'
    stock_settings.valuation_method = 'Moving Average'
    stock_settings.save()


def _set_global_defaults():
    print('Setting up Global Defaults...')
    global_defaults = frappe.get_single('Global Defaults')
    global_defaults.disable_rounded_total = True
    global_defaults.default_currency = 'BHD'
    global_defaults.save()
