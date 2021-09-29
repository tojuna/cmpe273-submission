import logging
import grpc
import psycopg2
import replicator_pb2_grpc as pb2_grpc
import replicator_pb2 as pb2
import json

class UnaryClient():

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = pb2_grpc.replStub(self.channel)

    def get_url(self, message):
        """
        Client function to call the rpc for GetServerResponse
        """
        message = pb2.dml(message=message)
        return self.stub.query(message)


def get_data(client, username, pwd, host, port):
    conn = None
    try:
        conn = psycopg2.connect(
        #database='college', user='postgres', password='anujot', host='127.0.0.1', port= '5432'
        database='college', user=username, password=pwd, host=host, port= port
        )
        print ("Connected")
    except: 
        print ("Could not open database")
        return
    cur = conn.cursor()
    try:
        cur.execute("SELECT 'init' FROM pg_create_logical_replication_slot('slot000', 'wal2json')")
        print('\nslot initialized')
    except: 
        print('\nslot was already present or was not initialized')
        cur.execute("ROLLBACK")
    print('\nReady to replicate!\n')
    while True:
        cur.execute("SELECT data FROM pg_logical_slot_get_changes('slot000', NULL, NULL)")
        rows_count = cur.rowcount
        if rows_count > 0: 
            while True:
                row = cur.fetchone()
                if not row:
                    break
                js = json.loads(''.join(row))
                i = 0
                while True:
                    try:
                        result = client.get_url(json.dumps(js["change"][i]))
                        print(result)
                    except: break
                    i += 1
       

if __name__ == '__main__':
    client = UnaryClient()
    print('Hi, please enter username, password, host, and port number: \n')
    username = input ("Enter username: ")
    pwd = input ("Enter password: ")
    host = input ("Enter host: ")
    port = input ("Enter port: ")
    get_data(client, username, pwd, host, port)
