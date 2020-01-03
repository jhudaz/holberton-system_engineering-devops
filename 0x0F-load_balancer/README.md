# 0x0F. Load balancer
---
Let’s improve our web stack so that there is redundancy for our web servers. This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.
|TASK|DESCRIPTION|
|---|---|
|0. Double the number of webservers|configure web-02 to be identical to web-01. Fortunately, you built a Bash script during your web server project|
|1. Install your load balancer |Install and configure HAproxy on your lb-01 server.|

## License

MIT