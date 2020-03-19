# Big Data Project 1 - Open Parking and Camera Violations

Analysis on open parking and camera violation data obtained from NYC Open Data.

Sample data

```

{"plate":"GRB8570","state":"NY","license_type":"PAS","summons_number":1406780807,"issue_date":"2016-06-23","violation_time":"01:52A","violation":"NO PARKING-DAY/TIME LIMITS","fine_amount":60.0,"penalty_amount":10.0,"interest_amount":0.0,"reduction_amount":0.0,"payment_amount":70.0,"amount_due":0.0,"precinct":"067","county":"K","issuing_agency":"POLICE DEPARTMENT","summons_image":{"url":"http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VFZSUmQwNXFZelJOUkdkM1RuYzlQUT09&locationName=_____________________","description":"View Summons"}}},{"_index":"bigdata1","_type":"_doc","_id":"8662096517","_score":0.18232156,"_source":{"plate":"HAP3877","state":"NY","license_type":"PAS","summons_number":8662096517,"issue_date":"2019-05-03","violation_time":"11:42A","violation":"NO PARKING-STREET CLEANING","judgment_entry_date":"2019-08-22","fine_amount":45.0,"penalty_amount":60.0,"interest_amount":2.11,"reduction_amount":0.08,"payment_amount":107.03,"amount_due":0.0,"precinct":"040","county":"BX","issuing_agency":"TRAFFIC","summons_image":{"url":"http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VDBSWk1rMXFRVFZPYWxWNFRuYzlQUT09&locationName=_____________________","description":"View Summons"}}},{"_index":"bigdata1","_type":"_doc","_id":"8715896535","_score":0.18232156,"_source":
```

Part 2. Loading into ElasticSearch

Python code can be found in 
```
Ec.py
```
Docker command to generate data:
```
docker-compose run -e APP_TOKEN=<app_token> pyth python main.py --page_size=5 --num_pages=10 --output
=results.json --elastic_search=True
```
To demonstrate Elastic Search 

Run following command in docker
```
curl -o output.txt <docker IP>:9200/bigdata1/_search?q=state:NY&size=5
```
Open web browser for output
```
http://<docker IP>/bigdata1/_search?q=state:NY&size=10
```

Part 3. Visualization and Analysis on Kibana

Figure 1: Average Fine amount vs. County

Figure 1 shows how average fine amount are different based on 8 counties.

```
![image](https://user-images.githubusercontent.com/57785809/77029292-ae04ea00-6971-11ea-9373-ff1e84bf5643.png)
```


Figure 2: Violation count by license type

Figure 2 shows counts of violation for  6 differnet license types.


Figure 3: Count of violation 

Figure 3 shows the ratio of all 20 violations .

Figure 4: Total Fine amount vs. County

Figure 4 shows total fine amount in each counties.







