# -*- coding: utf-8 -*-

from openerp.osv import fields, osv

class personal_expense(osv.osv):
	_name = 'personal.expense'

	name = fields.char()
	_columns = {
		'subject' : fields.char('Subject', size=120, required=True),
		'date' : fields.date('Date', required=True),
		'note' : fields.text('Notes'),
		'amount' : fields.float('Amount', required=True),
		'type' : fields.selection([
			('transport', 'Transport'),
			('household', 'Household'),
			('personal', 'Personal'),
			],'Type', required=True),
	}

class personal_lunch(osv.osv):
	_name = 'personal.lunch'

	_columns = {
		'subject' : fields.many2one('lunch.product', 'Product', required=True),
		'date' : fields.date('Date', required=True),
		'note' : fields.text('Notes'),
	}