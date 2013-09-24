# -*- encoding: utf-8 -*-
# Copyright © 2008-Today Marcel van der Boom. All Rights Reserved. c
from osv import osv, fields

#
# Phrase types
#
# Examples for products:
# R - risk phrases             [regulated] [deprecated]
# S - safety phrases           [regulated] [deprecated]
# H - health statements        [regulated]
# P - precautionary statements [regulated]
# EUH - euh statements         [regulated]
class product_phrase_type(osv.osv):
  _name   = 'product.phrase.type'
  _description = 'Phrase types'
  _columns = {
    'name'       : fields.char('Code', size=3, required=True, select=1),
    'description': fields.text('Description'),
    'regulated'  : fields.boolean('Regulated', required=True),
    'active'     : fields.boolean('Active', required=True)
  }
  _defaults = {
    'active'    : lambda *a: True,
    'regulated' : lambda *a: False
  }
  # Note: sql constraint may not be updated automatically on change!
  _sql_constraints = [
    ('name', 'UNIQUE(name)', 'Code for the phrasetype must be unique')
  ]
product_phrase_type()

#
# Phrases, as such
class product_phrase(osv.osv):
  _name = 'product.phrase'
  _description = 'Product phrases'
  _columns = {
      # Common stuff for all name-like structures
      'name'    : fields.char('Code',   size=64,  required=True),
      'type_id' : fields.many2one('product.phrase.type','Type', required=True),
      'phrase'  : fields.char('Phrase', size=256, required=True, translate=True),
      'notes'   : fields.text('Notes', translate=True),
      'addition': fields.boolean('Needs addition', required=True),
      'active'  : fields.boolean('Active', required=True)
  }
  _order = "type_id, name"
  _defaults = {
    'addition'  : lambda *a: False,
    'active'    : lambda *a: True
  }
  # Note: sql constraint may not be updated automatically on change!
  _sql_constraints = [
    ('ident', 'UNIQUE(type_id, name)', 'Phrases must be unique within their type')
  ]
product_phrase()
