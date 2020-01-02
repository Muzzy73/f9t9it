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


def disable_doctype(doctype):
    """
    If Custom DocPerm is not setup (not transferred to cache), this will work.
    :param doctype: DocType to disable
    :return:
    """
    custom_docperm = frappe.get_doc({
        'doctype': 'Custom DocPerm',
        'parent': doctype,
        'parenttype': 'DocType',
        'parentfield': 'permissions',
        'role': 'System Manager',
        'permlevel': 0,
        'read': 0,
        'export': 0
    })
    custom_docperm.save()
