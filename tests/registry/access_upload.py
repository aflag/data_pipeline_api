from hashlib import sha1

import pytest

from data_pipeline_api.registry.access_upload import _verify_hash


@pytest.fixture()
def tmp_file_calculated_hash(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "test.txt"
    p.write_text("some content in a file")
    return p


@pytest.fixture()
def calculated_hash(tmp_file_calculated_hash):
    with open(tmp_file_calculated_hash, "rb") as f:
        return sha1(f.read()).hexdigest()


def test_verify_hash(tmp_file_calculated_hash, calculated_hash):
    _verify_hash(tmp_file_calculated_hash, calculated_hash)
    with pytest.raises(ValueError):
        _verify_hash(tmp_file_calculated_hash, "somemadeuphash")
