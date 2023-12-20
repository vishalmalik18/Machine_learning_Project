from flask import Flask,request,jsonify
import util
from flask_cors import CORS
app = Flask(__name__)

@app.route('/Hello')
def Hello():
    return "Hello"

@app.route('/Creadit_card_fraud_detaction',methods=['POST'])
def Creadit_card_fraud_detaction():
    Time = int(request.form['Time'])
    v1=float(request.form['v1'])
    v2=float(request.form['v2'])
    v3=float(request.form['v3'])
    v4=float(request.form['v4'])
    v5=float(request.form['v5'])
    v6=float(request.form['v6'])
    v7=float(request.form['v7'])
    v8=float(request.form['v8'])
    v9=float(request.form['v9'])
    v10=float(request.form['v10'])
    v11=float(request.form['v11'])
    v12=float(request.form['v12'])
    v13=float(request.form['v13'])
    v14=float(request.form['v14'])
    v15=float(request.form['v15'])
    v16=float(request.form['v16'])
    v17=float(request.form['v17'])
    v18=float(request.form['v18'])
    v19=float(request.form['v19'])
    v20=float(request.form['v20'])
    v21=float(request.form['v21'])
    v22=float(request.form['v22'])
    v23=float(request.form['v23'])
    v24=float(request.form['v24'])
    v25=float(request.form['v25'])
    v26=float(request.form['v26'])
    v27=float(request.form['v27'])
    v28=float(request.form['v28'])
    Amount=float(request.form['Amount'])

    predication_result = util.creadit_card_preadication(Time,v1,v2,v3,v4,v5,v6,v7,v8,
                                                        v9,v10,v11,v12,v13,v14,
                                                        v15,v16,v17,v18,v19,v20,
                                                        v21,v22,v23,v24,v25,v26,
                                                        v27,v28,Amount)
    
    predication_value = predication_result.tolist()

    if predication_value[0] > 0.5:
        message = "fraud"

    else:
        message = "Not a fraud"

    response = jsonify({
        'estimated':predication_value,
        'result_message':message
    })

    return response
if __name__ == '__main__':
    util.load_save_artifacts()
    app.run()