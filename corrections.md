## docker-compose
With the integration of Docker Compose V2 into Docker's CLI the command is now "docker compose" instead of "docker-compose"

## Port 5000 already in use on Macs
Starting with MacOS Monterey Apple introduced a Control Center, which uses Port 5000. See:  
lsof -i :5000  

Solutions are for example described here: 
- https://medium.com/@inspiremeashish/port-5000-already-in-use-macos-sonama-issue-69d0adc09157
- https://twissmueller.medium.com/resolving-the-problem-of-port-5000-already-being-in-use-dd2fe4bad0be
