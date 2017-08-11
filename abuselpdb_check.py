import requests, json, argparse, re, csv, os
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def check_ip(api_key, ip, days=30):
    req = "https://www.abuseipdb.com/check/{0}/json?key={1}&days={2}".format(ip, api_key, days)
    #res = http.request('GET',req).json()
    res = requests.get(req,verify=False).json()
    for i in res:
        print("IP: {0} Country: {1} isoCode: {2} Category: {3} Created: {4}".format(i['ip'],i['country'],i['isoCode'],','.join(str(c) for c in i['category']),i['created']))

    return res

def write_csv(path, datas):
    with open(path, 'w') as csvfile:
        fieldnames = ['ip', 'country', 'isoCode', 'category', 'created']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for data in datas:
            for row in data:
                writer.writerow(
                    {'ip': row['ip'], 
                    'country': row['country'], 
                    'isoCode' : row['isoCode'], 
                    'category': ','.join(str(c) for c in row['category']), 
                    'created': row['created']
                    }
                )

    print('csv write complete')

def read_csv(path):   
    with open(path,'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            yield row

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # for check
    parser.add_argument('-k','--key', help="APIKeys", default=None ,required=False)
    parser.add_argument('-s','--source', help="ip list file path",default='check_ip.csv')
    parser.add_argument('-r','--result', help="check result file path",default='check_result.csv')
    parser.add_argument('--check', help="check",default=True,action="store_true")

    args = parser.parse_args()
    if not args.key:
        key = "oedvorwGLJofgOeoVZda8aS5rJTqJoigo6ufUzxp"

    datas=[]
    if args.check:
        for row in read_csv(args.source):
            datas.append(check_ip(api_key=key,ip=row['ip']))
        write_csv(args.result, datas)