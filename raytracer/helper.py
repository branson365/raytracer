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

from typing import Final
from typing import TypeAlias

Number: TypeAlias = int | float
"""
The Number constraint or constant
"""

EPSILON: Final[Number] = 0.00001
"""

"""


def clamp(num: Number, minimum: Number, maximum: Number) -> Number:
    """
    Clamps a number between a minimum and maximum value i.e., the number is
    in the range of minimum <= number <= maximum. Sidenote: I would have
    shortened the minimum and maximum parameter names; however, it would
    overshadow the builtin functions and the PyCharm IDLE does not like it.

    :param num: the number scalar value
    :param minimum: the minimum scalar value
    :param maximum: the maximum scalar value
    :return: the number, minimum, or maximum scalar value
    """
    return min(max(minimum, num), maximum)


def is_almost_equal(lhs: Number, rhs: Number) -> bool:
    """
    Determines if the two values are equal using a buffer (epsilon value)

    :param lhs: the left-hand-side scalar value
    :param rhs: the right-hand-side scalar value
    :return: True if the values are equal; otherwise, False
    """
    return abs(lhs - rhs) < EPSILON
