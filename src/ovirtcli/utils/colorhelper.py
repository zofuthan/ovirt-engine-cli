#
# Copyright (c) 2010 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#           http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


class ColorHelper():
    BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

    __NONE = None
    __ENDC = '\033[0m'

    @staticmethod
    def color(text, color_):
        """
        Colors text

        @param text: text to color
        @param color_: color to use (ColorHelper.RED|ColorHelper.BLUE...)
        """
        if color_:
            return "\x1b[1;%dm" % (30 + color_) + text + "\x1b[0m"
        return text
