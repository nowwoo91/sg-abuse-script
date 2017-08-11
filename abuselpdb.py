import requests, json, argparse, re

def check_ip(api_key, ip, days):
    req = "https://www.abuseipdb.com/check/{0}/json?key={1}&days={2}".format(ip, api_key, days)
    #res = http.request('GET',req).json()
    res = requests.get(req,verify=False).json()
    for i in res:
        print("IP: {0} Country: {1} isoCode: {2} Category: {3} Created: {4}".format(i['ip'],i['country'],i['isoCode'],','.join(str(c) for c in i['category']),i['created']))

def report_ip(api_key, ip, cg, cm=None):
    req = "https://www.abuseipdb.com/report/json?key={0}&category={1}&comment={2}&ip={3}".format(api_key,cg,cm,ip)
    if cm:
        print('request report ip: {0} category: {1} comment: {2}'.format(ip,','.join(cg),cm))
    else:
        print('request report ip: {0} category: {1}'.format(ip,','.join(cg)))
    res = requests.get(req,verify=True).json()
    
    if res['success']:
        print('success report ip: {0}'.format(res['ip']))
    else:
        print('fail report')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--day', help="Days", default='30' ,required=False)
    #parser.add_argument('-k','--key', help="APIKeys", required=True)
    parser.add_argument('-i','--ip', help="Ip",default='8.8.8.8' ,required=False)
    parser.add_argument('-cg','--category', help="Report Category 1,2,3... etc",required=False)
    parser.add_argument('-cm','--comment', help="comment",required=False)
    parser.add_argument('--check', help="check",action="store_true")
    parser.add_argument('--report', help="report",action="store_true")

    args = parser.parse_args()
    key = "oedvorwGLJofgOeoVZda8aS5rJTqJoigo6ufUzxp"

    if args.check:
        check_ip(api_key=key,ip=args.ip,days=args.day)
    elif args.report:
        report_ip(api_key=key,ip=args.ip,cg=args.category,cm="default")
    else:
        print('use --check or --report')