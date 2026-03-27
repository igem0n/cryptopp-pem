from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps, cmake_layout
import os

class cryptopp_pem(ConanFile):
    name = "cryptopp-pem"
    version = "8.9.0"
    settings = "os", "arch", "compiler", "build_type"
    exports_sources = "CMakeLists.txt", "pem.h", "pem_common.h", "x509cert.h", "x509cert.cpp", "pem_write.cpp", "pem_read.cpp", "pem_common.cpp"

    options = {
        "shared": [True, False],
        "fPIC": [True, False],
        "with_executable": [True, False]
    }

    default_options = {
        "shared": False,
        "fPIC": True,
        "with_executable": False
    }
    
    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def configure(self):
        if self.options.shared:
            self.options.rm_safe("fPIC")
        
    def requirements(self):
        self.requires("cryptopp/8.9.0", transitive_headers=True)
 
    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()
        deps = CMakeDeps(self)
        deps.generate()

    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["cryptopp-pem"]

