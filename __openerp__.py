# -*- encoding: utf-8 -*-
# Copyright © 2013 Marcel van der Boom. All Rights Reserved.
#
# Meta information about the substances module
{
	'name'       : 'Phrase management',
	'version'    : '1.0',
	'author'     : 'HSD',
	'category'   : 'Generic Modules/Others',
	'website'    : 'http://hsdev.com',
	'url'        : 'http://hsdev.com',
        'summary'    : 'Manage legislative product phrases',
	'description': 'Module to manage phrases/statement for products (examples: R/S phrases, Health statements etc.)',
	'depends'    : ['base','product','stock'],
	'init_xml'   : [],
	'update_xml' : [
	  'phrase_view.xml',
	  'security/ir.model.access.csv',
          'data/product.phrase.type.csv'
	],
	'active'     : False,
	'installable': True
}
