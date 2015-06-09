# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in root directory
##############################################################################

from openerp import models, fields


class StockPackOperation(models.Model):
    _inherit = "stock.pack.operation"

    machine = fields.Many2one('machinery', string='Machine')
