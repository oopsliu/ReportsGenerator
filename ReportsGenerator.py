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

# confirmation page
@app.route('/confirm')
def showConfirm():
   return render_template('confirm.html')







	




if __name__ == '__main__':
	app.run(host='localhost', port=5000, debug=True)
	
# @app.route('/signup', methods=['POST'])
# def signup():
	# session['username'] = request.form['username']
	# session['message'] = request.form['message']
	# tpl = DocxTemplate(r"E:\Projects\2017.1.20_generateReports\test\tmp.docx")
	# context = {
		# 'tbl_contents': [
			# {'label': '人员', 'cols': [request.form['message']]},
			# {'label': '时间', 'cols': [request.form['message']]},
			# {'label': '内容', 'cols': [request.form['message']]},
			# ]
	# }
	# tpl.render(context)
	# tpl.save(r"E:\Projects\2017.1.20_generateReports\test\out.docx")
	# return redirect(url_for('message'))

# @app.route('/message')
# def message():

	# return render_template('message.html', message=session['message'])
	
	
# @app.route('/')
# def home():
	# return render_template('index.html')
	
# @app.route('/category', methods=['GET','POST'])
# def click():
	# global selectedValue
	# selectedValue = request.form['options']
	# return redirect(url_for('renderingPage'))
	
# @app.route('/content')
# def renderingPage():
	# return render_template(selectedValue + '.html')
	
# @app.route('/')
# def openDoc():
	# docx = r"E:\Projects\2017.1.20_generateReports\ReportsGenerator\docx\docxtmpl\meeting\out.docx"
	# wordPath = r'E:\Software\MicrosoftOffice\Office15\WINWORD.EXE'
	# subprocess.Popen("%s %s" % (wordPath, docx))
	# return render_template('index.html')		