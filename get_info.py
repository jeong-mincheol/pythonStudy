
import requests
from xml.etree import ElementTree as ET
import pathlib
import pandas as pd
import multiprocessing

def get_info(symbol, startdate, enddate, path='./'):
    url = f"https://m.stock.naver.com/front-api/external/chart/domestic/notice?symbol={symbol}&startTime={startdate}&endTime={enddate}&requestType=0"

    root = ET.fromstring(requests.get(url).text)

    total = [{'date' : i.get('date'), 'information' : x.text} for i in root.iter(tag='item') for x in i]

    pathlib.Path(f"{path}").mkdir(parents=True, exist_ok=True)
    pd.DataFrame(total).to_csv(f"{path}{symbol}.csv", index=False, encoding='utf-8')

if __name__ == "__main__": # import 되면 실행되지 않는다.
    get_info('035720', '20211201', '20230120', './stock/')
    params = [('035720', '20211201', '20230120', './stock/'),
              ("000020", "20250101", "20250525", './stock/')]
    with multiprocessing.Pool(processes=6) as pool:
        pool.starmap(get_info, params)