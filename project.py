# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2015
#    All Rights Reserved.
#    info skype: german_442 email: (german.ponce@outlook.com)
############################################################################

from openerp.osv import fields, osv
from openerp.tools.translate import _
from datetime import datetime, timedelta
import time
from openerp import SUPERUSER_ID

class project_task(osv.osv):
    _name = 'project.task'
    _inherit ='project.task'

    def _get_total(self, cr, uid, ids, field_name, arg, context=None):
        result={}
        total = 0.0
        for rec in self.browse(cr, uid, ids, context=None):
            for line in rec.line_ids:
                total += line.total
            result[rec.id] = total
        return result

    _columns = {
        'line_ids': fields.one2many('task.line.product','task_id','Lineas de Presupuesto'),
        'total': fields.function(_get_total, string="Total", method=True, type='float', digits=(13,2), readonly=True, help='Total por la Cantidad y el Precio.' ),

        }

    _defaults = {
        }

class task_line_product(osv.osv):
    _name = 'task.line.product'
    _description = 'Linea de Presupuesto en Tarea'
    _rec_name = 'product_id' 

    def _get_total(self, cr, uid, ids, field_name, arg, context=None):
        result={}
        total = 0.0
        for rec in self.browse(cr, uid, ids, context=None):
            total = rec.qty * rec.list_price
            result[rec.id] = total
        return result

    _columns = {
     'product_id': fields.many2one('product.template','Producto', required=True, ),
     'uom_id': fields.many2one('product.uom','Unidad de Medida', required=True, ),
     'list_price': fields.float('Precio', required=True, ),
     'qty': fields.float('Cantidad', required=True, ),
     'total': fields.function(_get_total, string="Subtotal", method=True, type='float', digits=(13,2), store=True, readonly=True, help='Total por la Cantidad y el Precio.' ),
     'task_id': fields.many2one('project.task', 'ID REF'),
    }
    _defaults = {
    'qty': 1,
        }
    _order = 'product_id' 

    def on_change_product(self, cr, uid, ids, product_id, context=None):
        res = {}
        product_obj = self.pool.get('product.template')
        print "############ EJECUTANDO "
        print "############ PRODUCT IDS ", product_id
        if product_id:
            prod_br = product_obj.browse(cr, uid, product_id, context)
            print "############ UOM ID >>> ", prod_br.uom_id.name
            print "############ LIST PRICE >>> ", prod_br.list_price
            res.update({
                'uom_id': prod_br.uom_id.id,
                'list_price': prod_br.list_price,
                })
        print "################ RES >>> ", res
        return {'value':res}

    def on_change_product_total(self, cr, uid, ids, list_price, qty, context=None):
        res = {}
        total = list_price * qty
        res.update({
                'total': total,
                })
        return {'value':res}
