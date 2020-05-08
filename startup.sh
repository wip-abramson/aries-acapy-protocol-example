aca-py start \
    -it http 0.0.0.0 3000 \
    -ot http \
    -e http://0.0.0.0:3000 \
    --admin 0.0.0.0 5000 \
    --admin-insecure-mode \
    --plugin acapy_protocol_example
    "$@"
