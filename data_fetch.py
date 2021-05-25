import urllib3
from bs4 import BeautifulSoup


class VelocityVersionFetcher:
    def __init__(self, perform_initial_fetch: bool = True, url: str = 'https://nexus.velocitypowered.com/repository'
                                                                      '/maven-public/com/velocitypowered/velocity'
                                                                      '-native/maven-metadata.xml'):
        self.url = url

        self.versions = []
        self.stable_versions = []
        self.latest_version = None
        self.latest_release = None
        self.errored = False

        self.http = urllib3.PoolManager()

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