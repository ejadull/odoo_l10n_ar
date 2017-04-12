# -*- coding: utf-8 -*-
##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
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

    "name" : "Argentina - Chart of Account",

    "version" : "1.0",

    "author" : "OPENPYME SRL",

    "website": "openpyme.com.ar",

    "category" : "Localization/Account Charts",

    "summary": "Accounting chart for Argentina in Open ERP",

    "depends" : [

        "account_chart"

    ],

    "data" : [

        "views/account_tax_view.xml",
        "views/res_currency_view.xml",
        "data/account_tax_code_data.xml",
        "data/account_chart_data.xml",
        "data/account_tax_data.xml",
        "wizard/l10n_chart_ar_wizard.xml",


    ],

    "active": False,

    "installable": True,

}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

