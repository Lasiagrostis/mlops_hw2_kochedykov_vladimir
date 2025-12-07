import grpc
from concurrent import futures
import model_pb2, model_pb2_grpc
import joblib, pandas as pd

class PredictionService(model_pb2_grpc.PredictionServiceServicer):
    def __init__(self):
        self.model = joblib.load("model.pkl")

    def Predict(self, request, context):
        df = pd.DataFrame([{
            "feature1": request.feature1
        }])
        pred = self.model.predict(df)[0]
        return model_pb2.PredictResponse(prediction=str(pred))

    def Health(self, request, context):
        return model_pb2.HealthResponse(status="ok")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    model_pb2_grpc.add_PredictionServiceServicer_to_server(PredictionService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()