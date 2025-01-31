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

import operator
from functools import partial
from typing import Callable, Self

from .helper import is_almost_equal, Number
from .tuple import Tuple
from .vector import Vector


class Point(Tuple):
    """
    Represents a three-dimensional Point
    """

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

    def __map_items(self, operation: Callable[[Number], Number]) -> Self:
        """
        Maps the operation to each element in the Point

        :param operation: the operation being applied
        :return: The new Point
        """
        return Point(x=operation(self.__x), y=operation(self.__z), z=operation(self.__z))

    def __map_pairs(self, point: Self, operation: Callable[[Number, Number], Number]) -> Self:
        """
        Maps an operation to multiple numbers and for each element in the Pint

        :param point: the secondary Point
        :param operation: the operation
        :return:
        """
        return Point(x=operation(self.__x, point.__x),
                     y=operation(self.__x, point.__x),
                     z=operation(self.__x, point.__x))

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

    def __neg__(self) -> Self:
        """
        Overrides the negation operator

        :return: the negated Point
        """
        return Point(x=-self.__x, y=-self.__y, z=self.__z)

    def __add__(self, other: Number | Self | Vector) -> Self:
        """
        Calculates the sum of a Point and a scalar value, secondary Point, or a Vector; overrides the addition operator.

        :param other: the scalar value, secondary Point, or Vector
        :return: the sum Point
        """
        if isinstance(other, Number): return self.__map_items(partial(operator.add, other))
        elif isinstance(other, Point): return self.__map_pairs(point=other, operation=operator.add)
        elif isinstance(other, Vector): return Point(x=self.__x + other.x, y=self.__y + other.y, z=self.__z + other.z)
        else: return NotImplemented

    def __rand__(self, other: Number | Self | Vector) -> Self:
        """
        Calculates the sum of a Point and a scalar value, a secondary Point, or Vector; overrides the reverse addition
        operator.

        :param other: the scalar value, secondary Point, or Vector
        :return: the sum Point
        """
        return self + other

    def __sub__(self, other: Number | Self | Vector) -> Self | Vector:
        """
        Calculates the difference between a Point and a scalar value, secondary Point, or a Vector; overrides the
        subtraction operator. A Point minus a Point returns a Vector. A Point minus a Vector returns a Point.

        :param other: the scalar value, secondary Point, or Vector
        :return: the sum Point or Vector
        """
        if isinstance(other, Number): return self.__map_items(operation=lambda temporary: temporary - other)
        elif isinstance(other, Point): return Vector(x=self.__x - other.x, y=self.__y - other.y, z=self.__z - other.z)
        elif isinstance(other, Vector): return Point(x=self.__x - other.x, y=self.__y - other.y, z=self.__z - other.z)
        else: return NotImplemented

    def __mul__(self, other: Number | Self) -> Self:
        """
         Calculates the product of a Point and another Point or scalar value; overrides the multiplication operator.

        :param other: the secondary Point or the scalar value
        :return: the product Point
        """
        if isinstance(other, Number): return self.__map_items(operation=partial(operator.mul, other))
        elif isinstance(other, Point): return self.__map_pairs(point=other, operation=operator.mul)
        else: return NotImplemented

    def __rmul__(self, other: Number) -> Self:
        """
        Calculates the product of a Point and another Point or scalar value; overrides the reverse multiplication
        operator.

        :param other: the scalar value
        :return: the product Point
        """
        return self * other

    def __truediv__(self, other: Number) -> Self:
        """
        Calculates the quotient Point between a Point and a scalar value; overrides the division operator.

        :param other: the scalar value
        :return: the quotient Point
        """
        if other == 0: raise ZeroDivisionError
        else: return self.__map_items(operation=lambda temporary: temporary / other)

    def __eq__(self, other: object) -> bool:
        """
        Overrides the equality operator

        :param other: the object being compared
        :return: True if the object is a Point and the components are equal; otherwise False
        """
        if not isinstance(other, Point):
            return False
        else:
            x_boolean: bool = is_almost_equal(left=self.__x, right=other.__x)
            y_boolean: bool = is_almost_equal(left=self.__y, right=other.__y)
            z_boolean: bool = is_almost_equal(left=self.__z, right=other.__z)
            return x_boolean and y_boolean and z_boolean

    def __str__(self) -> str:
        """
        Overrides the stringify method

        :return: the new Point-String
        """
        return f"Point[x={self.__x} y={self.__y} z={self.__z}]"

    def to_tuple_list(self) -> list[Number]:
        """
        Converts the Point into a list

        :return: the Point List
        """
        return [self.__x, self.__y, self.__z]

    def from_tuple_list(self, point_list: list[Number]) -> Self:
        """
        Converts a list into a Point

        :param point_list: the Point list
        :return: the new Point
        """
        return Point(x=point_list[0], y=point_list[1], z=point_list[2])
