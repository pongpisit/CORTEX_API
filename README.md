# PANW_CortexAPI_GetEndpoint

Usages

0. Change all the APIs and Tenant Url

1. python3 Cortex_API_Endpoint_Lists.py > ip.txt

2. Use python3 host simple web server. python3 -m http.server

3. Configure NGFW EDL then point to http://xxx.xxx.xxx.xx/ip.txt

4. Create cronjob to run python script every 5 mins to delete ip.txt then get new ip.txt
