from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    send_employee_reminder_birthday = fields.Boolean(related="company_id.send_employee_reminder_birthday", readonly=False)