#!/bin/bash
python3 odoo-bin -c debian/odoo.conf --addons-path="./custom,./addons/" -u library -d default