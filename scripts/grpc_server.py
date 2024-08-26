import os
import sys
from concurrent import futures
import grpc
import pickle

# Add the project root directory to Python path
# project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(project_root)

import rpc_gen.service_pb2 as pb2
import rpc_gen.service_pb2_grpc as pb2_grpc
from scripts.app import text_transformer
from settings import Settings

# Load the model and vectorizer
model = pickle.load(open(Settings.MODEL_PATH, "rb"))
vectorizer = pickle.load(open(Settings.VECTORIZER_PATH, "rb"))

class SpamDetectorServicer(pb2_grpc.SpamDetectorServicer):
    def Predict(self, request, context):
        # Transform and vectorize the input message
        transformed_text = text_transformer(request.message)
        vector_input = vectorizer.transform([transformed_text])
        # Predict whether the message is spam
        result = model.predict(vector_input)[0]
        # Return the result in the response
        return pb2.SpamRes(result=result)

def serve():
    # Create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # Add the SpamDetector service to the server
    pb2_grpc.add_SpamDetectorServicer_to_server(SpamDetectorServicer(), server)
    # Bind the server to port 50051 (standard gRPC port)
    server.add_insecure_port("[::]:50051")
    # Start the server
    server.start()
    # Keep the server running
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
