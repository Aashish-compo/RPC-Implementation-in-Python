#from urllib.request import Request
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

with SimpleXMLRPCServer(('localhost', 8000), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    print("I am listening at port 8000")

    def factorial(x):
        facts = 1
        if(x == 0):
            return 1
        elif(x == 1):
            return 1

        else:
            for i in range(1 ,  x + 1):
                facts =  facts * i
        return facts
            

    server.register_function(factorial , 'fact')
    server.serve_forever()
