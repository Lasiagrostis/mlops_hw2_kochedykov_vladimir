import grpc
from concurrent import futures
from protos import model_pb2, model_pb2_grpc
import joblib, pandas as pd
import os

MODEL_PATH = os.environ["MODEL_PATH"]
MODEL_VERSION = os.environ["MODEL_VERSION"]
PORT = os.environ["PORT"]

class PredictionService(model_pb2_grpc.PredictionServiceServicer):
    def __init__(self):
        self.model = joblib.load(MODEL_PATH)
        self.model_version = MODEL_VERSION

    def Predict(self, request, context):
        df = pd.DataFrame([{
            "Pclass": request.pclass
        }])
        pred = self.model.predict(df)[0]
        proba = max(self.model.predict_proba(df)[0])

        return model_pb2.PredictResponse(prediction=str(pred), confidence=float(proba))

    def Health(self, request, context):
        return model_pb2.HealthResponse(status="ok", modelVersion=self.model_version)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    model_pb2_grpc.add_PredictionServiceServicer_to_server(PredictionService(), server)
    server.add_insecure_port(f'[::]:{PORT}')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()