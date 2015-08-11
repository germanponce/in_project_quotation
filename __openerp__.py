# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2015
#    All Rights Reserved.
#    info skype: german_442 email: (german.ponce@outlook.com)
############################################################################

{
    'name': 'Presupuestos en Proyectos (Extension)',
    'version': '1',
    "author" : "German Ponce Dominguez",
    "category" : "Almacen",
    'description': """

Este modulo añade en cada Tarea los Productos a utilizar, cantidad, costo, total.

    - Añade Total por Tarea.
    - Total por Fase.
    - Total por Proyecto.

    """,
    "website" : "http://integra.avalos.co",
    "license" : "AGPL-3",
    "depends" : ["account","project"],
    "init_xml" : [],
    "demo_xml" : [],
    "update_xml" : [
                    "project.xml",
                    ],
    "installable" : True,
    "active" : False,
}
