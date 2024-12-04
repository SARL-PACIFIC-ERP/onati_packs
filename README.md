# Packs ONATi

Customization of OCA pack modules `product_pack` and `sale_product_pack`, to match some specific needs.

Features :

- Sale Order : Add percentage discount from pricelist to sale.order.line even if price is zero
- Sale Order : Reflect percentage discount of pack parent line on pack child lines 
- Product Pack : Add a new "Pack Component Price" option named `onati` for detailed packs which unlocks :
  - Product Pack : Price is readonly and set to zero
  - Product Pack Line : Add a "Sale price" fields replacing the product's sale unit price
  - Sale Order : Pricelist does not apply to pack child lines, price from Pack Line "Sale price" field is used instead
  - Sale Order & Account Move : Price fields are not displayed anymore for pack parent line, on views and reports
- Product Pack Line : Does not display the "Discount" field anymore