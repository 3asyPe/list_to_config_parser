# list_to_config_parser

Generates a config for evm and starknet automation scripts

Files you need to create in root:
- mm_keys.txt - EVM private keys
- mm_okx_addresses.txt - EVM okx addresses
- starknet_keys.txt - StarkNet private keys
- starknet_okx_addresses.txt - StarkNet okx addresses
- proxies.txt - Proxies

All files should contain the same number of lines

## Config
Create 

## Run
```
python main.py
```

Choose a mode of config-generation

For running 1 mode you will need mm_keys.txt, mm_okx_addresses, proxies.txt

For running 2 mode you will need mm_keys.txt, mm_okx_addresses, starknet_keys.txt, starknet_okx_addresses.txt

Script generate config.json file that you will need for an automation script