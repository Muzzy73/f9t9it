import frappe


def set_hidden_property_setter(doctype, fieldname):
    frappe.make_property_setter({
        'doctype': doctype,
        'fieldname': fieldname,
        'property': 'hidden',
        'value': '1'
    })


def set_readonly_property_setter(doctype, fieldname):
    frappe.make_property_setter({
        'doctype': doctype,
        'fieldname': fieldname,
        'property': 'read_only',
        'value': '1'
    })
