from zeep import Client

# Use the WSDL URL of your server
wsdl = "http://127.0.0.1:8000/?wsdl"

# Create a client instance
client = Client(wsdl=wsdl)

# Call a SOAP method
result = client.service.add(intA=10, intB=20)
print(f"Result of addition: {result}")
