from conans import ConanFile
#from conan.tools.cmake import CMakeToolchain, CMake
#from conan.tools.layout import cmake_layout
from conans import CMake


class MainprojectConan(ConanFile):
    name = "mainproject"
    version = "1.0"

    # Optional metadata
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Mainproject here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "src/*"

    generators = "cmake", "cmake_find_package", "cmake_paths"

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self.source_folder + "/src")
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
