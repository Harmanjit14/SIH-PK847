from python_graphql_client import GraphqlClient

# Instantiate the client with an endpoint.
client = GraphqlClient(endpoint="https://countries.trevorblades.com")

# Create the query string and variables required for the request.
query = """
    query countryQuery($countryCode: String) {
        country(code:$countryCode) {
            code
            name
        }
    }
"""
variables = {"countryCode": "CA"}

# Synchronous request
data = client.execute(query=query, variables=variables)
print(data)  # => {'data': {'country': {'code': 'CA', 'name': 'Canada'}}}
