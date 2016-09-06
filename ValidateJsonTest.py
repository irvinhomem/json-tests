import json
import os
from pathlib import Path

protoLabel = 'HTTPovDNS'
featureName = 'DNS-Req-Lens'

#parent_directory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
parent_directory = str(Path(os.getcwd()).parent)
print('Parent Directory: ', parent_directory)
feature_base_path = str(parent_directory + '/' + 'TunnelFeatureExtractor/feature_base/JSON/' + protoLabel + '/' +
                                featureName + '/' + featureName + '.json')
print('Feature base path:', feature_base_path)

json_file=open(feature_base_path,encoding='utf-8')

def readin():
    return json_file.read()

def parse():
    decoder = json.JSONDecoder(strict=False)
    buffer = ''
    for chunk in iter(readin, ''):
        buffer += chunk
        while buffer:
            try:
                result, index = decoder.raw_decode(buffer)
                yield result
                buffer = buffer[index:]
            except ValueError as e:
                print("1",e)
                 # Not enough data to decode, read more
                break
def parser2():
    for line in json_file:
        

def main():
    imputd=parse()

    json_data = []
    json_data.append((next(imputd)))

    print(len(json_data))
    print(json_data[0]['filename'])
    print(json_data[0]['props']['feature-name'])
    print(json_data[1]['filename'])

    output = open('output.txt', 'w')
    output.write(json.dumps(next(imputd)))

main()