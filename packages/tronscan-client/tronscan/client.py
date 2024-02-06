import requests
from dataclasses import dataclass


@dataclass
class Token:
    """
    Data class representing a TRC20 token.
    """
    name: str
    symbol: str
    decimals: int
    address: str


class TronscanClient:
    """
    Class which implements Tronscan API.
    """
    api_key: str
    base_url: str

    def __init__(
        self,
        api_key: str,
        base_url: str = "https://apilist.tronscanapi.com/api/",
    ):
        self.api_key = api_key
        self.base_url = base_url
    
    def _auth_headers(self):
        """
        Return the authentication headers for the Tronscan API.
        """
        return {
            "TRON-PRO-API-KEY": self.api_key,
        }

    def fetch_transactions(
        self,
        address: str,
        start: int = 0,
        limit: int = 20,
    ):
        """
        Fetch a list of transactions related to the given account on Tron blockchain.

        :param account_address: The address of the account to fetch transactions for.
        :return: A list of transactions associated with the given account.
        """
        endpoint = f"/transaction?sort=-timestamp&count=true&limit={limit}&start={start}&address={address}"

        try:
            response = requests.get(self.base_url + endpoint, headers=self._auth_headers())
            response.raise_for_status()  # Raise an HTTPError for bad responses

            # Parse the JSON response
            transactions = response.json()

            return transactions.get('data', [])
        except requests.RequestException as e:
            print(f"Error fetching transactions: {e}")
            return []
            
    def fetch_transfers(
        self,
        address: str,
        start: int = 0,
        limit: int = 20,
    ):
        """
        Fetch a list of TRC20 transfers related to the given account on Tron blockchain
        """
        endpoint = f"/token_trc20/transfers?sort=-timestamp&limit={limit}&start={start}&relatedAddress={address}"

        try:
            response = requests.get(self.base_url + endpoint, headers=self._auth_headers())
            response.raise_for_status()  # Raise an HTTPError for bad responses

            # Parse the JSON response
            transactions = response.json()

            return transactions.get('token_transfers', [])
        except requests.RequestException as e:
            print(f"Error fetching transfers: {e}")
            return []

    def all_transactions(self, address: str):
        """
        Fetch all transactions related to the given account on Tron blockchain.

        :param account_address: The address of the account to fetch transactions for.
        :return: A generator of all transactions associated with the given account.
        """
        start = 0
        limit = 20

        while True:
            transactions = self.fetch_transactions(address, start, limit)
            yield from transactions
            if len(transactions) < limit:
                break
            start += limit