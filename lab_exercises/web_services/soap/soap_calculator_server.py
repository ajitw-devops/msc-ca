from spyne import Application, rpc, ServiceBase, Integer
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class CalculatorService(ServiceBase):
    @rpc(Integer, Integer, _returns=Integer)
    def add(ctx, intA, intB):
        return intA + intB

    @rpc(Integer, Integer, _returns=Integer)
    def subtract(ctx, intA, intB):
        return intA - intB

# Set up the application with a custom namespace
application = Application(
    [CalculatorService],
    tns="http://localhost/calculator",  # Custom namespace
    in_protocol=Soap11(validator="lxml"),
    out_protocol=Soap11(),
)

# Run the SOAP server
if __name__ == "__main__":
    from wsgiref.simple_server import make_server

    wsgi_app = WsgiApplication(application)
    server = make_server("127.0.0.1", 8000, wsgi_app)
    print("SOAP server running on http://127.0.0.1:8000")
    server.serve_forever()
