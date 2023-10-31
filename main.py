import json


def load_files(mode):
    values = []
    if mode == 1:
        file_names = ["mm_keys.txt", "mm_okx_addresses.txt", "proxies.txt"]
    else:
        file_names = [
            "mm_keys.txt",
            "mm_okx_addresses.txt",
            "starknet_keys.txt",
            "starknet_okx_addresses.txt",
        ]

    for file_name in file_names:
        with open(file_name) as f:
            lines = f.readlines()
            values.append([line.strip() for line in lines])

    return values


def divide_list(lst, n):
    # Calculate the size of each chunk
    chunk_size = len(lst) // n
    # Calculate the number of chunks that will have an extra element
    remainder = len(lst) % n

    chunks = []
    start = 0
    for i in range(n):
        # If this chunk should have an extra element
        if i < remainder:
            end = start + chunk_size + 1
        else:
            end = start + chunk_size
        chunks.append(lst[start:end])
        start = end
    return chunks


def main(num_of_groups):
    mode = int(input("Enter mode (1 for EVM, 2 for EVM + starknet): "))
    if mode != 1 and mode != 2:
        print("Invalid mode")
        return

    values = list(zip(*load_files(mode)))

    if mode == 1:
        accounts = [
            {"mm_private_key": key, "okx_address": okx_address, "proxy": proxy}
            for key, okx_address, proxy in values
        ]
    else:
        accounts = [
            {
                "mm_private_key": mm_key,
                "mm_okx_address": mm_okx_address,
                "starknet_private_key": starknet_key,
                "starknet_okx_address": starknet_okx_address,
            }
            for mm_key, mm_okx_address, starknet_key, starknet_okx_address in values
        ]

    chunks = divide_list(accounts, num_of_groups)

    config_dict = {
        "groups": [chunk for chunk in chunks],
        "okx_credentials": {"apikey": "", "apisecret": "", "passphrase": ""},
    }

    with open("config.json", "w") as config:
        json.dump(config_dict, config)


if __name__ == "__main__":
    num_of_groups = int(input("Enter number of groups: "))
    main(num_of_groups)
