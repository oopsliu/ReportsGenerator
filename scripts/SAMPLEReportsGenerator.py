from flask import Flask, render_template, request, redirect, url_for, abort, session
from docxtpl import DocxTemplate
import os


template_dir =  os.path.dirname(os.path.dirname(__file__))

template_dir = os.path.join(template_dir, '..','templates')
print (template_dir)


app = Flask(__name__, template_folder=template_dir)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        selectedValue = request.form['option']
        return redirect(url_for('click', selectedValue=selectedValue))
    return render_template('test.html')


@app.route('/<selectedValue>')
def click(selectedValue):
    print (selectedValue)
    return render_template(selectedValue + '.html')


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)



# app = Flask(__name__,template_folder=template_dir)

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


# if __name__ == '__main__':
    # app.run()