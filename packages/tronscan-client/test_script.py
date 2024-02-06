import json
import argparse
import os
from tronscan.client import TronscanClient

def main():
    client = TronscanClient(api_key=os.environ["TRONSCAN_API_KEY"])

    # Parse console arguments (--limit and --start)
    parser = argparse.ArgumentParser(description="Fetch transactions from Tron blockchain")
    parser.add_argument("--limit", type=int, default=20, help="The number of transactions to fetch")
    parser.add_argument("--start", type=int, default=0, help="The start index of transactions to fetch")
    parser.add_argument("address", type=str, help="The address of the account to fetch transactions for")
    args = parser.parse_args()

    # print(json.dumps(client.fetch_transactions(**vars(args))))
    print(json.dumps(list(client.fetch_transfers(**vars(args)))))


if __name__ == "__main__":
    main()