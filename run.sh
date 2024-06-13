#!/bin/bash
python3 odoo-bin -c debian/odoo.conf --addons-path="./addons/" -u library_isl -d odoo
