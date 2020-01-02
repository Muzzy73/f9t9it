from .utils import set_hidden_property_setter, set_readonly_property_setter


def execute():
    print('Applying Customer defaults...')
    set_hidden_property_setter('Customer', 'lead_name')
    set_hidden_property_setter('Customer', 'default_bank_account')
    _set_currency_and_price_list()
    _set_accounting()
    _set_more_information()
    _set_loyalty_points()


def _set_currency_and_price_list():
    print('Hiding Currency and Price List')
    fields = [
        'currency_and_price_list',
        'default_currency',
        'default_price_list',
        'column_break_14',
        'language'
    ]
    for field in fields:
        set_hidden_property_setter('Customer', field)


def _set_accounting():
    print('Hiding Accounting')
    fields = [
        'default_receivable_accounts',
        'accounts'
    ]
    for field in fields:
        set_hidden_property_setter('Customer', field)


def _set_more_information():
    print('Hiding More Information')
    fields = [
        'more_info',
        'customer_details',
        'column_break_45',
        'market_segment',
        'industry',
        'is_frozen'
    ]
    for field in fields:
        set_hidden_property_setter('Customer', field)


def _set_loyalty_points():
    print('Hiding Loyalty Points')
    fields = [
        'column_break_38',
        'loyalty_program',
        'loyalty_program_tier'
    ]
    for field in fields:
        set_hidden_property_setter('Customer', field)

