#  Copyright 2025 Patrick L. Branson
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from abc import ABC
from abc import abstractmethod
from typing import Self

from .helper import Number


class Tuple(ABC):
    """
    The interface for the three-dimensional tuple-like classes which are Color,
    Point, & Vector.
    """

    @abstractmethod
    def to_tuple_list(self) -> list[Number]:
        """
        Converts the three-dimensional tuple-like classes (Color, Point &
        Vector) into a list of length four containing the three components
        and a forth component. This list is essentially the homogeneous
        coordinate representation of the tuple.

        :return: the tuple-like classes list
        """
        ...

    @abstractmethod
    def from_tuple_list(self, lst: list[Number]) -> Self:
        """
        Creates a three-dimensional tuple-like class from a tuple list.

        :param lst: the tuple list
        :return: the tuple-like class
        """
        ...
