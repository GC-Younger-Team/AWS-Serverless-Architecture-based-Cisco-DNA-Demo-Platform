from datetime import  datetime
from elasticsearch import Elasticsearch
import time
import datetime
import sys
import json
import urllib
import re
import time
import math
es = Elasticsearch(
      hosts="https://search-dna-demo-elk-emox6tzojntmmdalqg5ryedlfi.cn-north-1.es.amazonaws.com.cn",
      http_auth=('dna-demo', 'C1sco@123'),
      scheme="https",
      port=443,
)
response = es.search(
    index="webhook",  # 索引名
    body={  # 请求体
        "_source": {"includes": ["eventId","details.Device","@timestamp","details.Assurance Issue Priority"]},
        "query": {  # 关键字，把查询语句给 query
            "bool": {  # 关键字，表示使用 filter 查询，没有匹配度
                "must":
                    {"term": {"domain.keyword": "Know Your Network"}}
        }
                },

    }
)

def get_elk_data(event,context):
    doc = response['hits']['hits']
    if len(doc):
        for item in doc:
            print(item['_source'])







