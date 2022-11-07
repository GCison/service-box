import json, requests

class Projecao:

    def __init__(self, uri):
        self.uri = uri
        
    def get_projecao_api_ibge(self):
        response = resquests.get(self.uri)
        data = json.loads(response.text)
        projecao = data['projecao']
        result = projecao['populacao']
        writer_data(str(result))

    def writer_data(value):
        arq = open("data.txt", 'w')
        arq.write(value)
        arq.close()

get_projecao_api_ibge()