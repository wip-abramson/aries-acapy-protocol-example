aca-py start \
    -it http 0.0.0.0 3000 \
    -ot http \
    -e http://0.0.0.0:3000 \
    --label BOB \
    --auto-accept-requests --auto-ping-connection \
    --auto-respond-credential-proposal --auto-respond-credential-offer --auto-respond-credential-request --auto-store-credential \
    --auto-respond-presentation-proposal --auto-respond-presentation-request --auto-verify-presentation \
    --genesis-url https://raw.githubusercontent.com/sovrin-foundation/sovrin/master/sovrin/pool_transactions_sandbox_genesis \
    --wallet-type indy \
    --debug-connections \
    --debug-credentials \
    --debug-presentations \
    --enable-undelivered-queue \
    --admin 0.0.0.0 5000 \
    --admin-insecure-mode \
    --plugin acapy_protocol_example
    "$@"
