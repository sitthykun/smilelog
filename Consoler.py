"""
Author: masakokh
Version: 1.0.0
"""
import datetime
from typing import Any


class Consoler:
    """

    """
    # hide all numbers that added
    hide    = []
    # index of output
    id      = 0

    def __init__(self, enable: bool, color: bool = True):
        """

        """
        # config
        self._enable            = enable

        #
        self._logId             = datetime.datetime.now().strftime('%H:%M:%S')
        # set color
        self._color             = color
        # inner class
        self._style             = self.StyleModifier()

    def _dataFormat(self, content: Any) -> Any:
        """

        :param _data:
        :return:
        """
        if isinstance(content, dict):
            return str(content)
        elif isinstance(content, str) or type(content) == str:
            return content
        else:
            return ''

    def _print(self, typeName: str = '', title: str = '', content: dict = {}, color: str = '') -> None:
        """

        :param typeName:
        :param title:
        :param content:
        :param color:
        :return:
        """
        # is enabled
        if bool(self._enable):
            # increase index first
            Consoler.id += 1

            # do filter
            if Consoler.id not in Consoler.hide:
                # check color too
                if self._color:
                    # generate content format with color
                    print(
                        f"{self._logId} <id: {Consoler.id}>"
                        f"{color}>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>{self._style.ENDC}\n"
                        f"[{typeName}] {self._style.TEXT_BOLD}{title}{self._style.ENDC} \n{self._dataFormat(content)} \n"
                        f"{color}<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<{self._style.ENDC}\n\n\n"
                    )
                else:
                    # generate content format without color
                    print(
                        f"{self._logId} <id: {Consoler.id}>"
                        f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
                        f"[{typeName}] {self._style.TEXT_BOLD}{title}{self._style.ENDC} \n{self._dataFormat(content)} \n{self._logId} "
                        f"<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n\n\n"
                    )

    def disable(self, numbers: list = []) -> None:
        """

        :return:
        """
        Consoler.hide   = numbers

    def error(self, title: str = '', content: dict = {}) -> None:
        """

        :param title:
        :param content:
        :return:
        """
        if self._color:
            self._print(
                f'{self._style.RED}ERROR{self._style.ENDC}'
                , f'{self._style.RED}{title}{self._style.ENDC}'
                , content
                , self._style.RED
            )
        else:
            self._print(
                'ERROR'
                , title
                , content
                , self._style.RED
            )

    def info(self, title: str = '', content: dict = {}) -> None:
        """
        :param title:
        :param content:
        :return:
        """
        if self._color:
            self._print(f'{self._style.BLUE}INFO{self._style.ENDC}'
                        , f'{self._style.BLUE}{title}{self._style.ENDC}'
                        , content
                        , self._style.BLUE
                        )
        else:
            self._print('INFO'
                        , title
                        , content
                        , self._style.BLUE
                        )

    def success(self, title: str = '', content: dict = {}) -> None:
        """
        :param title:
        :param content:
        :return:
        """
        if self._color:
            self._print(
                f'{self._style.GREEN}SUCCESS{self._style.ENDC}'
                , f'{self._style.GREEN}{title}{self._style.ENDC}'
                , content
                , self._style.GREEN
            )
        else:
            self._print(
                'INFO'
                , title
                , content
                , self._style.GREEN
            )

    def track(self, title: str = '', content: dict = {}) -> None:
        """
        :param title:
        :param content:
        :return:
        """
        if self._color:
            self._print('TRACK', title, content)
        else:
            self._print('TRACK', title, content)

    def warning(self, title: str = '', content: dict = {}) -> None:
        """
        :param title:
        :param content:
        :return:
        """
        if self._color:
            self._print(
                f'{self._style.YELLOW}WARNING{self._style.ENDC}'
                , f'{self._style.YELLOW}{title}{self._style.ENDC}'
                , content
                , self._style.YELLOW
            )
        else:
            self._print(
                'WARNING'
                , title
                , content
                , self._style.YELLOW
            )

    class StyleModifier:
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        RED = '\033[91m'
        YELLOW = '\033[93m'

        TEXT_BOLD = '\033[1m'
        TEXT_UNDERLINE = '\033[4m'

        ENDC = '\033[0m'