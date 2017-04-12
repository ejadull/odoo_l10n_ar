# -*- coding: utf-8 -*-
##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{

    "name" : "Checkbook Management",

    "version" : "1.0",

    "author" : "OPENPYME SRL",

    "website": "openpyme.com.ar",

    "category" : "Treasury",

    "summary": "Checkbook management for Own Checks",

    "license" : "AGPL-3",

    "depends" : ["base","l10n_ar_account_check"],

    "data" : [

        "security/ir.model.access.csv",
        "security/security.xml",
        "views/checkbook_view.xml",
        "views/account_voucher_view.xml",
        "views/account_issued_check_view.xml",
        "wizard/create_checkbook_view.xml",
        "wizard/cancel_issued_check_wizard_view.xml",
        "wizard/reject_issued_check_wizard_view.xml"

    ],

    "active": False,

    "installable": True,

}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:




