from requests import get

my_parser = get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs').text

my_parser_split = my_parser.split('\n')
ip_addres = []
request_list = []
directory_list = []
result = []

for i in range(len(my_parser_split) - 1):
    element_split = my_parser_split[i].split(' ')
    ip_addres.append(element_split[0])
    request_list.append(element_split[5].replace('"', ''))
    directory_list.append(element_split[6])

for ip, req, dir in zip(ip_addres, request_list, directory_list):
    result.append((ip, req, dir))

with open('res.txt', 'w') as f:
    for res in result:
        f.write(str(res) + '\n')



