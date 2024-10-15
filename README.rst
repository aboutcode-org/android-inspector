=================
android-inspector
=================

android-inspector is a set of utilities to inspect binary Android application APK as well as Android
firmwares. This is also a ScanCode.io pipeline plugin.

The available features are:

- Extract and map the files found in a binary Android application to the assumed corresponding
  source code.

Other information:

- License: Apache-2.0
- Copyright (c) nexB Inc., AboutCode.org and others.
- Homepage: https://github.com/aboutcode-org/android-inspector/


Requirements
------------

- ScanCode.io https://github.com/nexB/scancode.io
- Ensure Java 11+ is in your path (using an OpenJDK installation)
- Install jadx 1.5.0 https://github.com/skylot/jadx (You will need to add jadx to your path or
  moved its ``bin`` and ``lib`` directories to your ``/usr`` directory.

See also the next section for detailed instructions.


Local installation and usage test
------------------------------------

To install:
~~~~~~~~~~~~

- Clone android-inspector locally side-by-side: ``git clone https://github.com/aboutcode-org/android-inspector``
- Clone ScanCode.io locally side-by-side: ``git clone https://github.com/aboutcode-org/scancode.io``
- Change to the scancode.io directory and run ``make dev`` then ``source bin/activate`` 

  - Follow the full instructions at https://scancodeio.readthedocs.io/en/latest/installation.html#local-development-installation

- Install jadx minimally

  - Download https://github.com/skylot/jadx/releases/download/v1.5.0/jadx-1.5.0.zip in your
    scancode.io directory
  - Extract with ``unzip -qd jadx-1.5.0 jadx-1.5.0.zip``
  - Add the extracted directory jadx-1.5.0/bin and jadx-1.5.0/lib to your path with
    ``export PATH=$PATH:`pwd`/jadx-1.5.0/bin/jadx:`pwd`/jadx-1.5.0/lib``

- Run ``pip install --editable ../android-inspector``
- Run ScanCode.io with ``./manage.py runserver --insecure`` and open the URL in your browser.
  There is a new "android_d2d" pipeline available when creating a new project.


To use with example Android APKs and sources:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Create a new project and name it "sample-apk-analysis"
- In the input section, add ``Download URLs`` for the source and binary of a public APK:

You can use this pair of source (aka. "from") and binaries (aka. "to"):
  
  - https://github.com/ochadenas/cpudefense/archive/refs/tags/v1.42.zip#from
  - https://f-droid.org/repo/de.chadenas.cpudefense_42.apk#to

Or you can use alternatively this other example pair:

- https://github.com/Acclorite/book-story/archive/refs/tags/v1.3.0.tar.gz#from
- https://github.com/Acclorite/book-story/releases/download/v1.3.0/book-story.apk#to

Then:

- Select "android_d2d" in the pipeline dropdown and click "create".
- Wait for the pipeline to complete, and check the created Relations as well as the missing "To"
  source files resulting from mapping the binaries back to sources.
  
At this stage we typically report missing many source files because these are not present in the
source code reposirories. In particular:

- PurlDB matching would be enabled in a full ScanCode.io installation and could help match
  the Android toolchain and standard library if indexed.
- There is a significant number of standard library Java files that are part of the Android
  toolchain. This will be resolved with this issue https://github.com/aboutcode-org/android-inspector/issues/3


Development
----------------

- Install requirements and dependencies using ``make dev``
- Then ``source venv/bin/activate``

Testing:

- To run tests: ``pytest -vvs``



Acknowledgements, Funding, Support and Sponsoring
--------------------------------------------------------

This project is funded, supported and sponsored by:

- Generous support and contributions from users like you!
- the European Commission NGI programme
- the NLnet Foundation 
- the Swiss State Secretariat for Education, Research and Innovation (SERI)
- Google, including the Google Summer of Code and the Google Seasons of Doc programmes
- Mercedes-Benz Group
- Microsoft and Microsoft Azure
- AboutCode ASBL
- nexB Inc. 



|europa|   |dgconnect| 

|ngi|   |nlnet|   

|aboutcode|  |nexb|


This project was funded through the NGI0 Core Fund, a fund established by NLnet with financial
support from the European Commission's Next Generation Internet programme, under the aegis of DG
Communications Networks, Content and Technology under grant agreement No 101092990.

|ngizerocore| https://nlnet.nl/project/Back2source-next/

.. |nlnet| image:: https://nlnet.nl/logo/banner.png
    :target: https://nlnet.nl
    :height: 50
    :alt: NLnet foundation logo

.. |ngi| image:: https://ngi.eu/wp-content/uploads/thegem-logos/logo_8269bc6efcf731d34b6385775d76511d_1x.png
    :target: https://ngi.eu35
    :height: 50
    :alt: NGI logo

.. |nexb| image:: https://nexb.com/wp-content/uploads/2022/04/nexB.svg
    :target: https://nexb.com
    :height: 30
    :alt: nexB logo

.. |europa| image:: https://ngi.eu/wp-content/uploads/sites/77/2017/10/bandiera_stelle.png
    :target: http://ec.europa.eu/index_en.htm
    :height: 40
    :alt: Europa logo

.. |aboutcode| image:: https://aboutcode.org/wp-content/uploads/2023/10/AboutCode.svg
    :target: https://aboutcode.org/
    :height: 30
    :alt: AboutCode logo

.. |swiss| image:: https://www.sbfi.admin.ch/sbfi/en/_jcr_content/logo/image.imagespooler.png/1493119032540/logo.png
    :target: https://www.sbfi.admin.ch/sbfi/en/home/seri/seri.html
    :height: 40
    :alt: Swiss logo

.. |dgconnect| image:: https://commission.europa.eu/themes/contrib/oe_theme/dist/ec/images/logo/positive/logo-ec--en.svg
    :target: https://commission.europa.eu/about-european-commission/departments-and-executive-agencies/communications-networks-content-and-technology_en
    :height: 40
    :alt: EC DG Connect logo

.. |ngizerocore| image:: https://nlnet.nl/image/logos/NGI0_tag.svg
    :target: https://nlnet.nl/core
    :height: 40
    :alt: NGI Zero Core Logo

.. |ngizerocommons| image:: https://nlnet.nl/image/logos/NGI0_tag.svg
    :target: https://nlnet.nl/commonsfund/
    :height: 40
    :alt: NGI Zero Commons Logo

.. |ngizeropet| image:: https://nlnet.nl/image/logos/NGI0PET_tag.svg
    :target: https://nlnet.nl/PET
    :height: 40
    :alt: NGI Zero PET logo

.. |ngizeroentrust| image:: https://nlnet.nl/image/logos/NGI0Entrust_tag.svg
    :target: https://nlnet.nl/entrust
    :height: 38
    :alt: NGI Zero Entrust logo

.. |ngiassure| image:: https://nlnet.nl/image/logos/NGIAssure_tag.svg
    :target: https://nlnet.nl/image/logos/NGIAssure_tag.svg
    :height: 32
    :alt: NGI Assure logo

.. |ngidiscovery| image:: https://nlnet.nl/image/logos/NGI0Discovery_tag.svg
    :target: https://nlnet.nl/discovery/
    :height: 40
    :alt: NGI Discovery logo







