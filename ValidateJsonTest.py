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
def parser1():
    data = []
    with open(feature_base_path) as f:
        for line in f:
            data.append(json.loads(line))

    print("Length of Data", len(data))


def parser2():
    for line in json_file:
        yield json.loads(line)

def parser3():
    json_obj_list = []
    for line in json_file:
        try:
            json_obj_list.append(json.loads(line))
        except json.decoder.JSONDecodeError:
            pass

    return json_obj_list

def parser3_1():
    json_obj_list = []
    delimiters = ["{", "}", "[", "]", ","]
    open_brace = 0
    close_brace = 0
    #for count, line in enumerate(json_file):
    json_obj_str = ''
    for line in json_file:
        # if count < 6:
        #     print("Line: ", line)
        #     print("Start-strip: ", line.strip()[0:2])
        #     print("End-strip: ", line.strip()[-2:])

        if '{' in line.strip()[0:2] or '{' in line.strip()[-2:]:
            print("OpenBrace line: ", line.strip())
            open_brace += 1
            print("Open BRACE count: ", open_brace)
        if '}' in line.strip()[0:2] or '}' in line.strip()[-2:]:
            print("CloseBrace line: ", line.strip())
            close_brace += 1
            print("Close BRACE count: ", close_brace)
        if open_brace > close_brace:
            json_obj_str = json_obj_str + line
            #print("JSON str len: ", len(json_obj_str))
        #elif open_brace == close_brace:
        else:
            #try:
            json_obj_in_braces = json_obj_str[0:json_obj_str.rfind('}')]
            print("End of JSON Object: ", json_obj_in_braces[-3:])
            json_obj_list.append(json.load(json_obj_in_braces))
            print("Added Json obj to list")
            open_brace = 0
            close_brace = 0
            json_obj_str = ''

        # try:
        #     # json_obj_list.append(json.loads(line))
        #     json.loads(line)
        # except json.decoder.JSONDecodeError:
        #     pass
    print("Open Braces total: ", open_brace)
    print("Close Braces total: ", close_brace)
    print("JSON obj list len: ", len(json_obj_list))

    return json_obj_list

def parser4():
    json_obj_list = []
    with open(feature_base_path) as my_json_file:
        print("Parser4: Opened file: ", feature_base_path)
        try:
            my_obj = json.load(my_json_file)
            print("my_obj type: ", type(my_obj))
            json_obj_list.append(my_obj)
        except json.decoder.JSONDecodeError:
            print("Hit --> JSON decode error")
            pass
    return json_obj_list

def parser5():
    jfile = None
    with open(feature_base_path) as f:
        for line in f:
            while True:
                try:
                    jfile = json.loads(line)
                    break
                except ValueError:
                    # Not yet a complete JSON value
                    line += next(f)
                # except json.decoder.JSONDecodeError:
                #     line += next(f)

        print("Type: ", type(jfile))
        print("Length: ", len(jfile))
        print("JSON obj 1: ", jfile[0])
        print("JSON obj 2: ", jfile[1])
        # do something with jfile

def parser6():
    with open(feature_base_path) as my_json_file:
        json_objs = json.load(my_json_file)

    print("JSON objects list len: ", len(json_objs))
    print("JSON obj 1: ", json_objs[0]['filename'])
    print("JSON obj 1: ", json_objs[0]['protocol'])
    print("JSON obj 1: ", json_objs[0]['props']['feature-name'])
    print("JSON obj 1: ", json_objs[0]['props']['values'][0])
    print("JSON obj 1: ", json_objs[0]['props']['values'][7])

    print("JSON obj 1: ", json_objs[1]['filename'])
    print("JSON obj 1: ", json_objs[1]['protocol'])
    print("JSON obj 1: ", json_objs[1]['props']['feature-name'])
    print("JSON obj 1: ", json_objs[1]['props']['values'][0])
    print("JSON obj 1: ", json_objs[1]['props']['values'][7])

def main():

    parser6()

# ===========================
    # TESTING parser1
    # parser1()

# ===========================
    # TESTING parser5  <---- Somewhat works with comma separated json array from a python list
    # parser5()

# ===========================
    # TESTING parser 3
    # parser3_1()

# ===========================
    # TESTING parser 4  <----- Gets only first object, but no errors
    # json_objs = parser4()
    # print('Json list size: ', len(json_objs))
    # print("JSON obj 1: ", json_objs[0])

# ============================
    # TESTING parser3   <------ Not sure what out put this is
    # json_objs = parser3()
    # print('Json list size: ', len(json_objs))
    # print(str(type(json_objs[0])))
    # print(str(json_objs[0]))
    # print(str(json_objs[1]))
    # print(str(json_objs[0]['filename']))

# ===========================
    # TESTING parser2
    #data = parser2()
    #print(data)

    # json_data_objs = []
    # json_data_objs.append(parser2())
    # json_data_objs = list(parser2())
    #
    # print("JSON objects #: ", len(json_data_objs))
    # print(json_data_objs[0]['filename'])

# ==========================
    # ORIGINAL CODE:

    # imputd=parse()
    #
    # json_data = []
    # json_data.append((next(imputd)))
    #
    # print(len(json_data))
    # print(json_data[0]['filename'])
    # print(json_data[0]['props']['feature-name'])
    # print(json_data[1]['filename'])
    #
    # output = open('output.txt', 'w')
    # output.write(json.dumps(next(imputd)))

main()