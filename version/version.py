from __future__ import annotations

class Version:
    def __init__(self, version: str = None, *, 
        major: int = 0, 
        minor: int = 0, 
        build: int = 0, 
        revision: int = 0
    ) -> None:
        """Version 

        Args:
            version (str, optional): Parse version from string.
            major (int, optional): Major version number. Defaults to 0.
            minor (int, optional): Minor version number. Defaults to 0.
            build (int, optional): Build number. Defaults to 0.
            revision (int, optional): Revision number. Defaults to 0.

        Hint:
            - Version("1.8")
            - Version(major=1, minor=8)
        """
        self.__major = int(major)
        self.__minor = int(minor)
        self.__build = int(build)
        self.__revision = int(revision)
        
        if type(version) == str:
            try:
                values = [int(x) for x in version.split("-")[0].split(".", maxsplit=3)]
                length = len(values)

                if length > 0: 
                    self.__major = values[0]

                    if length > 1: 
                        self.__minor = values[1]

                        if length > 2: 
                            self.__build = values[2]

                            if length > 3: 
                                self.__revision = values[3]
            except:
                raise Exception(f"Invalid version: {repr(version)}")

        if self.__major < 0: self.__major = 0
        if self.__minor < 0: self.__minor = 0
        if self.__build < 0: self.__build = 0
        if self.__revision < 0: self.__revision = 0

    @property
    def major(self) -> int:
        """Major version number"""
        return self.__major

    @major.setter
    def major(self, value: int) -> int:
        if value < 0: value = 0
        self.__major = int(value)

    @property
    def minor(self) -> int:
        """Minor version number"""
        return self.__minor
        
    @minor.setter
    def minor(self, value: int) -> int:
        if value < 0: value = 0
        self.__minor = int(value)

    @property
    def build(self) -> int:
        """Build number"""
        return self.__build
        
    @build.setter
    def build(self, value: int) -> int:
        if value < 0: value = 0
        self.__build = int(value)

    @property
    def revision(self) -> int:
        """Revision number"""
        return self.__revision
        
    @revision.setter
    def revision(self, value: int) -> int:
        if value < 0: value = 0
        self.__revision = int(value)

    def __str__(self) -> str:
        if self.revision != 0:
            return f"{self.major}.{self.minor}.{self.build}.{self.revision}"

        if self.build != 0:
            return f"{self.major}.{self.minor}.{self.build}"
            
        return f"{self.major}.{self.minor}"

    def __repr__(self) -> str:
        return f"Version({repr(str(self))})"

    def __eq__(self, other: Version) -> bool:
        if type(other) != Version: return False
        
        return self.major == other.major \
            and self.minor == other.minor \
            and self.build == other.build \
            and self.revision == other.revision

    def __ne__(self, other: Version) -> bool:
        return not self.__eq__(other)

    def __gt__(self, other: Version) -> bool:
        if type(other) != Version: return False

        if self.major > other.major:
            return True
        elif self.major < other.major:
            return False

        if self.minor > other.minor:
            return True
        elif self.minor < other.minor:
            return False

        if self.build > other.build:
            return True
        elif self.build < other.build:
            return False

        if self.revision > other.revision:
            return True
        elif self.revision < other.revision:
            return False

        return False

    def __lt__(self, other: Version) -> bool:
        if type(other) != Version: return False

        if self.major < other.major:
            return True
        elif self.major > other.major:
            return False

        if self.minor < other.minor:
            return True
        elif self.minor > other.minor:
            return False

        if self.build < other.build:
            return True
        elif self.build > other.build:
            return False

        if self.revision < other.revision:
            return True
        elif self.revision > other.revision:
            return False

        return False

    def __ge__(self, other: Version) -> bool:
        return self.__eq__(other) or self.__gt__(other)

    def __le__(self, other: Version) -> bool:
        return self.__eq__(other) or self.__lt__(other)

    def __add__(self, other: Version) -> Version:
        return Version(
            major=self.major + other.major,
            minor=self.minor + other.minor,
            build=self.build + other.build,
            revision=self.revision + other.revision)

    def __sub__(self, other: Version) -> Version:
        return Version(
            major=self.major - other.major,
            minor=self.minor - other.minor,
            build=self.build - other.build,
            revision=self.revision - other.revision)