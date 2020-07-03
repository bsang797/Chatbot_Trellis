import numpy as np
import pandas as pd
import json

from networks_algo import NetworksAlgo as na

class RomePrototype:

    def __init__(self):
        self.available_channels = ["Public", "Private"]
        self.available_modes = ["Textual", "Visual", "Auditory"]

        RomePrototype._data_request(self)
        RomePrototype._channels_network(self)
        RomePrototype._mode_network(self)
        RomePrototype._final_output(self)

        for x in self.final_output:
            print(x)

    def _data_request(self):
        data = pd.read_excel(r'settings.xlsx', sheet_name='channel_transition')
        self.channel_transition = pd.DataFrame(data, columns=["Public", "Private"]).to_numpy()

        data = pd.read_excel(r'settings.xlsx', sheet_name='channel_network')
        self.channel_network = pd.DataFrame(data, columns=["Public", "Private"]).to_numpy()

        data = pd.read_excel(r'settings.xlsx', sheet_name='mode_transition')
        self.mode_transition = pd.DataFrame(data, columns=["Textual", "Visual", "Auditory"]).to_numpy()

        data = pd.read_excel(r'settings.xlsx', sheet_name='mode_network')
        self.mode_network = pd.DataFrame(data, columns=["Textual", "Visual", "Auditory"]).to_numpy()

    def _channels_network(self):
        self.channel_values = {}
        i = 0
        for x in na.channels_chain(self.channel_transition, self.channel_network):
                total_channel_weight = sum(na.channels_chain(self.channel_transition, self.channel_network))
                self.channel_values[self.available_channels[i]] = x/total_channel_weight
                i += 1

    def _mode_network(self):
        self.mode_values = {}
        i = 0
        for x in na.channels_chain(self.mode_transition, self.mode_network):
                total_mode_weight = sum(na.channels_chain(self.mode_transition, self.mode_network))
                self.mode_values[self.available_modes[i]] = x/total_mode_weight
                i += 1

    def _final_output(self):
        self.final_output = {}
        for x in self.channel_values:
            for y in self.mode_values:
                self.final_output[y + "_" + x] = self.channel_values[x] * self.mode_values[y]

        self.final_output = sorted(self.final_output.items(), key=lambda final_output: final_output[1], reverse=True)