# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import api, fields, models

class ProductPack(models.Model):
    _inherit = "product.pack.line"

    sale_price = fields.Float(
        "Prix unitaire HT",
        digits="Product Price",
        help="Prix unitaire (hors taxes) du produit lorsqu'il fait partie de ce pack"
    )

    @api.onchange('product_id')
    def _onchange_product_id(self):
        self.sale_price = self.product_id.list_price