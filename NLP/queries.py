from gql import gql

async def login(USERNAME, PASSWORD, client):

    query = gql(
        """
        mutation token ($uname: String!, $pass: String!) {
        tokenAuth (username: $uname, password: $pass) {
            token
        }
        }
    """
    )
    params = {"uname": USERNAME,
             "pass": PASSWORD,
             }
    # Get name of continent with code "EU"
    result =await client.execute(query, variable_values=params)
    print(result)
