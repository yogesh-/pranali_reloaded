# Copyright (c) 2015, Rtr.Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Member(Document):
	def validate(self):
		self.set_zone()
		
	def set_zone(self):
		self.zone = frappe.db.get_value("Club", self.club, "zone")
