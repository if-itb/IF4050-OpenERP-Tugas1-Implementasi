# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Course(models.Model):
	_name = 'openacademy.course'

	name = fields.Char(string="Title", required=True)
	description = fields.Text()