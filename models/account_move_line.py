# -*- coding: utf-8 -*-

from odoo import fields, models

class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    pack_type = fields.Selection(related='product_id.pack_type')
    pack_component_price = fields.Selection(related='product_id.pack_component_price')
