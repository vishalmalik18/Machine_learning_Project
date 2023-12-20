import pickle
import numpy as np
import json

__model = None

def load_save_artifacts():
    print("loading saved artificats...start")
    global __model

    if __model is None:
        with open("D:/Creadit_card_fraud_detaction/Creadit_card_fraud_detaction.pkl","rb") as f:
            __model = pickle.load(f,encoding='utf8')
        print("loading saved artifacts... done")

def creadit_card_preadication(
        Time,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,
        v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,
        v27,v28,Amount
):
    input_data = np.array([Time,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,
        v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,
        v27,v28,Amount])
    
    reshaped_data = input_data.reshape(1,-1)
    predication = __model.predict(reshaped_data)

    return predication

if __name__ == '__main__':
    load_save_artifacts()
    
    print(creadit_card_preadication(Time=0, v1=-1.359807134,	v2= -0.072781173,	v3=2.536346738,	
    v4 =1.378155224,	v5=-0.33832077,	v6=0.462387778,	v7=0.239598554,	
    v8=0.098697901,	v9=0.36378697,	v10=0.090794172,	v11=-0.551599533,	
    v12=-0.617800856,	v13=-0.991389847,	v14=-0.311169354,
    v15=1.468176972,	v16=-0.470400525,	v17=0.207971242,
    v18=0.02579058,	v19=0.40399296,	v20=0.251412098,	
    v21=-0.018306778,	v22=0.277837576,	v23=-0.11047391,
    v24=0.066928075,	v25=0.128539358,	v26=-0.189114844,
    v27=0.133558377,	v28=-0.021053053,	Amount=149.62,))


    
    
