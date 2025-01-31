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

from typing import Final, TypeAlias

Number: TypeAlias = int | float
"""
The Number constraint or constant
"""

EPSILON: Final[Number] = 0.00001
"""
The Buffer (tolerance) value
"""


def clamp(number: Number, minimum: Number, maximum: Number) -> Number:
    """
    Clamps a number between a minimum and maximum scalar values.

    :param number: the number scalar value
    :param minimum: the minimum scalar value
    :param maximum: the maximum scalar value
    :return: the number, minimum, or maximum scalar values
    """
    return min(max(minimum, number), maximum)


def is_almost_equal(left: Number, right: Number) -> bool:
    """
    Determines if the two values are equal using a buffer (epsilon) scalar value.

    :param left: the left-hand-side scalar value
    :param right: the right-hand-side scalar value
    :return: True if the values are equal; otherwise, False
    """
    return abs(left - right) < EPSILON
