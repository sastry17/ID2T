import re
import typing as t

import Attack.ParameterTypes.BaseType as BaseType


class MACAddress(BaseType.ParameterType):

    def __init__(self):
        BaseType.ParameterType.__init__(self)
        self.name = "MACAddress"

    @staticmethod
    def validate(value: str) -> (bool, str):
        return MACAddress._is_mac_address(value), value

    @staticmethod
    def _is_mac_address(mac_address: t.Union[str, t.List[str]]) -> bool:
        """
        Verifies if the given string is a valid MAC address.
        Accepts the formats 00:80:41:ae:fd:7e and 00-80-41-ae-fd-7e.

        :param mac_address: The MAC address as string.
        :return: True if the MAC address is valid, otherwise False.
        """
        pattern = re.compile('^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$', re.MULTILINE)
        if isinstance(mac_address, list):
            for mac in mac_address:
                if re.match(pattern, mac) is None:
                    return False
        else:
            if re.match(pattern, mac_address) is None:
                return False

        return True
