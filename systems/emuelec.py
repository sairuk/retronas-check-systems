#!/usr/bin/env python3

import os
from lxml import etree
from lib.url import URLHandler
from lib.config import Config
from lib.logger import Logger
from systems.emulationstation import EmulationStation


class EmuELEC(EmulationStation):
    def __init__(self):
        self.name = 'emulelec'
        self.system_key = self.name
        self.logger = Logger(self.name)
        self.systems_url = 'https://raw.githubusercontent.com/EmuELEC/EmuELEC/master/packages/sx05re/emuelec-emulationstation/config/es_systems.cfg'
        self.systems = []
        self.ignored = ['setup']
        self.logger.log_info("Initiated %s module" % self.name)

    def read(self):
        self.uh = URLHandler()
        self.content = self.uh.direct(self.systems_url)
        self.data = self.read_config(self.content[0])
        self.systems = self.get_paths(self.data)