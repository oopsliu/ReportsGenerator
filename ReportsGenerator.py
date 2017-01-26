from flask import Flask, flash, render_template, request, redirect, url_for, abort, session
from docxtpl import DocxTemplate
import os,sys,subprocess

template_dir =  os.path.dirname(__file__)
template_dir = os.path.join(template_dir,'templates')

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
	
@app.route('/confirm')
def showConfirm():
   return render_template('confirm.html')

@app.route('/')
def openDoc():
	docx = r"E:\Projects\2017.1.20_generateReports\ReportsGenerator\docx\docxtmpl\meeting\out.docx"
	wordPath = r'E:\Software\MicrosoftOffice\Office15\WINWORD.EXE'
	subprocess.Popen("%s %s" % (wordPath, docx))
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
	return render_template('onsite.html')
	
# meeting page
@app.route('/meeting', methods=['GET','POST'])
def gotoMeeting():
	if request.method == 'POST':
		meetingtime = request.form['meetingtime']
		content = request.form['content']
		plan = request.form['plan']
		
		flash('You were successfully logged in')
		return redirect(url_for('showConfirm'))
		# tpl = DocxTemplate(r"E:\Projects\2017.1.20_generateReports\ReportsGenerator\docx\docxtmpl\meeting\meeting.docx")
		# context = {
			# 'item1': meetingtime,
			# 'item2': content,
			# 'item3': plan
		# }
		# tpl.render(context)
		# tpl.save(r"E:\Projects\2017.1.20_generateReports\ReportsGenerator\docx\docxtmpl\meeting\out.docx")
		
		
	return render_template('meeting.html')

		
	

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


if __name__ == '__main__':
	app.run(host='localhost', port=5000, debug=True)