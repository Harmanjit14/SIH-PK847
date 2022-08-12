from python_graphql_client import GraphqlClient


class Credentials:

    token = None

    def setToken(self, token):
        self.loggedIn = True
        self.token = token

    def getToken(self):
        if self.token == None:
            return 'JWT '
        return self.token


def login(USERNAME, PASSWORD, client):

    query = """
        mutation token ($uname: String!, $pass: String!) {
        tokenAuth (username: $uname, password: $pass) {
            token
        }
        }
    """
    params = {"uname": USERNAME,
              "pass": PASSWORD,
              }

    result = client.execute(query=query, variables=params)
    token = 'JWT '
    if result['data']['tokenAuth']['token'] != None:
        token = f"JWT {result['data']['tokenAuth']['token']}"
        return token

    else:
        return token


def get_migration_certificate(client):

    query = """
    {
        migrationCertificate
    }
    """
    try:
        result = client.execute(query=query)
        if result['data']['migrationCertificate'] == 'Success':
            return "ਮੈਂ ਤੁਹਾਡਾ ਮਾਈਗ੍ਰੇਸ਼ਨ ਸਰਟੀਫਿਕੇਟ ਬਣਾਇਆ ਹੈ ਅਤੇ ਤੁਹਾਨੂੰ ਡਾਕ ਰਾਹੀਂ ਭੇਜ ਦਿੱਤਾ ਹੈ। ਕ੍ਰਿਪਾ ਜਾਂਚ ਕਰੋ"
        else:
            return "ਮਾਫ਼ ਕਰਨਾ ਮੈਂ ਤੁਹਾਡਾ ਮਾਈਗ੍ਰੇਸ਼ਨ ਸਰਟੀਫਿਕੇਟ ਬਣਾਉਣ ਵਿੱਚ ਅਸਮਰੱਥ ਸੀ"

    except:
        return "ਮਾਫ਼ ਕਰਨਾ ਮੈਂ ਤੁਹਾਨੂੰ ਲੌਗਇਨ ਕਰਨ ਵਿੱਚ ਅਸਮਰੱਥ ਸੀ"


def get_character_certificate(client):

    query = """
    {
        characterCertificate
    }
    """
    try:
        result = client.execute(query=query)
        if result['data']['characterCertificate'] == 'Success':
            return "ਮੈਂ ਤੁਹਾਡਾ ਅੱਖਰ ਸਰਟੀਫਿਕੇਟ ਬਣਾਇਆ ਹੈ ਅਤੇ ਤੁਹਾਨੂੰ ਡਾਕ ਰਾਹੀਂ ਭੇਜ ਦਿੱਤਾ ਹੈ। ਕ੍ਰਿਪਾ ਜਾਂਚ ਕਰੋ"
        else:
            return "ਮਾਫ਼ ਕਰਨਾ ਮੈਂ ਤੁਹਾਡਾ ਅੱਖਰ ਸਰਟੀਫਿਕੇਟ ਬਣਾਉਣ ਵਿੱਚ ਅਸਮਰੱਥ ਸੀ"

    except:
        return "ਮਾਫ਼ ਕਰਨਾ ਮੈਂ ਤੁਹਾਨੂੰ ਲੌਗਇਨ ਕਰਨ ਵਿੱਚ ਅਸਮਰੱਥ ਸੀ"


def get_semester_certificate(client):

    query = """
    {
        semesterCertificate(sem:1)
    }
    """
    try:
        result = client.execute(query=query)
        if result['data']['semesterCertificate'] == 'Success':
            return "ਮੈਂ ਤੁਹਾਡਾ ਸਮੈਸਟਰ ਸਰਟੀਫਿਕੇਟ ਬਣਾਇਆ ਹੈ ਅਤੇ ਤੁਹਾਨੂੰ ਡਾਕ ਰਾਹੀਂ ਭੇਜ ਦਿੱਤਾ ਹੈ। ਕ੍ਰਿਪਾ ਜਾਂਚ ਕਰੋ"
        else:
            return "ਮਾਫ਼ ਕਰਨਾ ਮੈਂ ਤੁਹਾਡਾ ਸਮੈਸਟਰ ਸਰਟੀਫਿਕੇਟ ਬਣਾਉਣ ਵਿੱਚ ਅਸਮਰੱਥ ਸੀ"

    except:
        return "ਮਾਫ਼ ਕਰਨਾ ਮੈਂ ਤੁਹਾਨੂੰ ਲੌਗਇਨ ਕਰਨ ਵਿੱਚ ਅਸਮਰੱਥ ਸੀ"


