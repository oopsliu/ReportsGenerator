#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import cx_Oracle
from xml.etree import ElementTree


# parse mxdperfstat result xml
HTML = r'E:\Projects\2017.1.20_generateReports\ReportsGenerator\scripts\test.xml'
with open(HTML, 'rt') as f:
	tree = ElementTree.parse(f)

for node in tree.iter('scale'):
	print node.attrib['Scale'], ": ",node.attrib['ScaleRefreshTime']







# connect to sde via python
con = cx_Oracle.connect('sde/sde@192.168.220.131/orcl')

start = time.time()

cur=con.cursor()
cur.execute('select * from bigPolygon')
res = cur.fetchall()

elapsed = (time.time() - start)
print elapsed, "seconds"

cur.close()
con.close() 