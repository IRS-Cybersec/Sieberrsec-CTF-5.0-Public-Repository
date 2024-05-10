from flask import Flask, render_template, redirect, request, make_response
import jwt
import uuid

app = Flask(__name__)
with open('secret.txt', 'r') as f:
	app.config['SECRET'] = f.read()

@app.route('/')
def index():
	try:
		if 'access_token' in  request.cookies: 
			access = jwt.decode(request.cookies['access_token'], app.config['SECRET'], algorithms=['HS256'])
			return render_template('home.html', access=access)
			
		else:
			return render_template('index.html')
				
	except:	
		return render_template('error.html')
		

@app.route('/create', methods=['POST'])
def create():
	token = jwt.encode({'uuid':str(uuid.uuid4()), 'username':request.form['username']}, app.config['SECRET'], algorithm='HS256')
	print(token)
	resp = make_response(redirect('/',200))
	resp.set_cookie('access_token', token)
	return resp

@app.route('/source', methods=['GET'])
def source():
	file = request.args.get('file')
	if 'home' in file:
		return render_template('error.html')
	file = file.replace('..', '')
	file = file.replace('../','')
	file = file.replace('secret', '')
	print('templates/'+file)
	with open('templates/'+file,'r') as f:
		return f.read()

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
