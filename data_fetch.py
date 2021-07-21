import json

import urllib3
from bs4 import BeautifulSoup

velocity_native_url = "https://nexus.velocitypowered.com/repository/maven-public/com/velocitypowered/velocity-native/"
pool_manager = urllib3.PoolManager()


class VelocityVersionFetcher:
    # TODO: Fix default url when tux migrates to reposilite
    def __init__(self, perform_initial_fetch: bool = True, url: str = 'https://nexus.velocitypowered.com/repository'
                                                                      '/maven-public/com/velocitypowered/velocity'
                                                                      '-native/maven-metadata.xml'):
        self.url = url

        self.versions = []
        self.stable_versions = []
        self.latest_version = None
        self.latest_release = None
        self.errored = False

        self.http = pool_manager

        if perform_initial_fetch:
            self.fetch_data()

    def fetch_data(self):
        self.versions = []
        self.stable_versions = []
        self.latest_version = None
        self.latest_release = None

        request = self.http.request('GET', self.url)
        if request.status == 200:
            raw_xml = request.data.decode("utf-8")
            parsed_xml = BeautifulSoup(raw_xml, "lxml")

            for item in parsed_xml.metadata.versioning.versions.findAll("version"):
                self.versions.append(str(item.text))

            for item in self.versions:
                if not "-SNAPSHOT" in item:
                    self.stable_versions.append(item)

            self.latest_version = str(parsed_xml.metadata.versioning.latest.text)
            self.latest_release = str(parsed_xml.metadata.versioning.release.text)
            self.errored = False
        else:
            self.errored = True


class VelocityDownloadFetcher:
    def __init__(self, version: str, url: str = 'https://nexus.velocitypowered.com/repository/maven-public/com'
                                                '/velocitypowered/velocity-native/', extension: str = ".jar"):
        self.url = f"{url}{version}/velocity-native-{version}{extension}"
        if "-snapshot" in version.lower():
            self.url = "/snapshot-error/"


class VelocityVersion:
    def __init__(self, real: bool, version: str, module_info: dict or None, base_url: str = velocity_native_url):
        self.real = real

        self.version = version
        self.snapshot = "-SNAPSHOT" in version

        self.relative_url = None
        self.url = None
        self.velocity_file_sha512 = None
        self.velocity_file_sha256 = None
        self.velocity_file_sha1 = None
        self.velocity_file_md5 = None

        if real:
            velocity_file = module_info["variants"][0]["files"][0]  # Assume only 1 variant with 1 file

            self.relative_url = velocity_file["url"]
            self.url = f"{base_url}{version}/{self.relative_url}"
            self.velocity_file_sha512 = velocity_file["sha512"]
            self.velocity_file_sha256 = velocity_file["sha256"]
            self.velocity_file_sha1 = velocity_file["sha1"]
            self.velocity_file_md5 = velocity_file["md5"]


def get_version(version: str, base_url: str = velocity_native_url,
                http: urllib3.PoolManager = pool_manager) -> VelocityVersion:
    version_url = base_url + version
    version_url_module = f"{version_url}/velocity-native-{version}.module"

    if "-SNAPSHOT" in version:
        request = pool_manager.request("GET", f"{version_url}/maven-metadata.xml")
        if request.status == 200:
            raw_xml = request.data.decode("utf-8")
            parsed_xml = BeautifulSoup(raw_xml, "lxml")

            snapshot = parsed_xml.metadata.versioning.snapshot

            snapshot_name = f"{version.replace('-SNAPSHOT', '')}-{snapshot.timestamp.text}-{snapshot.buildnumber.text}"

            version_url_module = f"{velocity_native_url}{version}/velocity-native-{snapshot_name}.module"
        else:
            return VelocityVersion(False, version, None)

    request = pool_manager.request('GET', version_url_module)

    if request.status == 200:
        module_info = json.loads(request.data.decode("utf-8"))

        return VelocityVersion(True, version, module_info, base_url)
    else:
        return VelocityVersion(False, version, None)
