from Sensor.pipeline.training_pipeline import TrainingPipeline
from flask import Flask, request, jsonify,render_template
import joblib 
import os
import pandas as pd
from Sensor.ml.model.estimator import ModelResolver
from Sensor.Constant.training_pipeline import project_directory,saved_model_dir
from Sensor.exception import SensorException
from Sensor.utils.main_utils import load_object,read_yaml_file
from Sensor.Constant.training_pipeline import log_dir,schema_file
from sklearn.metrics import f1_score
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])
model_path=os.path.join(project_directory,saved_model_dir)
model_resolver=ModelResolver(model_path)
drop_columns=read_yaml_file(schema_file)['drop_columns']
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/train',methods=['POST'])
def train():
    try:
        # Initialize and start the training pipeline
        pipeline = TrainingPipeline()
        pusher_artifact = pipeline.start_pipeline()
        return jsonify({"message": "Training pipeline executed successfully", "pusher_artifact": str(pusher_artifact)})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/predict', methods=['POST'])
def predict():
    try: 
        file = request.files['file']
        df = pd.read_csv(file)
        latest_model_path=model_resolver.get_latest_model_path()
        model = load_object(latest_model_path)
        df = df.drop(drop_columns,axis=1)
        if 'class' in df.columns:
            df['class']=df['class'].replace({'pos':1,'neg':0})
            features,labels=df.drop('class',axis=1),df['class']
        else:
            features=df.values
        predictions =  model.predict(features)
        if 'class' in df.columns:
            f1 = f1_score(labels,predictions)
            return jsonify({"predictions": predictions.tolist(), "f1_score": f1})
        else:
            return jsonify({"predictions": predictions.tolist()})

    except Exception as e:
        raise SensorException("Error occured while making prediction.")
    return jsonify({"message": str(df.columns)})
if __name__ == '__main__':
    app.run(debug=True)