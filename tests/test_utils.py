import pytest

from core.utils import camel_to_snake


@pytest.mark.parametrize(
    "camel, expected_snake",
    [
        ("CamelCase", "camel_case"),
        ("OrderProductAssociation", "order_product_association"),
        ("Test", "test"),
        ("HTTPResponseCode", "http_response_code"),
        ("XMLParser", "xml_parser"),
        ("SomeXMLAndHTTPStuff", "some_xml_and_http_stuff"),
    ],
)
def test_camel_to_snake(camel: str, expected_snake: str):
    assert camel_to_snake(camel) == expected_snake
