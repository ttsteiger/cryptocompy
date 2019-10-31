import pytest
import datetime

from cryptocompy import helper_functions


@pytest.mark.parametrize("to_ts, timestamp", [
    ("FALSE", False),
    (datetime.datetime(2019, 5, 16, 18, 1, 48), 1558022508),
    (1558022508, 1558022508),
    ("1558022508", 1558022508),
])
def test_to_ts_args_to_timestamp(to_ts, timestamp):

    assert helper_functions.to_ts_args_to_timestamp(to_ts) == timestamp
