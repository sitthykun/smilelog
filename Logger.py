"""
Author: masakokh
Version: 1.1.0
"""
import datetime
import time
from typing import Any


class Logger:
    """

    """
    # hide all numbers that added
    hide    = []
    # index of output
    id      = 0

    def __init__(self, path: str, prefix: str, extension: str, formatFileName: str, enable: bool, color: bool = True):
        """

        """
        # config
        self.__enable           = enable
        self.__extension        = extension
        self.__formatFileName   = formatFileName
        self.__path             = path
        self.__prefix           = prefix

        #
        self.__filename         = self.__getFileName()
        self.__logId            = datetime.datetime.now().strftime('%H:%M:%S')
        # set color
        self.__color            = color
        # inner class
        self.__style            = self.StyleModifier()

    def __dataFormat(self, content: Any) -> Any:
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

    def __getFileName(self) -> str:
        """

        :return:
        """
        return self.__path \
               + self.__prefix \
               + time.strftime(self.__formatFileName) \
               + self.__extension

    def __write(self, typeName: str = '', title: str = '', content: dict = {}, color: str = '') -> None:
        """

        :param typeName:
        :param title:
        :param content:
        :return:
        """
        # write log
        if bool(self.__enable):
            try:
                # open log file, if not exist will create
                f = open(self.__filename, 'a+', encoding= 'utf-8')
                # increase index first
                Logger.id += 1

                # do filter
                if Logger.id not in Logger.hide:
                    if self.__color:
                        # generate content format with color
                        f.write(
                            f"{self.__logId} <id: {Logger.id}>"
                            f"{color}>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>{self.__style.ENDC}\n"
                            f"[{typeName}] {self.__style.TEXT_BOLD}{title}{self.__style.ENDC} \n{self.__dataFormat(content)} \n"
                            f"{color}<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<{self.__style.ENDC}\n\n\n"
                        )

                        # generate content format with color
                        print(
                            f"{self.__logId} <id: {Logger.id}>"
                            f"{color}>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>{self.__style.ENDC}\n"
                            f"[{typeName}] {self.__style.TEXT_BOLD}{title}{self.__style.ENDC} \n{self.__dataFormat(content)} \n"
                            f"{color}<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<{self.__style.ENDC}\n\n\n"
                        )
                    else:
                        # generate content format without color
                        f.write(
                            f"{self.__logId} <id: {Logger.id}>"
                            f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
                            f"[{typeName}] {self.__style.TEXT_BOLD}{title}{self.__style.ENDC} \n{self.__dataFormat(content)} \n{self.__logId} "
                            f"<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n\n\n"
                        )

                        # generate content format without color
                        f.write(
                            f"{self.__logId} <id: {Logger.id}>"
                            f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
                            f"[{typeName}] {self.__style.TEXT_BOLD}{title}{self.__style.ENDC} \n{self.__dataFormat(content)} \n{self.__logId} "
                            f"<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n\n\n"
                        )

                # close file
                f.close()
            except IOError as e:
                print(f"IOError open file {e.errno} {e.strerror}({self.__filename})")
            except FileNotFoundError as e:
                print(f"FileNotFoundError open file {e.errno} {e.strerror}({self.__filename})")
            except Exception as e:
                print(f"Exception open file {e.errno} {e.strerror}({self.__filename})")

    def disable(self, numbers: list = []) -> None:
        """

        :return:
        """
        Logger.hide     = numbers

    def error(self, title: str = '', content: dict = {}) -> None:
        """

        :param title:
        :param content:
        :return:
        """
        if self.__color:
            self.__write(
                f'{self.__style.RED}ERROR{self.__style.ENDC}'
                , f'{self.__style.RED}{title}{self.__style.ENDC}'
                , content
                , self.__style.RED
            )
        else:
            self.__write(
                'ERROR'
                , title
                , content
                , self.__style.RED
            )

    def info(self, title: str = '', content: dict = {}) -> None:
        """
        :param title:
        :param content:
        :return:
        """
        if self.__color:
            self.__write(f'{self.__style.BLUE}INFO{self.__style.ENDC}'
                        , f'{self.__style.BLUE}{title}{self.__style.ENDC}'
                        , content
                        , self.__style.BLUE
                        )
        else:
            self.__write('INFO'
                        , title
                        , content
                        , self.__style.BLUE
                        )

    def success(self, title: str = '', content: dict = {}) -> None:
        """
        :param title:
        :param content:
        :return:
        """
        if self.__color:
            self.__write(
                f'{self.__style.GREEN}SUCCESS{self.__style.ENDC}'
                , f'{self.__style.GREEN}{title}{self.__style.ENDC}'
                , content
                , self.__style.GREEN
            )
        else:
            self.__write(
                'INFO'
                , title
                , content
                , self.__style.GREEN
            )

    def track(self, title: str = '', content: dict = {}) -> None:
        """
        :param title:
        :param content:
        :return:
        """
        if self.__color:
            self.__write('TRACK', title, content)
        else:
            self.__write('TRACK', title, content)

    def warning(self, title: str = '', content: dict = {}) -> None:
        """
        :param title:
        :param content:
        :return:
        """
        if self.__color:
            self.__write(
                f'{self.__style.YELLOW}WARNING{self.__style.ENDC}'
                , f'{self.__style.YELLOW}{title}{self.__style.ENDC}'
                , content
                , self.__style.YELLOW
            )
        else:
            self.__write(
                'WARNING'
                , title
                , content
                , self.__style.YELLOW
            )

    class StyleModifier:
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        RED = '\033[91m'
        YELLOW = '\033[93m'

        TEXT_BOLD = '\033[1m'
        TEXT_UNDERLINE = '\033[4m'

        ENDC = '\033[0m'
