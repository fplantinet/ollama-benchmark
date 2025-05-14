import requests,json


remote_server = "https://central.brutdeflo.com"

def send_sysinfo(data_dict):
    
    json_object = json.dumps(data_dict, indent = 4)
    print(json_object)
    print('-'*10)

    url = f'{remote_server}/api/system-information'

    x = requests.post(url, data = json_object)

    return x.text 

def send_benchmark(uuid, ollama_version,data_dict):
    data_dict.update({"uuid":f"{uuid}"})
    data_dict.update({"ollama_version":f"{ollama_version}"})
    json_object = json.dumps(data_dict, indent = 4)
    print(json_object)
    print('-'*10)

    url = f'{remote_server}/api/benchmark'

    x = requests.post(url, data = json_object)

    return x.text 