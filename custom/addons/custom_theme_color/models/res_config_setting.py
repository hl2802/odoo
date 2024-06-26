from odoo import models,api, fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    theme_color = fields.Char(string="Theme Color", default="#190b68e5")

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('custom_theme_color.theme_color', self.theme_color)

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res.update(
            theme_color=self.env['ir.config_parameter'].sudo().get_param('custom_theme_color.theme_color', default="#190b68e5"),
        )
        return res
