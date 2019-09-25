# http://multivax.com/last_question.html

"""

Modern Pythonic interface for working with MAC addresses. It provides
object-oriented facilities for address discovery, parsing, and validation.

Lightweight.
Pure-python.
Python 3.6+
asyncio-friendly? (look at pysnmp 5.0 implementation)

"EUI-48"


OUI-lookup?

from macaddress import MacAddress

mac = MacAddress()
mac.get_mac_address()
mac.get_vendor()

mac = MacAddress("00:00:00:00:00:00")
mac = MacAddress()
mac = MacAddress.get_mac_address('enp3s0')
mac = MacAddress(interface='enp3s0')

mac = MacAddress()
mac.get_mac_address('enp3s0')
str(mac)
mac.mac = "00:00:00:00:00:3C"

user_params = [...]
00-00-00-00-00-00
00:00:00:00:00:00
00.00.00.00.00.00
00:00:00:00:00:3c
00:00:00:00:00:3C

=> 00:00:00:00:00:3c

Comparison


try:
    mac = MacAddress("00:00:00:00:00:00")
except MacAddressException:
    ... bad address handling ...
else:
    ... only run when there's no exception ...
... continue on your merry way ...

"""

import logging
from functools import total_ordering
from typing import Union, Optional

from getmac import get_mac_address

log = logging.getLogger("macaddress")
log.addHandler(logging.NullHandler())


# TODO: customization of exception return attributes
class MacAddressException(Exception):
    pass


@total_ordering
class MacAddress:
    """Object representing a MAC address."""

    def __init__(self, mac_address: Optional[str] = None):
        # TODO: logging

        # TODO: accept base-10 integer values for mac address
        # TODO: hex string

        # Default to getting local interface MAC
        if mac_address is None:
            mac_address = get_mac_address()

        # TODO: integer to string

        # 74:d4:35:e9:45:73
        self.mac: str = mac_address  # Lower-case Colon-separated
        self.value: int = self.str_to_int(self.mac)

    def oui(self, mask: Union[str, int]) -> str:
        """Returns the OUI portion of the address.

        Args:
            mask: number of bits of the OUI to return as either a
            string in CIDR "slash" notation, e.g. "/24", or as a
            integer with the number of bits of the address to return.

        Returns:
             The OUI portion of the address.

        """
        # /24
        # 24
        pass

    def oui_vendor(self):
        pass

    # TODO: staticmethod?
    @classmethod
    def str_to_int(cls, mac: str) -> int:
        # Validate base length
        if len(mac) != 17:
            raise MacAddressException(
                f"Invalid length {len(mac)}for MAC address string {mac}"
            )

        # Remove separator characters
        mac = mac.replace(":", "").replace(".", "").replace("-", "")

        # Validate unseparated length
        if len(mac) != 12:
            raise MacAddressException(
                f"Invalid length {len(mac)} for "
                f"unseparated MAC address string {mac}"
            )

        # Convert to integer value as a hexadecimal number
        try:
            int_mac = int(mac, 16)
        except ValueError:
            raise MacAddressException(
                f"Failed to convert MAC address string {mac} to an integer"
            )

        # Validate address range
        if 0 <= int_mac <= 0xFFFFFFFFFFFF:
            return int_mac
        else:
            raise MacAddressException(
                f"MAC address {mac} is outside of the valid integer range"
            )

    @classmethod
    def get_mac_address(
        cls, interface=None, ip=None, ip6=None, hostname=None, network_request=True
    ) -> Optional[object]:
        mac = get_mac_address(
            interface=interface,
            ip=ip,
            ip6=ip6,
            hostname=hostname,
            network_request=network_request,
        )
        if mac is not None:
            return MacAddress(mac)
        return None

    # TODO: get vendor name => how to lookup?
    def get_vendor_name(self):
        pass

    def __hash__(self):
        pass  # TODO

    # dunder methods
    def __eq__(self, other):
        return isinstance(other, MacAddress) and self.value == other.value

    def __lt__(self, other):
        return isinstance(other, MacAddress) and self.value < other.value

    def __str__(self) -> str:
        return self.mac

    def __repr__(self) -> str:
        return f'MacAddress("{self.mac}")'


__all__ = ["MacAddress", "MacAddressException"]
