import grpc
from protos import model_pb2, model_pb2_grpc

channel = grpc.insecure_channel("localhost:50051")
stub = model_pb2_grpc.PredictionServiceStub(channel)

print("----- Prediction Request -----")
predict_request = model_pb2.PredictRequest(pclass=1.0)
predict_response = stub.Predict(predict_request)

print("Prediction:", predict_response.prediction, "Probability:", round(predict_response.confidence, 3))

print("\n----- Health Check -----")
health_request = model_pb2.Empty()
health_response = stub.Health(health_request)
print("Status:", health_response.status)
print("Model version:", health_response.modelVersion)