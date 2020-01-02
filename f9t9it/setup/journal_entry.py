from .utils import set_hidden_property_setter, set_readonly_property_setter


def execute():
    print('Applying Journal Entry defaults...')
    set_readonly_property_setter('Journal Entry', 'naming_series')
    set_hidden_property_setter('Journal Entry', 'finance_book')
    _set_printing_settings()
    _set_more_information()


def _set_printing_settings():
    print('Hiding Printing Settings')
    fields = [
        'printing_settings',
        'pay_to_recd_from',
        'column_break_35',
        'letter_head',
        'select_print_heading'
    ]
    for field in fields:
        set_hidden_property_setter('Journal Entry', field)


def _set_more_information():
    print('Hiding More Information')
    fields = [
        'additional_info',
        'mode_of_payment',
        'payment_order',
        'column_break3',
        'is_opening',
        'stock_entry'
    ]
    for field in fields:
        set_hidden_property_setter('Journal Entry', field)
