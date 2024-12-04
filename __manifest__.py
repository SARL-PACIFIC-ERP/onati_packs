{
    "name": "Packs ONATi",
    "version": "17.0.1.0.0",
    "category": "Sales",
    "summary": "Customization of product pack and sale product pack to match ONATi specific needs",
    "website": "https://www.pacific-erp.com",
    "author": "Pacific ERP",
    "license": "AGPL-3",
    "depends": ["sale_product_pack","pe_custom_report"],
    "installable": True,
    "data": [
        "views/product_pack_line_views.xml",
        "views/product_template_views.xml",
        'report/custom_sales.xml',
        'report/custom_invoice.xml',
        'views/account_move_views.xml',
    ]
}