def get_domicile_certificate(client):

    query = """
    {
        domicileCertificate
    }
    """
    try:
        result = client.execute(query=query)
        if result['data']['domicileCertificate'] == 'Success':
            return "ਮੈਂ ਤੁਹਾਡਾ ਨਿਵਾਸ ਸਰਟੀਫਿਕੇਟ ਬਣਾਇਆ ਹੈ ਅਤੇ ਤੁਹਾਨੂੰ ਡਾਕ ਰਾਹੀਂ ਭੇਜ ਦਿੱਤਾ ਹੈ। ਕ੍ਰਿਪਾ ਜਾਂਚ ਕਰੋ"
        else:
            return "ਮਾਫ਼ ਕਰਨਾ ਮੈਂ ਤੁਹਾਡਾ ਨਿਵਾਸ ਸਰਟੀਫਿਕੇਟ ਬਣਾਉਣ ਵਿੱਚ ਅਸਮਰੱਥ ਸੀ"

    except:
        return "ਮਾਫ਼ ਕਰਨਾ ਮੈਂ ਤੁਹਾਨੂੰ ਲੌਗਇਨ ਕਰਨ ਵਿੱਚ ਅਸਮਰੱਥ ਸੀ"


def get_affidavit(client):

    query = """
    {
        affidavit
    }
    """
    try:
        result = client.execute(query=query)
        if result['data']['affidavit'] == 'Success':
            return "ਮੈਂ ਤੁਹਾਡਾ ਹਲਫੀਆ ਬਿਆਨ ਬਣਾਇਆ ਹੈ ਅਤੇ ਤੁਹਾਨੂੰ ਡਾਕ ਰਾਹੀਂ ਭੇਜ ਦਿੱਤਾ ਹੈ। ਕ੍ਰਿਪਾ ਜਾਂਚ ਕਰੋ"
        else:
            return "ਮਾਫ਼ ਕਰਨਾ ਮੈਂ ਤੁਹਾਡਾ ਹਲਫੀਆ ਬਿਆਨ ਬਣਾਉਣ ਵਿੱਚ ਅਸਮਰੱਥ ਸੀ"

    except:
        return "ਮਾਫ਼ ਕਰਨਾ ਮੈਂ ਤੁਹਾਨੂੰ ਲੌਗਇਨ ਕਰਨ ਵਿੱਚ ਅਸਮਰੱਥ ਸੀ"


def get_institute_info(client):

    query = """
    {
        instituteInformation
    }
    """
    try:
        result = client.execute(query=query)
        if result['data']['instituteInformation'] == 'Success':
            return "ਮੈਂ ਸੰਸਥਾ ਦੀ ਉਹ ਜਾਣਕਾਰੀ ਦੇ ਦਿੱਤੀ ਹੈ ਜੋ ਤੁਸੀਂ ਮੰਗੀ ਸੀ"
        else:
            return "ਮਾਫ਼ ਕਰਨਾ ਪਰ ਮੈਂ ਤੁਹਾਨੂੰ ਸੰਸਥਾ ਦੀ ਜਾਣਕਾਰੀ ਨਹੀਂ ਦੇ ਸਕਦਾ"

    except:
        return "ਮਾਫ਼ ਕਰਨਾ ਮੈਂ ਤੁਹਾਨੂੰ ਲੌਗਇਨ ਕਰਨ ਵਿੱਚ ਅਸਮਰੱਥ ਸੀ"


def get_institute_events_info(client):

    query = """
    {
        instituteEventsInformation
    }
    """
    try:
        result = client.execute(query=query)
        if result['data']['instituteEventsInformation'] == 'Success':
            return "ਮੈਂ ਸੰਸਥਾ ਦੇ ਸਮਾਗਮਾਂ ਬਾਰੇ ਜਾਣਕਾਰੀ ਦੇ ਦਿੱਤੀ ਹੈ ਜੋ ਤੁਸੀਂ ਮੰਗੀ ਸੀ"
        else:
            return "ਮਾਫ਼ ਕਰਨਾ ਪਰ ਮੈਂ ਤੁਹਾਨੂੰ ਇੰਸਟੀਚਿਊਟ ਦੇ ਸਮਾਗਮਾਂ ਬਾਰੇ ਜਾਣਕਾਰੀ ਨਹੀਂ ਦੇ ਸਕਦਾ"

    except:
        return "ਮਾਫ਼ ਕਰਨਾ ਮੈਂ ਤੁਹਾਨੂੰ ਲੌਗਇਨ ਕਰਨ ਵਿੱਚ ਅਸਮਰੱਥ ਸੀ"


def case_selector(id, obj):

    # Server Connection
    server_client = GraphqlClient(endpoint="http://localhost:8000/graphql", headers={
        'Authorization': obj.token,
    })

    if id == -1:
        uname = str(input("Enter Username: "))
        upass = str(input("Enter Password: "))
        token = login(uname, upass, server_client)
        if len(token) > 3:
            obj.setToken(token)
            return True
        return False
    if id == 1:
        return get_migration_certificate(server_client)
    elif id == 2:
        return get_character_certificate(server_client)
    elif id == 3:
        return get_semester_certificate(server_client)
    elif id == 4:
        return get_domicile_certificate(server_client)
    elif id == 5:
        return get_affidavit(server_client)
    elif id == 6:
        return get_institute_info(server_client)
    elif id == 7:
        return get_institute_events_info(server_client)

