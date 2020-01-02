from .utils import set_hidden_property_setter, set_readonly_property_setter


def execute():
    print('Applying Supplier defaults...')
    set_hidden_property_setter('Supplier', 'default_bank_account')
    set_hidden_property_setter('Supplier', 'pan')
    set_hidden_property_setter('Supplier', 'tax_withholding_category')
    _set_currency_and_price_list()
    _set_default_payable_accounts()
    _set_more_information()
    set_hidden_property_setter('Supplier', 'warn_rfqs')
    set_hidden_property_setter('Supplier', 'warn_pos')
    set_hidden_property_setter('Supplier', 'prevent_rfqs')
    set_hidden_property_setter('Supplier', 'prevent_pos')


def _set_currency_and_price_list():
    print('Hiding Currency and Price List')
    fields = [
        'section_break_7',
        'default_currency',
        'column_break_10',
        'default_price_list'
    ]
    for field in fields:
        set_hidden_property_setter('Supplier', field)


def _set_default_payable_accounts():
    print('Hiding Default Payable Accounts')
    fields = [
        'default_payable_accounts',
        'accounts'
    ]
    for field in fields:
        set_hidden_property_setter('Supplier', field)


def _set_more_information():
    print('Hiding More Information')
    fields = [
        'column_break2',
        'website',
        'supplier_details'
    ]
    for field in fields:
        set_hidden_property_setter('Supplier', field)
