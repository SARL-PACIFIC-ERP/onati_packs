# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import _, api, models

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    def _get_pack_line_discount(self):
        """returns the discount settled in the parent pack lines"""
        self.ensure_one()
        discount = 0.0
        if self.pack_parent_line_id.pack_component_price == "detailed":
            discount += self.pack_parent_line_id.discount
            for pack_line in self.pack_parent_line_id.product_id.pack_line_ids:
                if pack_line.product_id == self.product_id:
                    discount += pack_line.sale_discount
                    break
        elif self.pack_parent_line_id.pack_component_price == 'onati':
            discount += self.pack_parent_line_id.discount
        return discount

    @api.depends("product_id", "product_uom", "product_uom_qty")
    def _compute_discount(self):
        res = super()._compute_discount()
        # Hack to get the % discount even if price is at 0
        for line in self:
            if not line.discount and line.pricelist_item_id and line.pricelist_item_id.compute_price == 'percentage':
                line.discount = line.pricelist_item_id.percent_price

        for pack_line in self.filtered("pack_parent_line_id"):
            pack_line.discount = pack_line._get_pack_line_discount()

        return res

    def write(self, vals):
        res = super().write(vals)
        # Apply pack discount to all pack lines
        if 'discount' in vals:
            for record in self:
                if record.product_id.pack_ok and record.pack_type == "detailed":
                    for pack_line in record.pack_child_line_ids:
                        pack_line.discount = pack_line._get_pack_line_discount()
        return res

    def _get_display_price(self):
        """ Overwrite for onati packs, retrieve pack.line.sale_price instead of computing it (no pricelist allowed)
        """
        pp = self.pack_parent_line_id.product_id or False
        if pp and pp.pack_ok and pp.pack_type == 'detailed' and pp.pack_component_price == 'onati':
            price = pp.pack_line_ids.filtered(lambda l: l.product_id == self.product_id).sale_price
        # Parent pack price should always be 0
        elif self.product_id.pack_ok and self.product_id.pack_type == 'detailed' and self.product_id.pack_component_price == 'onati':
            price = 0.0
        else:
            price = super()._get_display_price()
        return price