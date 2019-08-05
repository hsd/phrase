# -*- encoding: utf-8 -*-
# Copyright © 2008-Today Marcel van der Boom. All Rights Reserved. c
from openerp import models, fields, api

import logging
logger = logging.getLogger(__name__)

#
# Phrase types
#
# Examples for products:
# R - risk phrases             [regulated] [deprecated]
# S - safety phrases           [regulated] [deprecated]
# H - health statements        [regulated]
# P - precautionary statements [regulated]
# EUH - euh statements         [regulated]
class product_phrase_type(models.Model):
  _name   = 'product.phrase.type'
  _description = 'Phrase types'

  name        = fields.Char(size=3, required=True)
  description = fields.Text()
  regulated   = fields.Boolean(default = False)
  active      = fields.Boolean(default = True)

  # Note: sql constraint may not be updated automatically on change!
  _sql_constraints = [
    ('name', 'UNIQUE(name)', 'Name for the phrasetype must be unique')
  ]

#
# Phrases, as such
class product_phrase(models.Model):
  _name = 'product.phrase'
  _description = 'Product phrases'

  # Fields for phrases
  type_id  = fields.Many2one(string = 'Type', comodel_name = 'product.phrase.type', required=True)
  name     = fields.Char(string = 'Code',   size=64,  required=True)
  phrase   = fields.Char(size=256, required=True, translate=True)

  notes    = fields.Text()
  addition = fields.Boolean(string = 'Needs addition', default = False)
  active   = fields.Boolean(default = True)
  sequence = fields.Integer(default = 1)

  product_ids = fields.One2many(comodel_name = 'product.phraseinfo',
                                inverse_name = 'phrase_id', string='Products')

  # Show the translated
  # We select the translations from our module, only the phrase field, of model type.
  # With this config, modify is possible, not adding and deleting
  translate_ids = fields.One2many(comodel_name = 'ir.translation',
                                  inverse_name = 'res_id',  string='Translation',
                                  domain = [('module','=','phrase'),
                                            ('name'  ,'=','product.phrase,phrase'),
                                            ('type'  ,'=','model')],
                                  context = {"default_name": 'product.phrase,phrase',
                                             "default_type":'model',
                                             "default_module": 'phrase'})


  _order = "sequence,type_id, name"

  # Note: sql constraint may not be updated automatically on change!
  _sql_constraints = [
    ('ident', 'UNIQUE(type_id, name)', 'Phrase codes must be unique within their type')
  ]


# Define the link model
# We need to define this explicitly, because of the addition field
class product_phraseinfo(models.Model):
  _name = 'product.phraseinfo'
  _description = 'Phrase information for products'

  # Define name, so searches work intuitively
  name = fields.Char(related = 'phrase_id.name')

  # Link to the product and the phrase
  product_tmpl_id = fields.Many2one('product.template', string = 'Product', required=True, ondelete='cascade')
  phrase_id  = fields.Many2one('product.phrase', string = 'Code', required=True)

  # Field that holds the, per assignment, addition when applicable
  addition   = fields.Char(string = 'Optional addition (when applicable)', size=128)

  # Allow reordering per product.
  sequence   = fields.Integer(default = 1)

  # For form design, we include these related fields
  type       = fields.Char(related = 'phrase_id.type_id.name')
  phrase     = fields.Char(related = 'phrase_id.phrase')
  # Get the product code in here for sorting and identification
  product_code = fields.Char(related = 'product_tmpl_id.default_code', store=True)

  # By default, sort by priority (only relavant from products point of view)
  _order = 'sequence'

# Let the products have phrases, using models should probably define a domain
class product_template(models.Model):
   _name = 'product.template'
   _inherit = 'product.template'

   phrase_ids = fields.One2many(comodel_name = 'product.phraseinfo',
                                inverse_name = 'product_tmpl_id', string='Phrases')

   # FIXME: this should not be here!!
   default_code = fields.Char(store=True, related='product_variant_ids.default_code')
