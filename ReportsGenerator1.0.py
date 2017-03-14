#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, flash, render_template, request, redirect, url_for, abort, session
from docxtpl import DocxTemplate,InlineImage
from docx.shared import Mm, Pt
import os,sys,subprocess,csv,codecs,re
import matplotlib.pyplot as plt
import pandas as pd

# working directories
current_dir =  os.path.dirname(__file__)
template_dir = os.path.join(current_dir,'templates')
docx_dir = os.path.join(current_dir,'docx')
docxtmp_dir = os.path.join(docx_dir,'docxtmpl')
docxout_dir = os.path.join(docx_dir,'docxoutput')
static_dir = os.path.join(current_dir,'static')
csv_dir = os.path.join(static_dir,'csv')
img_dir = os.path.join(static_dir,'image')

# get fixed parameters from config file:
# prj,userOrg,userOrgShr,userAddr,userCont,userCont2,userPhone,esriAddr,esriCont,esriPhone
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
		
# patrol seasonal page
@app.route('/patrolseasonal', methods=['GET','POST'])
def gotoPatrolSeasonal():
	if request.method == 'POST':
		selectedValue = request.form['options']
		if selectedValue == '1st':
			season = '第一季度'
			myCsv = csv_dir + "\\1\\machines.csv"
			imgDir = img_dir + "\\1"
		elif selectedValue == '2nd':
			season = '第二季度'
			myCsv = csv_dir + "\\2\\machines.csv"
			imgDir = img_dir + "\\2"
		elif selectedValue == '3rd':
			season = '第三季度'
			myCsv = csv_dir + "\\3\\machines.csv"
			imgDir = img_dir + "\\3"
		elif selectedValue == '4th':
			season = '第四季度'
			myCsv = csv_dir + "\\4\\machines.csv"
			imgDir = img_dir + "\\4"
		
		m31c1 = request.form['31c1']
		m31m1 = request.form['31m1']
		m31c2 = request.form['31c2']
		m31m2 = request.form['31m2']
		m31c3 = request.form['31c3']
		m31m3 = request.form['31m3']

		m32c1 = request.form['32c1']
		m32m1 = request.form['32m1']
		m32c2 = request.form['32c2']
		m32m2 = request.form['32m2']
		m32c3 = request.form['32c3']
		m32m3 = request.form['32m3']
		
		m35c1 = request.form['35c1']
		m35m1 = request.form['35m1']
		m35c2 = request.form['35c2']
		m35m2 = request.form['35m2']
		m35c3 = request.form['35c3']
		m35m3 = request.form['35m3']		
		
		m36c1 = request.form['36c1']
		m36m1 = request.form['36m1']
		m36c2 = request.form['36c2']
		m36m2 = request.form['36m2']
		m36c3 = request.form['36c3']
		m36m3 = request.form['36m3']		
		
		m113c1 = request.form['113c1']
		m113m1 = request.form['113m1']
		m113c2 = request.form['113c2']
		m113m2 = request.form['113m2']
		m113c3 = request.form['113c3']
		m113m3 = request.form['113m3']		
		
		m114c1 = request.form['114c1']
		m114m1 = request.form['114m1']
		m114c2 = request.form['114c2']
		m114m2 = request.form['114m2']
		m114c3 = request.form['114c3']
		m114m3 = request.form['114m3']		
		
		patrolseatime = request.form['patrolseatime']
		sysmon = request.form['sysmon']
		commiss = request.form['commiss']
		patrolseasum = request.form['patrolseasum']
		
		with open(myCsv, 'w', newline='') as fp:
			myWriter = csv.writer(fp, delimiter=',')
			data = [['machine','cpu 1st','cpu 2nd','cpu 3rd','mem 1st','mem 2nd','mem 3rd'],
					['31',m31c1,m31c2,m31c3,m31m1,m31m2,m31m3],
					['32',m32c1,m32c2,m32c3,m32m1,m32m2,m32m3],
					['35',m35c1,m35c2,m35c3,m35m1,m35m2,m35m3],
					['36',m36c1,m36c2,m36c3,m36m1,m36m2,m36m3],
					['113',m113c1,m113c2,m113c3,m113m1,m113m2,m113m3],
					['114',m114c1,m114c2,m114c3,m114m1,m114m2,m114m3]]
			myWriter.writerows(data)

		# Set colors
		myColors = [ (14, 187, 159), (245, 199, 0),  (239, 72, 54)]  

		for i in range(len(myColors)):  
			r, g, b = myColors[i]  
			myColors[i] = (r / 255., g / 255., b / 255.)  

		# Figure 0
		plt.figure(0,figsize=(14, 12))  
		# Remove the plot frame lines. 
		ax = plt.subplot(111)  
		ax.spines["top"].set_visible(False)  
		ax.spines["bottom"].set_visible(False)  
		ax.spines["right"].set_visible(False)  
		ax.spines["left"].set_visible(False)  
		ax.get_xaxis().tick_bottom()  
		ax.get_yaxis().tick_left()  
		plt.ylim(0, 80)  
		plt.xlim(8, 68)  
		plt.yticks(range(0, 81, 10), [str(x) + "%" for x in range(0, 81, 10)], fontsize=14)  
		plt.xticks(fontsize=14)  
		for y in range(10, 81, 10):  
			plt.plot(range(8, 62), [y] * len(range(8, 62)), "--", lw=0.5, color="black", alpha=0.3)  
		plt.tick_params(axis="both", which="both", bottom="off", top="off",  
						labelbottom="on", left="off", right="off", labelleft="on")  

		# Figure1
		plt.figure(1,figsize=(14, 12))  
		ax = plt.subplot(111)  
		ax.spines["top"].set_visible(False)  
		ax.spines["bottom"].set_visible(False)  
		ax.spines["right"].set_visible(False)  
		ax.spines["left"].set_visible(False)  
		ax.get_xaxis().tick_bottom()  
		ax.get_yaxis().tick_left()  
		plt.ylim(0, 80)  
		plt.xlim(8, 68)  
		plt.yticks(range(0, 81, 10), [str(x) + "%" for x in range(0, 81, 10)], fontsize=14)  
		plt.xticks(fontsize=14)  
		for y in range(10, 81, 10):  
			plt.plot(range(8, 62), [y] * len(range(8, 62)), "--", lw=0.5, color="black", alpha=0.3)  
		plt.tick_params(axis="both", which="both", bottom="off", top="off",  
						labelbottom="on", left="off", right="off", labelleft="on")  
		
		# Plot data
		patrol_data = pd.read_csv(myCsv) 

		fields0 = ['cpu 1st','cpu 2nd','cpu 3rd']
		title0 = 'CPU Utilization'
		fields1 = ['mem 1st','mem 2nd','mem 3rd']
		title1 = 'Memory Utilization'
		
		x = [10,20,30,40,50,60]
		xlabel=['31','32','35','36','113','114']

		plt.figure(0)
		plt.title(title0, fontsize=20)
		for rank, column in enumerate(fields0):  
			plt.plot(x,  
					patrol_data[column.replace("\n", " ")].values,"o-", markeredgewidth=0.0,ms=10, 
					lw=2.5, color=myColors[rank],label = fields0[rank])  
			plt.xticks(x,xlabel) 
			y_pos = patrol_data[column.replace("\n", " ")].values[-1] - 0.5  

			plt.text(61, y_pos, column, fontsize=14, color=myColors[rank])  
			
		plt.legend()
		plt.savefig(imgDir + "\\cpu.png", bbox_inches="tight")
		
		plt.figure(1)
		plt.title(title1, fontsize=20)
		for rank, column in enumerate(fields1):  
			plt.plot(x,  
					patrol_data[column.replace("\n", " ")].values,"o-", markeredgewidth=0.0,ms=10, 
					lw=2.5, color=myColors[rank],label = fields1[rank])  
			plt.xticks(x,xlabel) 
			y_pos = patrol_data[column.replace("\n", " ")].values[-1] - 0.5  

			plt.text(61, y_pos, column, fontsize=14, color=myColors[rank])  
			
		plt.legend()
		plt.savefig(imgDir + "\\mem.png", bbox_inches="tight")		
		
		inputTmpl = docxtmp_dir + '\patrolseasonal\patrolseasonal.docx'
		tpl = DocxTemplate(inputTmpl)
		context = {
			'm31c1':m31c1,
			'm31m1':m31m1,
			'm31c2': m31c2,
			'm31m2': m31m2,
			'm31c3': m31c3,
			'm31m3': m31m3,

			'm32c1': m32c1,
			'm32m1': m32m1,
			'm32c2': m32c2,
			'm32m2': m32m2,
			'm32c3': m32c3,
			'm32m3': m32m3,
			
			'm35c1': m35c1,
			'm35m1': m35m1,
			'm35c2': m35c2,
			'm35m2': m35m2,
			'm35c3': m35c3,
			'm35m3': m35m3,		
			
			'm36c1': m36c1,
			'm36m1': m36m1,
			'm36c2': m36c2,
			'm36m2': m36m2,
			'm36c3': m36c3,
			'm36m3': m36m3,		
			
			'm113c1': m113c1,
			'm113m1': m113m1,
			'm113c2': m113c2,
			'm113m2': m113m2,
			'm113c3': m113c3,
			'm113m3': m113m3,		
			
			'm114c1': m114c1,
			'm114m1': m114m1,
			'm114c2': m114c2,
			'm114m2': m114m2,
			'm114c3': m114c3,
			'm114m3': m114m3,	
			
			'imgCPU': InlineImage(tpl,imgDir + "\\cpu.png",width=Mm(112), height=Mm(96)),
			'imgMem': InlineImage(tpl,imgDir + "\\mem.png",width=Mm(112), height=Mm(96)),
			
			'season': season,
			'patrolseatime': patrolseatime,
			'sysmon': sysmon,
			'commiss': commiss,
			'patrolseasum': patrolseasum,
			
			'prj': prj,
			'userOrgShr': userOrgShr,
			'userAddr': userAddr,
			'userCont': userCont,
			'userCont2': userCont2,
			'userPhone': userPhone,
			'esriCont': esriCont
		}
		tpl.render(context)
		outputFile = docxout_dir + '\patrolseasonal' + '\\' +  userOrgShr + '_' + season + '_' + '巡检报告.docx'
		tpl.save(outputFile)
		
		flash(os.path.abspath(outputFile))
		return redirect(url_for('showConfirm'))
		
	return render_template('patrolseasonal.html')	

# confirmation page
@app.route('/confirm')
def showConfirm():
   return render_template('confirm.html')

if __name__ == '__main__':
	app.run(host='localhost', port=5000, debug=True)
