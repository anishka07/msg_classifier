import grpc
import rpc_gen.service_pb2 as pb2
import rpc_gen.service_pb2_grpc as pb2_grpc

def run():
    # Connect to the gRPC server at localhost:50051
    with grpc.insecure_channel('localhost:50051') as channel:
        # Create a stub (client) for the SpamDetector service
        stub = pb2_grpc.SpamDetectorStub(channel)
        
        # Get the message to classify from user input
        message = input("Enter the message to classify: ")
        
        # Create a PredictRequest message
        request = pb2.PredictRequest(message=message)
        
        # Call the Predict method on the server
        response = stub.Predict(request)
        
        # Print the result
        print(f"Is Spam: {response.is_spam}")

if __name__ == "__main__":
    run()
