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

from typing import Self

from .helper import Number
from .tuple import Tuple


class Point(Tuple):

    __x: Number
    """
    The mathematical reference to the x-coordinate scalar value
    """
    __y: Number
    """
    The mathematical reference to the x-coordinate scalar value
    """

    __z: Number
    """
    The mathematical reference to the x-coordinate scalar value
    """

    def __init__(self, x: Number = 0, y: Number = 0, z: Number = 0):
        """
        Initializes the Point Class

        :param x: the mathematical reference to the x-coordinate scalar value
        :param y: the mathematical reference to the y-coordinate scalar value
        :param z: the mathematical reference to the z-coordinate scalar value
        """
        self.__x = x
        self.__y = y
        self.__z = z

    @property
    def x(self) -> Number:
        """
        Gets the x-coordinate scalar value

        :return: the x-coordinate scalar value
        """
        return self.__x

    @x.setter
    def x(self, x: Number) -> None:
        """
        Sets the x-coordinate scalar value

        :param x: the x-coordinate scalar value to set
        :return: None - "void" function
        """
        self.__x = x

    @property
    def y(self) -> Number:
        """
        Gets the y-coordinate scalar value

        :return: the y-coordinate scalar value
        """
        return self.__y

    @y.setter
    def y(self, y: Number) -> None:
        """
        Sets the y-coordinate scalar value

        :param y: the y-coordinate scalar value to set
        :return: None - "void" function
        """
        self.__y = y

    @property
    def z(self) -> Number:
        """
        Gets the z-coordinate scalar value

        :return: the z-coordinate scalar value
        """
        return self.__z

    @z.setter
    def z(self, z: Number) -> None:
        """
        Sets the z-coordinate scalar value

        :param z: the z-coordinate scalar value to set
        :return: None - "void" function
        """
        self.__z = z

    def to_tuple_list(self) -> list[Number]:
        """
        Converts the Point into a list

        :return: the Point List
        """
        return [self.__x, self.__y, self.__z]

    def from_tuple_list(self, lst: list[Number]) -> Self:
        """
        Converts a list into a Point

        :param lst: the list
        :return: the new Point
        """
        return Point(lst[0], lst[1], lst[2])
