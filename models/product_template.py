# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models

class ProductTemplate(models.Model):
    _inherit = "product.template"

    pack_component_price = fields.Selection(selection_add=[("onati", "ONATi")])

    list_price = fields.Float(compute="_compute_list_price", store=True)
    
    @api.depends('pack_ok','pack_type','pack_component_price', 'pack_line_ids')
    def _compute_list_price(self):
        """ List price computation - occurs only for ONATi packs
        """
        for record in self:
            if record.pack_ok and record.pack_type == 'detailed' and record.pack_component_price == 'onati':
                price = 0.0
                for line in record.pack_line_ids:
                    price += line.sale_price
                record.list_price = price


    