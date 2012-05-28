#!/bin/bash

if [ $# -lt 4 ] ; then
    echo "$0 file ssid password [-n] printer [services [services ...]]"
    exit 1
fi

for i in FILE SSID PASSWORD ; do
    declare $i=$1
    shift
done

tshark \
    -r "$FILE" \
    -R "http.host and http.cookie" \
    -T fields -e http.host -e http.cookie \
    -o wlan.enable_decryption:TRUE \
    -o "wlan.wep_key1:wpa-pwd:$PASSWORD:$SSID" \
    | \
    ./biscuit parse "$@"
