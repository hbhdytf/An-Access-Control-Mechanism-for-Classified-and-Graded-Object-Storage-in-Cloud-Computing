#!/bin/bash
for x in {1..300}
do
     curl -X DELETE -H 'X-Auth-Token: AUTH_tk3694c0f33a1e4ae8a5a0ffd0e33012b4' http://127.0.0.1:8080/v1/AUTH_mac/ytf13/13ytf$x.mp3
done

