from .utils import set_readonly_property_setter, set_hidden_property_setter


def execute():
    print('Applying Purchase Invoice defaults...')
    set_readonly_property_setter('Purchase Invoice', 'naming_series')
    set_hidden_property_setter('Purchase Invoice', 'apply_tds')
    set_hidden_property_setter('Purchase Invoice', 'raw_materials_supplied')
    set_hidden_property_setter('Purchase Invoice', 'supplied_items')
    set_hidden_property_setter('Purchase Invoice', 'shipping_rule')
    _set_printing_settings()


def _set_printing_settings():
    print('Hiding Printing Settings')
    fields = [
        'printing_settings',
        'letter_head',
        'group_same_items',
        'column_break_112',
        'select_print_heading',
        'language'
    ]
    for field in fields:
        set_hidden_property_setter('Purchase Invoice', field)
