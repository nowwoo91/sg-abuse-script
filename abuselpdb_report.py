import requests, json, argparse, re, csv
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def check_ip(api_key, ip, days):
    req = "https://www.abuseipdb.com/check/{0}/json?key={1}&days={2}".format(ip, api_key, days)
    #res = http.request('GET',req).json()
    res = requests.get(req,verify=False).json()
    for i in res:
        print("IP: {0} Country: {1} isoCode: {2} Category: {3} Created: {4}".format(i['ip'],i['country'],i['isoCode'],','.join(str(c) for c in i['category']),i['created']))

def report_ip(api_key, ip, cg=None, cm=None):
    if not cm or cm=='':
        cm = 'sg_cert_report'
    if not cg or cg=='':
        cg = '3,4,9,10,11,14,18,19,20,21,22,23'
    req = "https://www.abuseipdb.com/report/json?key={0}&category={1}&comment={2}&ip={3}".format(api_key,cg,cm,ip)
    print('request report ip: {0} category: {1} comment: {2}'.format(ip,cg,cm))
    res = requests.get(req,verify=False).json()
    try:
        if res['success']:
            print('success report ip: {0}'.format(res['ip']))
    except TypeError as e:
        print('fail[{0}] report ip: {1} {2}'.format(res[0]['status'],ip,res[0]['meta']))


def read_csv(path):   
    with open(path,'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            yield row

def parse_category(category):
    if category == '':
        return
    ct_result = []
    ct_list = ['3','4','9','10','11','14','18','19','20','21','22','23']
    ct_dict = {
        'fraud orders' :'3',
        'ddos attack': '4',
        'open proxy' : '9',
        'web spam' : '10',
        'email spam' : '11',
        'port scan' : '14',
        'brute-force' : '18',
        'bad web bot':'19',
        'exploited host' : '20',
        'web app attack' : '21',
        'ssh' : '22',
        'iot targeted' : '23'
    }
    
    
    ct_list = category.split(',')
    for ct in ct_list:
        ct=ct.strip()
        ct=ct.lower()
        if ct.isdigit():
            if ct in ct_list:
                ct_result.append(ct)
            else:
                print('number error category number is {0} '.format(ct_list))
        elif ct in ct_dict:
            
            ct_result.append(ct_dict[ct])      
        else:
            print('category error category name is\n{0}'.format(ct_dict.keys()))

    return ','.join(ct_result)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # for check
    parser.add_argument('-k','--key', help="APIKeys", default=None ,required=False)
    parser.add_argument('-f','--file', help="ip list file path",default='report_ip.csv')
    parser.add_argument('--report', help="report",default=True,action="store_true")

    args = parser.parse_args()
    if not args.key:
        key = "oedvorwGLJofgOeoVZda8aS5rJTqJoigo6ufUzxp"

    if args.report:
        for row in read_csv(args.file):
            row['category']=parse_category(row['category'])
            report_ip(api_key=key,ip=row['ip'],cg=row['category'],cm=row['comment'])