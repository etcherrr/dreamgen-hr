from odoo import api, fields, models, exceptions, _

class statuskelulusan(models.Model):
    _name = "status.kelulusan"

    name = fields.Char(string='Name', required=True)