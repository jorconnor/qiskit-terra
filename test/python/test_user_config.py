# This code is part of Qiskit.
#
# (C) Copyright IBM 2017, 2019.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

# pylint: disable=missing-docstring

import os

from qiskit import exceptions
from qiskit.test import QiskitTestCase
from qiskit import user_config


class TestUserConfig(QiskitTestCase):

    def setUp(self):
        super().setUp()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        test_name = str(self.id()).split('.')[-1]
        file_path = os.path.join(current_dir, 'configurations', test_name + ".conf")
        self.config = user_config.UserConfig(file_path)

    def test_empty_file_read(self):
        self.config.read_config_file()
        self.assertEqual({},
                         self.config.settings)

    def test_invalid_optimization_level(self):
        self.assertRaises(exceptions.QiskitUserConfigError,
                          self.config.read_config_file)

    def test_invalid_circuit_drawer(self):
        self.assertRaises(exceptions.QiskitUserConfigError,
                          self.config.read_config_file)

    def test_circuit_drawer_valid(self):
        self.config.read_config_file()
        self.assertEqual({'circuit_drawer': 'latex'},
                         self.config.settings)

    def test_optimization_level_valid(self):
        self.config.read_config_file()
        self.assertEqual(
            {'transpile_optimization_level': 1},
            self.config.settings)

    def test_invalid_num_processes(self):
        self.assertRaises(exceptions.QiskitUserConfigError,
                          self.config.read_config_file)

    def test_valid_num_processes(self):
        self.config.read_config_file()
        self.assertEqual(
            {'num_processes': 31},
            self.config.settings)

    def test_valid_parallel(self):
        self.config.read_config_file()
        self.assertEqual(
            {'parallel_enabled': False},
            self.config.settings)

    def test_all_options_valid(self):
        self.config.read_config_file()
        self.assertEqual({'circuit_drawer': 'latex',
                          'circuit_mpl_style': 'default',
                          'circuit_mpl_style_path': ['~', '~/.qiskit'],
                          'transpile_optimization_level': 3,
                          'num_processes': 15,
                          'parallel_enabled': False},
                         self.config.settings)
