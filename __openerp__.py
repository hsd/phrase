# -*- encoding: utf-8 -*-
# Copyright © 2013 Marcel van der Boom. All Rights Reserved.
#
# Meta information about the substances module
{
	'name'       : 'Phrase management',
	'version'    : '2.0',
	'author'     : 'HSD',
	'category'   : 'Generic Modules/Others',
	'website'    : 'https://hsdev.com',
	'url'        : 'https://hsdev.com',
        'summary'    : 'Manage legislative product phrases',
	'description': 'Module to manage phrases/statement for products (examples: R/S phrases, Health statements etc.)',
	'depends'    : ['base','product','stock'],
	'data' : [
            'views/phrase.xml',
            'views/phrase_type.xml',
            'views/product.xml',
            'security/ir.model.access.csv',
            'data/product.phrase.type.csv',
            'data/product.phrase.csv'
	]
}
