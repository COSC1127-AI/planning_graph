VERSION = "dev"
try:
    # this requires the package to be installed!
    from importlib.metadata import version, PackageNotFoundError
    VERSION = version("lzvcup")
except PackageNotFoundError:
    VERSION = "dev"  # fallback version - running with python -m lzvcup
