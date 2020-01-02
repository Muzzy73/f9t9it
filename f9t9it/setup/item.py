from .utils import set_hidden_property_setter, set_readonly_property_setter


def execute():
    print('Applying Item defaults...')
    set_readonly_property_setter('Item', 'naming_series')
    set_hidden_property_setter('Item', 'allow_alternative_item')
    set_hidden_property_setter('Item', 'is_fixed_asset')
    set_hidden_property_setter('Item', 'is_item_from_hub')
    _set_variants()
    _set_foreign_trade_details()
    _set_sales_purchase_accounting_defaults()
    _set_deferred_expense()
    _set_deferred_revenue()
    _set_customer_details()
    _set_inspection_criteria()
    _set_website()
    _set_hub_publishing_details()
    _set_serial_nos_and_batches()
    _set_inventory()


def _set_variants():
    print('Hiding Variants')
    fields = [
        'variants_section',
        'has_variants',
        'variant_based_on',
        'attributes'
    ]
    for field in fields:
        set_hidden_property_setter('Item', field)


def _set_sales_purchase_accounting_defaults():
    print('Hiding Sales Purchase Accounting Defaults')
    fields = [
        'defaults',
        'item_defaults'
    ]
    for field in fields:
        set_hidden_property_setter('Item', field)


def _set_foreign_trade_details():
    print('Hiding Foreign Trade Details')
    fields = [
        'foreign_trade_details',
        'country_of_origin',
        'column_break_59',
        'customs_tariff_number'
    ]
    for field in fields:
        set_hidden_property_setter('Item', field)


def _set_deferred_revenue():
    print('Hiding Deferred Revenue')
    fields = [
        'deferred_revenue',
        'deferred_revenue_account',
        'enable_deferred_revenue',
        'column_break_85',
        'no_of_months'
    ]
    for field in fields:
        set_hidden_property_setter('Item', field)


def _set_deferred_expense():
    print('Hiding Deferred Expense')
    fields = [
        'deferred_expense_section',
        'deferred_expense_account',
        'column_break_88',
        'no_of_months_exp'
    ]
    for field in fields:
        set_hidden_property_setter('Item', field)


def _set_customer_details():
    print('Hiding Customer Details')
    fields = [
        'customer_details',
        'customer_items'
    ]
    for field in fields:
        set_hidden_property_setter('Item', field)


def _set_inspection_criteria():
    print('Hiding Inspection Criteria')
    fields = [
        'inspection_criteria',
        'inspection_required_before_purchase',
        'inspection_required_before_delivery',
        'quality_inspection_template'
    ]
    for field in fields:
        set_hidden_property_setter('Item', field)


def _set_website():
    print('Hiding Website')
    fields = [
        'website_section',
        'show_in_website',
        'show_variant_in_website',
        'route',
        'weightage',
        'slideshow',
        'website_image',
        'thumbnail',
        'cb72',
        'website_warehouse',
        'website_item_groups'
    ]
    for field in fields:
        set_hidden_property_setter('Item', field)


def _set_hub_publishing_details():
    print('Hiding Hub Publishing Details')
    fields = [
        'hub_publishing_sb',
        'publish_in_hub',
        'hub_category_to_publish',
        'hub_warehouse',
        'synced_with_hub'
    ]
    for field in fields:
        set_hidden_property_setter('Item', field)


def _set_serial_nos_and_batches():
    print('Hiding Serial Nos and Batches')
    fields = [
        'serial_nos_and_batches',
        'has_batch_no',
        'create_new_batch',
        'batch_number_series',
        'has_expiry_date',
        'retain_sample',
        'sample_quantity',
        'column_break_37',
        'has_serial_no',
        'serial_no_series'
    ]
    for field in fields:
        set_hidden_property_setter('Item', field)


def _set_inventory():
    print('Hiding Inventory')
    fields = [
        'inventory_section',
        'shelf_life_in_days',
        'end_of_life',
        'default_material_request_type',
        'valuation_method',
        'column_break1',
        'warranty_period',
        'weight_per_unit',
        'weight_uom'
    ]
    for field in fields:
        set_hidden_property_setter('Item', field)
