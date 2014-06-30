import os
from flask import Flask, request, redirect, url_for, jsonify
import uuid
from subprocess import Popen, PIPE
app = Flask(__name__)


@app.route('/',methods=['GET'])
# for browser
def hello_world():
    # print Popen("/Applications/MATLAB_R2013a.app/bin/matlab -nodisplay -nosplash -r \"try,testing('123'),catch,  end,quit\"", stdout=PIPE, shell=True).stdout.read()
    # outputs = []
    # names = ['Urticaria','Seborrheic','Acne','Psoriasis','Skin Cancer','Unrecognized']
    # for index,line in enumerate("0.9\n0.1\n0.2\n0.3\n0.8\n0.1\n".split()):
    #     outputs.append({'name':names[index],'confidence':float(line.strip())})
    # return jsonify({'diagnoses':outputs})

    return jsonify({'answer':'hello_world'})

# for ios
@app.route('/', methods=['POST'])
def classify():
    #return jsonify({'answer_post':'hello_world'})
    #print request.files['file']
    user = request.files['userfile']
    user.save('test.wav')
    answer = ['Taraba Major','Great antshrike','Fixy Mixy','Chicken']
    #return jsonify({'0':answer[0], '1':answer[1]})
    answer = {'1':'Taraba Major','2':'Great antshrike','3':'Fixy Mixy','4':'Chicken'}
    return jsonify(answer)

@app.route('/old',methods=['POST'])
def diagnose():
    file = request.files['file']
    filename = uuid.uuid4().hex
    file.save(os.path.join('inputs', filename))
    print Popen("/Applications/MATLAB_R2013a.app/bin/matlab -nodisplay -nosplash -r \"try,testing('"+filename+"'),catch,  end,quit\"", stdout=PIPE, shell=True).stdout.read()
    names = ['Urticaria','Seborrheic','Acne','Psoriasis','Skin Cancer','Unrecognized']
    outputs = []
    for index,line in enumerate(open('outputs/'+filename,'r')):
        outputs.append({'name':names[index],'confidence':float(line.strip())})
    print outputs
    return jsonify({'diagnoses':outputs})
    
if __name__ == '__main__':
    app.debug = True
    app.run()
