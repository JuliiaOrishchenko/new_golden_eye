import xml.etree.ElementTree as ET

import requests

from api import _Api


class Api(_Api):
    def __init__(self):
        super().__init__("CbrApi")

    def _update_rate(self, xrate):
        rate = self._get_cbr_rate(xrate.from_currency)
        return rate

    def _get_cbr_rate(self, from_currency):
        response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
        response.encoding = 'windows-1251'
        self.log.debug("response.encoding: %s" % response.encoding)
        response_content = response.content
        self.log.debug("response.text: %s" % response_content)
        rate = self._find_rate(response_content, from_currency)

        return rate


    def _find_rate(self, response_content, from_currency):
        tree = ET.fromstring(response_content)
        root = ET.ElementTree(ET.fromstring(response_content)).getroot()

        cbr_valute_map = {840:"USD"}
        currency_cbr_alias = cbr_valute_map[from_currency]

        for valute in root.findall(".//Valute/[CharCode='" + currency_cbr_alias + "']"):
            return float(valute.find("Value").text.replace(",", "."))

