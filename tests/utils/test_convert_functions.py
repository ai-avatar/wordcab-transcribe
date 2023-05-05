# Copyright 2023 The Wordcab Team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests the conversion functions."""
import pytest

from typing import Union
from wordcab_transcribe.utils import (
    convert_timestamp,
    _convert_ms_to_hms,
    _convert_ms_to_s,
)

@pytest.mark.parametrize("timestamp, target, expected", [
    (1000, "ms", 1000),
    (1000, "s", 1),
    (1000, "hms", "00:00:01.000"),
    (3600000, "hms", "01:00:00.000"),
    (3661000, "hms", "01:01:01.000")
])
def test_convert_timestamp(timestamp: float, target: str, expected: Union[str, float]) -> None:
    """Test the convert_timestamp function."""
    assert convert_timestamp(timestamp, target) == expected


def test_convert_timestamp_raises_error() -> None:
    with pytest.raises(ValueError):
        convert_timestamp(1000, "invalid_target")


@pytest.mark.parametrize("ms, expected", [
    (1000, 1),
    (3600000, 3600),
    (3661000, 3661)
])
def test_convert_ms_to_s(ms: float, expected: float) -> None:
    """Test the _convert_ms_to_s function."""
    assert _convert_ms_to_s(ms) == expected


@pytest.mark.parametrize("ms, expected", [
    (1000, "00:00:01.000"),
    (3600000, "01:00:00.000"),
    (3661000, "01:01:01.000")
])
def test_convert_ms_to_hms(ms: float, expected: str) -> None:
    """Test the _convert_ms_to_hms function."""
    assert _convert_ms_to_hms(ms) == expected
