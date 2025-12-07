import grpc
import model_pb2, model_pb2_grpc

channel = grpc.insecure_channel("localhost:50051")
stub = model_pb2_grpc.PredictionServiceStub(channel)

request = model_pb2.PredictRequest(feature1="1")
response = stub.Predict(request)
print("Prediction:", response.prediction)