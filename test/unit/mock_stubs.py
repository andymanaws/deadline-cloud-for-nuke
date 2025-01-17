# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.

from typing import Any, Dict


class MockKnob:
    """Mock class which emulates the Nuke Knob"""

    _value: Any
    __name__ = "Knob"

    def __init__(self, value: Any):
        self._value = value

    def value(self) -> Any:
        return self._value

    def getEvaluatedValue(self) -> Any:
        return self._value

    def setValue(self, value):
        self._value = value
        return True


class MockNode:
    """Mock class which emulates the Nuke Node"""

    _knobs: Dict[str, MockKnob]
    _name: str = ""
    _class: str = ""
    __name__ = "Node"

    def __init__(self, name, knobs, class_name) -> None:
        self._name = name
        self._knobs = knobs
        self._class = class_name

    def name(self) -> str:
        return self._name

    def knobs(self) -> Dict[str, MockKnob]:
        return self._knobs

    def knob(self, name) -> Any:
        return self._knobs.get(name)

    def Class(self) -> str:
        return self._class


class MockOCIOConfig:
    """Mock class which emulates an OCIO Config"""

    __name__ = "Config"

    def __init__(self, working_dir: str, search_paths: list[str]):
        self._working_dir = working_dir
        self._search_paths = search_paths
        self._serialize_path = ""

    def getWorkingDir(self) -> str:
        return self._working_dir

    def getSearchPaths(self) -> list[str]:
        return self._search_paths

    def clearSearchPaths(self) -> None:
        self._search_paths = []

    def addSearchPath(self, search_path: str) -> None:
        self._search_paths.append(search_path)

    def serialize(self, file_path: str) -> None:
        self._serialize_path = file_path
