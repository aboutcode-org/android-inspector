# SPDX-License-Identifier: Apache-2.0
#
# Copyright (c) nexB Inc. and others. All rights reserved.
# ScanCode is a trademark of nexB Inc.
# SPDX-License-Identifier: Apache-2.0
# See http://www.apache.org/licenses/LICENSE-2.0 for the license text.
# See https://github.com/aboutcode-org/android-inspector for support or download.
# See https://aboutcode.org for more information about nexB OSS projects.
#

from scanpipe.pipelines.deploy_to_develop import DeployToDevelop

from android_inspector.pipes import android_d2d


class AndroidAPKDeployToDevelop(DeployToDevelop):
    """
    Establish relationships between two code trees: deployment and development for Android APKs.

    This pipeline requires a minimum of two archive files, each properly tagged with:

    - **from** for archives containing the development source code.
    - **to** for archives containing the deployment compiled code.

    When using download URLs as inputs, the "from" and "to" tags can be
    provided by adding a "#from" or "#to" fragment at the end of the download URLs.

    When uploading local files:

    - **User Interface:** Use the "Edit flag" link in the "Inputs" panel of the Project
      details view.
    - **REST API:** Utilize the "upload_file_tag" field in addition to the
      "upload_file".
    - **Command Line Interface:** Tag uploaded files using the "filename:tag" syntax,
      for example, ``--input-file path/filename:tag``.
    """

    @classmethod
    def steps(cls):
        return (
            cls.get_inputs,
            cls.extract_inputs_to_codebase_directory,
            cls.extract_archives,
            cls.convert_dex_to_java,
            cls.collect_and_create_codebase_resources,
            cls.map_checksum,
            cls.map_path,
        )

    def convert_dex_to_java(self):
        android_d2d.convert_dex_to_java(self.project, to_only=True)
