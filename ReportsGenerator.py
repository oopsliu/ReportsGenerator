#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, flash, render_template, request, redirect, url_for, abort, session
from docxtpl import DocxTemplate
import os,sys,subprocess,csv,codecs,re

# working directories
current_dir =  os.path.dirname(__file__)
template_dir = os.path.join(current_dir,'templates')
docx_dir = os.path.join(current_dir,'docx')
docxtmp_dir = os.path.join(docx_dir,'docxtmpl')
docxout_dir = os.path.join(docx_dir,'docxoutput')

# get fixed parameters from config file:
# prj,userOrg,userOrgShr,userAddr,userCont,userPhone,esriAddr,esriCont,esriPhone
configFile = os.path.join(current_dir ,'config.csv')
reader = csv.reader(codecs.open(configFile, encoding="utf-8"))
next(reader)
dict = {}
dict = {row[0]: row[2] for row in reader}
locals().update(dict)

# create flask application
app = Flask(__name__,template_folder=template_dir)
app.secret_key = 'some_secret'

# home page (select report category)
@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		selectedValue = request.form['options']
		if selectedValue == 'onsite':
			return redirect(url_for('gotoOnsite'))
		elif selectedValue == 'meeting':
			return redirect(url_for('gotoMeeting'))
		elif selectedValue == 'patrol':
			return redirect(url_for('gotoPatrol'))
		elif selectedValue == 'patrolsea':
			return redirect(url_for('gotoPatrolSeasonal'))
	return render_template('index.html')
	
# onsite page
@app.route('/onsite', methods=['GET', 'POST'])
def gotoOnsite():
	if request.method == 'POST':
		selectedValue = request.form['options']
		onsitetime = request.form['onsitetime']
		title = request.form['title']
		expert = request.form['expert']
		content = request.form['content']
		summary = request.form['summary']
		
		if selectedValue == 'training':
			type = '技术培训'
		elif selectedValue == 'salon':
			type = '技术沙龙'
		elif selectedValue == 'onsite':
			type = '现场技术支持'
		
		inputTmpl = docxtmp_dir + '\onsite\onsite.docx'
		tpl = DocxTemplate(inputTmpl)
		context = {
			'type': type,
			'onsitetime': onsitetime,
			'title': title,
			'expert': expert,
			'content': content,
			'summary': summary,
			
			'prj': prj,
			'userOrgShr': userOrgShr,
			'userAddr': userAddr,
			'userCont': userCont,
			'userPhone': userPhone,
			'esriCont': esriCont
		}
		tpl.render(context)
		date = re.split(',|，',onsitetime)[0]
		outputFile = docxout_dir + '\onsite' + '\\' +  userOrgShr + '_' + date + '_' + '技术服务记录表.docx'
		tpl.save(outputFile)
		
		flash(os.path.abspath(outputFile))
		return redirect(url_for('showConfirm'))		
		
	return render_template('onsite.html')
	
# meeting page
@app.route('/meeting', methods=['GET','POST'])
def gotoMeeting():
	if request.method == 'POST':
		meetingtime = request.form['meetingtime']
		content = request.form['content']
		plan = request.form['plan']
		
		inputTmpl = docxtmp_dir + '\meeting\meeting.docx'
		tpl = DocxTemplate(inputTmpl)
		context = {
			'meetingtime': meetingtime,
			'content': content,
			'plan': plan,
			
			'prj': prj,
			'userOrgShr': userOrgShr,
			'userAddr': userAddr,
			'userCont': userCont,
			'userPhone': userPhone,
			'esriCont': esriCont
		}
		tpl.render(context)
		date = re.split(',|，',meetingtime)[0]
		outputFile = docxout_dir + '\meeting' + '\\' +  userOrgShr + '_' + date + '_' + '会议纪要.docx'
		tpl.save(outputFile)
		
		flash(os.path.abspath(outputFile))
		return redirect(url_for('showConfirm'))
		
	return render_template('meeting.html')
	
	
	
	
