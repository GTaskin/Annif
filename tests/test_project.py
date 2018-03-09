"""Unit tests for projects in Annif"""

import pytest
import annif.project
import annif.backend.dummy


def test_get_project_en():
    project = annif.project.get_project('myproject-en')
    assert project.project_id == 'myproject-en'
    assert project.language == 'en'
    assert project.analyzer == 'english'
    assert len(project.backends) == 1
    assert isinstance(project.backends[0][0], annif.backend.dummy.DummyBackend)
    assert project.backends[0][1] == 0.5


def test_get_project_fi():
    project = annif.project.get_project('myproject-fi')
    assert project.project_id == 'myproject-fi'
    assert project.language == 'fi'
    assert project.analyzer == 'finnish'
    assert len(project.backends) == 1
    assert isinstance(project.backends[0][0], annif.backend.dummy.DummyBackend)
    assert project.backends[0][1] == 1.0


def test_get_project_nonexistent():
    with pytest.raises(ValueError):
        annif.project.get_project('nonexistent')
