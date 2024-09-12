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

from commoncode.fileutils import get_temp_dir
from commoncode.testcase import FileBasedTesting
from scancode.cli_test_utils import check_json_scan
from scancode.cli_test_utils import run_scan_click

from android_inspector.pipes import android_d2d

# Used for tests to regenerate fixtures with regen=True
REGEN_TEST_FIXTURES = os.getenv("SCANCODE_REGEN_TEST_FIXTURES", False)


class TestXgettextSymbolScannerPlugin(FileBasedTesting):

    test_data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data/android_d2d")

    def test_is_jadx_installed(self):
        assert android_d2d.is_jadx_installed()

    def test_android_d2d_run_jadx(self):
        test_file = self.get_test_loc("classes.dex")
        temp_dir = get_temp_dir()
        android_d2d.run_jadx(test_file, temp_dir)
        result_file = self.get_temp_file("json")
        sources_dir = os.path.join(temp_dir, "sources")
        args = ["-i", sources_dir, "--json-pp", result_file]
        run_scan_click(args)
        expected_loc = self.get_test_loc("run_jadx-expected.json")
        check_json_scan(expected_loc, result_file, regen=REGEN_TEST_FIXTURES)
