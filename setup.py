""" installs dnppy """


# sets up dependencies that pip alone seems to frequently fail at.
import install_dependencies
install_dependencies.main()

# standard setup
from distutils.core import setup

setup(
    name='dnppy',
    version='1.15.3b1',
    packages=['dev.test', 'dnppy', 'dnppy.tsa', 'dnppy.core', 'dnppy.modis', 'dnppy.radar', 'dnppy.solar',
              'dnppy.raster', 'dnppy.textio', 'dnppy.convert', 'dnppy.landsat', 'dnppy.R_dnppy', 'dnppy.download'],
    url='https://github.com/NASA-DEVELOP/dnppy',
    download_url="https://github.com/NASA-DEVELOP/dnppy/archive/master.zip",
    license='NASA OPEN SOURCE AGREEMENT VERSION 1.3',
    author=["Jwely",
            "djjensen",
            "Syntaf",
            "lancewatkins",
            "lmakely",
            "qgeddes",
            "Scott Baron",
            ],
    author_email='',
    description='DEVELOP National Program python package'
)


if __name__ == "__main__":
    import pip
    pip.main(["install", "https://github.com/NASA-DEVELOP/dnppy/archive/setup.zip"])