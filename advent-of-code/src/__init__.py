import pathlib


def get_file_path(*args: str) -> pathlib.Path:
    return get_working_directory() / pathlib.Path(*args)


def get_working_directory() -> pathlib.Path:
    return pathlib.Path(__file__).parent.parent


__all__ = ["get_file_path", "get_working_directory"]
