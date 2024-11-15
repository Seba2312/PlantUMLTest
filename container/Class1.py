from dataclasses import dataclass
from typing import List

from container.Class2 import UmlItem


@dataclass
class UmlAttribute:
    name: str
    type: str
    static: bool


@dataclass
class UmlClass(UmlItem):
    attributes: List[UmlAttribute]
    is_abstract: bool = False