# patrol seasonal page
@app.route('/patrolseasonal', methods=['GET','POST'])
def gotoPatrolSeasonal():
	if request.method == 'POST':
		meetingtime = request.form['meetingtime']
		content = request.form['content']
		plan = request.form['plan']
		
		inputTmpl = docxtmp_dir + '\patrolseasonal\patrolseasonal.docx'
		tpl = DocxTemplate(inputTmpl)
		context = {
			'meetingtime': meetingtime,
			'content': content,
			'plan': plan,
			
			'prj': prj,
			'userOrgShr': userOrgShr,
			'userAddr': userAddr,
			'userCont': userCont,
			'userPhone': userPhone,
			'esriCont': esriCont
		}
		tpl.render(context)
		date = re.split(',|，',meetingtime)[0]
		outputFile = docxout_dir + '\patrolseasonal' + '\\' +  userOrgShr + '_' + date + '_' + '会议纪要.docx'
		tpl.save(outputFile)
		
		flash(os.path.abspath(outputFile))
		return redirect(url_for('showConfirm'))
		
	return render_template('patrolseasonal.html')	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

	
# patrol page
@app.route('/patrol', methods=['GET','POST'])
def gotoPatrol():
	if request.method == 'POST':
		y_init = request.form['y_init']
		y_base = request.form['y_base']
		y_buss = request.form['y_buss']		
		y_spaq = request.form['y_spaq']
		y_attq = request.form['y_attq']
		y_spaa = request.form['y_spaa']
		y_expm = request.form['y_expm']
		y_iden = request.form['y_iden']
		y_quer = request.form['y_quer']
		y_geos = request.form['y_geos']	
		
		z_init = request.form['z_init']
		z_base = request.form['z_base']
		z_buss = request.form['z_buss']		
		z_spaq = request.form['z_spaq']
		z_attq = request.form['z_attq']
		z_spaa = request.form['z_spaa']
		z_expm = request.form['z_expm']
		z_iden = request.form['z_iden']
		z_quer = request.form['z_quer']
		z_geos = request.form['z_geos']			

		x_init = request.form['x_init']
		x_base = request.form['x_base']
		x_buss = request.form['x_buss']		
		x_spaq = request.form['x_spaq']
		x_attq = request.form['x_attq']
		x_spaa = request.form['x_spaa']
		x_expm = request.form['x_expm']
		x_iden = request.form['x_iden']
		x_quer = request.form['x_quer']
		x_geos = request.form['x_geos']		
		
		mxdren = request.form['mxdren']
		mxdque = request.form['mxdque']	
		
		patroldate = request.form['patroldate']
		patrolcomm = request.form['patrolcomm']
		patrolsumm = request.form['patrolsumm']		
		
		inputTmpl = docxtmp_dir + '\patrol\patrol.docx'
		tpl = DocxTemplate(inputTmpl)
		context = {
			'y_init': y_init,
			'y_base': y_base,
			'y_buss': y_buss,
			'y_spaq': y_spaq,
			'y_attq': y_attq,
			'y_spaa': y_spaa,
			'y_expm': y_expm,
			'y_iden': y_iden,
			'y_quer': y_quer,
			'y_geos': y_geos,
			
			'z_init': z_init,
			'z_base': z_base,
			'z_buss': z_buss,
			'z_spaq': z_spaq,
			'z_attq': z_attq,
			'z_spaa': z_spaa,
			'z_expm': z_expm,
			'z_iden': z_iden,
			'z_quer': z_quer,
			'z_geos': z_geos,		

			'x_init': x_init,
			'x_base': x_base,
			'x_buss': x_buss,
			'x_spaq': x_spaq,
			'x_attq': x_attq,
			'x_spaa': x_spaa,
			'x_expm': x_expm,
			'x_iden': x_iden,
			'x_quer': x_quer,
			'x_geos': x_geos,		

			'mxdren': mxdren,
			'mxdque': mxdque,
			
			'patroldate': patroldate,
			'patrolcomm': patrolcomm,
			'patrolsumm': patrolsumm,
			
			'prj': prj,
			'userOrgShr': userOrgShr,
			'userAddr': userAddr,
			'userCont': userCont,
			'userPhone': userPhone,
			'esriCont': esriCont
		}
		tpl.render(context)
		date = re.split(',|，',patroldate)[0]
		outputFile = docxout_dir + '\patrol' + '\\' +  userOrgShr + '_' + date + '_' + '日常巡检服务记录表.docx'
		tpl.save(outputFile)
		
		flash(os.path.abspath(outputFile))
		return redirect(url_for('showConfirm'))
		
	return render_template('patrol.html')

# confirmation page
@app.route('/confirm')
def showConfirm():
   return render_template('confirm.html')

if __name__ == '__main__':
	app.run(host='localhost', port=5000, debug=True)
