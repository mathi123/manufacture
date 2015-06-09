# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in root directory
##############################################################################

from openerp import models, fields


class Machinery(models.Model):
    _inherit = 'machinery'

    purch_inv_line = fields.Many2one('account.invoice.line',
                                     string='Invoice Line')
