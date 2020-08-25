import requests
import argparse
import sys


parser =  argparse.ArgumentParser()
parser.add_argument('-c','--code', type=str, help='the code of the quote')
parser.add_argument('-s','--start', type=str, help='the start time you want to get the data')
parser.add_argument('-e','--end', type=str, help='the end time you want to get the data')


def download(prefix, code, start, end):
    url = 'http://quotes.money.163.com/service/chddata.html?code='+prefix+code+'&start='+start+'&end='+end+'&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP'

    data = requests.get(url)

    file = open(code + '_' + start + '_' + end + '.csv', 'wb', encoding='utf-8')
    for chunk in data.iter_content(chunk_size=10000):
        if chunk:
            file.write(chunk)

    print('数据获取完成')



if __name__ == "__main__":

    args = parser.parse_args()
    prefix = ''
    if args.code[0] == '6':
        prefix = '0'
    elif args.code[0] == '0':
        prefix = '1'
    
    download(prefix, args.code, args.start, args.end)



