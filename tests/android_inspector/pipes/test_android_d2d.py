# -*- coding: utf-8 -*-
#
# Copyright (c) nexB Inc. and others. All rights reserved.
# ScanCode is a trademark of nexB Inc.
# SPDX-License-Identifier: Apache-2.0
# See http://www.apache.org/licenses/LICENSE-2.0 for the license text.
# See https://github.com/aboutcode-org/android-inspector for support or download.
# See https://aboutcode.org for more information about nexB OSS projects.
#

import os

from commoncode.resource import Codebase
from commoncode.resource import VirtualCodebase
from commoncode.testcase import FileBasedTesting

from android_inspector.pipes import android_d2d

# Used for tests to regenerate fixtures with regen=True
REGEN_TEST_FIXTURES = os.getenv("SCANCODE_REGEN_TEST_FIXTURES", False)


class TestXgettextSymbolScannerPlugin(FileBasedTesting):

    test_data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data/android_d2d")

    def test_is_jadx_installed(self):
        assert android_d2d.is_jadx_installed()

    def test_android_d2d_run_jadx(self):
        test_file = self.get_test_loc("classes.dex")
        temp_dir = self.get_temp_dir()
        android_d2d.run_jadx(test_file, temp_dir)
        sources_dir = os.path.join(temp_dir, "sources")
        # Check if paths are the same
        expected_loc = self.get_test_loc("run_jadx-expected.json")
        expected_codebase = VirtualCodebase(expected_loc)
        expected_paths = sorted(r.path for r in expected_codebase.walk())
        codebase = Codebase(sources_dir)
        paths = sorted(r.path for r in codebase.walk())
        for expected_path, path in zip(expected_paths, paths):
            self.assertEqual(expected_path, path)
