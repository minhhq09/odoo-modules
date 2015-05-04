# -*- coding: utf-8 -*-
#
# Author : Jerome Sonnet - jerome.sonnet@be-cloud.be
#
#
from openerp import models, fields, api, _

import logging
_logger = logging.getLogger(__name__)

class real_estate_lead (models.Model):
    """ Real Estate Lead Case """
    _name = "realestate.real_estate_lead"
    _description = "Lead/Opportunity"
    _order = "priority desc,date_action,id desc"
    _inherit = ['crm.lead']
    
    item_of_interest_id = fields.Many2one('realestate.building_land', string='Item of Interest', ondelete='set null', track_visibility='onchange',
            select=True, help="Linked item of interest (optional). Usually created when converting the lead.")

    def default_get(self, cr, uid, fields, context=None):
        res = super(real_estate_lead, self).default_get(cr, uid, fields, context=context)
        return res

real_estate_lead()

class building_land(models.Model):
    '''Building Land'''
    _name = 'realestate.building_land'
        
    owner_id = fields.Many2one('res.partner', string = 'The land owner.')
    address_id = fields.Many2one('res.partner', string = 'The land address')
    land_division = fields.Char(string = "The land division reference.")
    land_size = fields.Integer(string = "Size in ares.")   
    
    public_price = fields.Integer(string = "The public price.")
    estimated_price = fields.Integer(string = "The estimated price.")
    
    parent_id = fields.Many2one('realestate.building_land', string = 'The parent land.')
       
building_land()