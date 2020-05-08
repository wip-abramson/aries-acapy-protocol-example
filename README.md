# Aries aca-py Protocol Example

This is a basic example of a protocol implemented for an aca-py agent and included as a plugin.

To startup run

```
git clone https://github.com/wip-abramson/aries-acapy-protocol-example

cd aries-acapy-protocol-example

python3 -m venv env

source env/bin/activate

pip install -e .

aca-py start -it http localhost 3000 -it ws localhost 3001 -ot http -e http://localhost:3000 ws://localhost:3001  --admin 0.0.0.0 5000 --admin-insecure-mode --plugin aries_protocol_example.protocolexample
```

Alternatively you can use docker and docker-compose, if you have these installed just run `docker-compose up`

Once the agent has started you should be able to navigate to the swagger interface and see the protocol that is included through the plugin. It should expose an api endpoint /connections/{conn_id}/test-protocolexample
