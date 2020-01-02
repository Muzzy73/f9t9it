from .utils import set_hidden_property_setter, set_readonly_property_setter


def execute():
    set_readonly_property_setter('Payment Entry', 'naming_series')
    set_readonly_property_setter('Payment Entry', 'party_name')
    set_readonly_property_setter('Payment Entry', 'paid_from')
    set_hidden_property_setter('Payment Entry', 'deductions_or_loss_section')
    set_hidden_property_setter('Payment Entry', 'deductions')
    _set_more_information()


def _set_more_information():
    print('Hiding More Information')
    fields = [
        'section_break_12',
        'project',
        'remarks',
        'column_break_16',
        'letter_head',
        'print_heading',
        'bank',
        'bank_account_no',
        'payment_order'
    ]
    for field in fields:
        set_hidden_property_setter('Payment Entry', field)
