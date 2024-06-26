# Copyright 2024 The Wordcab Team. All rights reserved.
#
# Licensed under the MIT License (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://github.com/Wordcab/wordcab-transcribe/blob/main/LICENSE
#
# Except as expressly provided otherwise herein, and to the fullest
# extent permitted by law, Licensor provides the Software (and each
# Contributor provides its Contributions) AS IS, and Licensor
# disclaims all warranties or guarantees of any kind, express or
# implied, whether arising under any law or from any usage in trade,
# or otherwise including but not limited to the implied warranties
# of merchantability, non-infringement, quiet enjoyment, fitness
# for a particular purpose, or otherwise.
#
# See the License for the specific language governing permissions
# and limitations under the License.
"""Test config settings."""

from collections import OrderedDict

import pytest

from wordcab_transcribe import __version__
from wordcab_transcribe.config import Settings, settings


@pytest.fixture
def default_settings() -> OrderedDict:
    """Return the default settings."""
    return OrderedDict(
        project_name="Wordcab Transcribe",
        version=__version__,
        description=(
            "💬 ASR FastAPI server using faster-whisper and Auto-Tuning Spectral"
            " Clustering for diarization."
        ),
        api_prefix="/api/v1",
        debug=True,
        whisper_model="large-v2",
        compute_type="float16",
        extra_languages=["he"],
        extra_languages_model_paths={"he": "path/to/model"},
        window_lengths=[1.5, 1.25, 1.0, 0.75, 0.5],
        shift_lengths=[0.75, 0.625, 0.5, 0.375, 0.25],
        multiscale_weights=[1.0, 1.0, 1.0, 1.0, 1.0],
        asr_type="async",
        cortex_endpoint=True,
        username="admin",
        password="admin",
        openssl_key="0123456789abcdefghijklmnopqrstuvwyz",
        openssl_algorithm="HS256",
        access_token_expire_minutes=30,
        cortex_api_key="",
        svix_api_key="",
        svix_app_id="",
    )


def test_config() -> None:
    """Test default config settings with the .env file."""
    assert settings.project_name == "Wordcab Transcribe"
    assert settings.version == __version__
    assert (
        settings.description
        == "💬 ASR FastAPI server using faster-whisper and Auto-Tuning Spectral"
        " Clustering for diarization."
    )
    assert settings.api_prefix == "/api/v1"
    assert settings.debug is True

    assert settings.whisper_model == "large-v2"
    assert settings.compute_type == "float16"
    assert settings.extra_languages is None
    assert settings.extra_languages_model_paths is None

    assert settings.window_lengths == [1.5, 1.25, 1.0, 0.75, 0.5]
    assert settings.shift_lengths == [0.75, 0.625, 0.5, 0.375, 0.25]
    assert settings.multiscale_weights == [1.0, 1.0, 1.0, 1.0, 1.0]

    assert settings.asr_type == "async"
    assert settings.cortex_endpoint is True

    assert settings.username == "admin"  # noqa: S105
    assert settings.password == "admin"  # noqa: S105
    assert settings.openssl_key == "0123456789abcdefghijklmnopqrstuvwyz"  # noqa: S105
    assert settings.openssl_algorithm == "HS256"
    assert settings.access_token_expire_minutes == 30

    assert settings.cortex_api_key == ""
    assert settings.svix_api_key == ""
    assert settings.svix_app_id == ""


def test_general_parameters_validator(default_settings: dict) -> None:
    """Test general parameters validator."""
    wrong_project_name = default_settings.copy()
    wrong_project_name["project_name"] = None
    with pytest.raises(ValueError):
        Settings(**wrong_project_name)

    wrong_version = default_settings.copy()
    wrong_version["version"] = None
    with pytest.raises(ValueError):
        Settings(**wrong_version)

    wrong_description = default_settings.copy()
    wrong_description["description"] = None
    with pytest.raises(ValueError):
        Settings(**wrong_description)

    wrong_api_prefix = default_settings.copy()
    wrong_api_prefix["api_prefix"] = None
    with pytest.raises(ValueError):
        Settings(**wrong_api_prefix)


def test_compute_type_validator(default_settings: dict) -> None:
    """Test compute type validator."""
    default_settings["compute_type"] = "invalid_compute_type"
    with pytest.raises(ValueError):
        Settings(**default_settings)


def test_asr_type_validator(default_settings: dict) -> None:
    """Test asr type validator."""
    default_settings["asr_type"] = "invalid_asr_type"
    with pytest.raises(ValueError):
        Settings(**default_settings)


def test_openssl_algorithm_validator(default_settings: dict) -> None:
    """Test openssl algorithm validator."""
    default_settings["openssl_algorithm"] = "invalid_algorithm"
    with pytest.raises(ValueError):
        Settings(**default_settings)


def test_access_token_expire_minutes_validator(default_settings: dict) -> None:
    """Test access token expire minutes validator."""
    default_settings["access_token_expire_minutes"] = -1
    with pytest.raises(ValueError):
        Settings(**default_settings)
