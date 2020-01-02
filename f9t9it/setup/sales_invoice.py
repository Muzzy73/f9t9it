import frappe
from .utils import set_hidden_property_setter


def execute():
    print('Applying Sales Invoice defaults...')
    fields = [
        {
            "field_name": "naming_series",
            "property": "read_only",
            "property_type": "Check",
            "value": "1"
        },
        {
            "field_name": "project",
            "property": "hidden",
            "property_type": "Link",
            "value": "1"
        },
        {
            "field_name": "loyalty_points_redemption",
            "property": "hidden",
            "property_type": "Section Break",
            "value": "1"
        },
        {
            "field_name": "loyalty_points",
            "property": "hidden",
            "property_type": "Int",
            "value": "1"
        },
        {
            "field_name": "loyalty_amount",
            "property": "hidden",
            "property_type": "Currency",
            "value": "1"
        },
        {
            "field_name": "redeem_loyalty_points",
            "property": "hidden",
            "property_type": "Check",
            "value": "1"
        },
        {
            "field_name": "column_break_77",
            "property": "hidden",
            "property_type": "Column Break",
            "value": "1"
        },
        {
            "field_name": "loyalty_program",
            "property": "hidden",
            "property_type": "Link",
            "value": "1"
        },
        {
            "field_name": "loyalty_redemption_account",
            "property": "hidden",
            "property_type": "Link",
            "value": "1"
        },
        {
            "field_name": "loyalty_redemption_cost_center",
            "property": "hidden",
            "property_type": "Link",
            "value": "1"
        },
        {
            "field_name": "time_sheet_list",
            "property": "hidden",
            "property_type": "Section Break",
            "value": "1"
        },
        {
            "field_name": "timesheets",
            "property": "hidden",
            "property_type": "Table",
            "value": "1"
        },
        {
            "field_name": "total_billing_amount",
            "property": "hidden",
            "property_type": "Currency",
            "value": "1"
        }
    ]

    for field in fields:
        frappe.make_property_setter({
            'doctype': 'Sales Invoice',
            'fieldname': field['field_name'],
            'property': field['property'],
            'value': field['value'],
            'property_type': field['property_type']
        })
        print('Created property setter for {}'.format(field['field_name']))

    _set_printing_settings()

    set_hidden_property_setter('Sales Invoice', 'total_net_weight')
    set_hidden_property_setter('Sales Invoice', 'shipping_rule')


def _set_printing_settings():
    print('Hiding printing settings...')
    fields = [
        'edit_printing_settings',
        'letter_head',
        'group_same_items',
        'language',
        'column_break_84',
        'select_print_heading'
    ]
    for field in fields:
        set_hidden_property_setter('Sales Invoice', field)
