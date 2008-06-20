from setuptools import setup, find_packages

djl_url = "http://douglatornell.ca/software/python/nosy/"
version = "1.0"

setup(
    name="Nosy",
    version=version,
    description="""\
Run the nose test discovery and execution tool whenever a source file
is changed.
    """,
    long_description="""\
An elaborated version of Jeff Winkler's nosy tool that runs nose
whenever a source file is changed.  This version has a command line
parser added, and the capability to use a configuration file to
control what files are watched, and how nose runs.
    """,
    author="Jeff Winkler & Doug Latornell",
    author_email="doug-code@sadahome.ca",
    url=djl_url,
    download_url="%(djl_url)sNosy-%(version)s.tar.gz" % locals(),
    packages=find_packages(),
    install_requires=['nose'],
    entry_points={'console_scripts':['nosy = nosy.nosy:main']}
    )

# end of file
