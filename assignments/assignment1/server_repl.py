from concurrent import futures
import logging
import replicator_pb2_grpc as pb2_grpc
import replicator_pb2 as pb2
import grpc
import json
import pymongo

class assignmentService(pb2_grpc.replServicer):
    def __init__(self, *args, **kwargs):
        pass

    def query(self, request, context):

        # get the string from the incoming request
        message = request.message
        update = self.query_mongo(message)
        mess = f'Hello I am up and running received "{message}" message from you'
        result = {'message': mess, 'received': True}
        print ("Received message: " + message)
        print ("\nMongodb query fired: " + str(update))
        return pb2.rec(**result)

    def query_mongo(self, message):
        js = json.loads(message)
        mydb = myclient["college"]
        mycol = mydb["students"]
        if js["kind"] == "insert":
            arr = js["columnvalues"]
            x = mycol.insert_one({"_id" : arr[0], "first_name": arr[1], "last_name": arr[2], "sjsu_id": arr[3],
            "email" : arr[4], "create_timestamp": arr[5], "update_timestamp": arr[6]
            })
            print(x)
            return True
        elif js["kind"] == "update":
            arr = js["columnvalues"]
            myquery = { "_id": js["oldkeys"]["keyvalues"][0] }
            newvalues = { "$set": {"_id": arr[0], "first_name": arr[1], "last_name": arr[2], "sjsu_id": arr[3],
            "email" : arr[4], "create_timestamp": arr[5], "update_timestamp": arr[6] } }
            mycol.update_one(myquery, newvalues)
            return True
        elif js["kind"] == "delete":
            myquery = { "_id": js["oldkeys"]["keyvalues"][0] }
            mycol.delete_one(myquery)
            return True
        return False

myclient = None    

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_replServicer_to_server(assignmentService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    print('Hi, please enter mongo client address: \n')
    add = input ("Address: ")
    print('\nReady to replicate! \n')
    #myclient = pymongo.MongoClient("mongodb+srv://anujot:anujot@cluster0.q4kbm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    myclient = pymongo.MongoClient(add)
    logging.basicConfig()
    serve()
