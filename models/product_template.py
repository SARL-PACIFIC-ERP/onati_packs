# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models

class ProductTemplate(models.Model):
    _inherit = "product.template"

    pack_component_price = fields.Selection(selection_add=[("onati", "ONATi")])

    @api.onchange('pack_component_price')
    def _onchange_pack_component_price(self):
        if self.pack_component_price == "onati":
            self.list_price = 0
    