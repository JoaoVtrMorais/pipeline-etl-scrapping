from .transform_raw_data import TransformRawData
from ..contracts.mocks.extract_contract import extract_contract_mock


def test_transform():
    transform_raw_data = TransformRawData()
    transform_raw_data.transform(extract_contract_mock)
    print()
