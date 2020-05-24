#!/bin/bash

curl -XPOST '127.0.0.1:9200/_search?pretty' -d '
{
        "size":0,
  "query": {
    "match_all": {}
  },
  "aggs":{
    "groud_by_app_name_100" :{
      "terms" :{
        "field": "app_name.raw",
    "size":10000,
    "order" : {  "_count" : "desc" },
    "min_doc_count": 10000
      },
      "aggs": {
    "type_count":{
    "cardinality":{
      "field":"user_id.raw"
    }
  }
  }
    }
  }
}'  > result.json

sed -e '/timed_out/d' result.json
