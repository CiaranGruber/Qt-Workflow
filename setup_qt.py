import subprocess
from pathlib import Path, PurePosixPath

ENVIRONMENT_LOCATION = "../testenv/Scripts/activate"


def convert_ui_files(directory):
    """Walks through subdirectories and files to convert the ui files"""
    for file in Path.iterdir(directory):
        if Path.is_dir(file):
            convert_ui_files(file)
        elif Path(file).suffix == ".ui":
            ui_file = Path(file)
            converted_file = directory / Path("ui_" + PurePosixPath(file).stem + ".py")
            command = "call {} && pyside6-uic \"{}\" > \"{}\"".format(ENVIRONMENT_LOCATION, ui_file, converted_file)
            subprocess.call(command, shell=True)


def convert_qrc_files(directory):
    """Walks through subdirectories and files to convert qrc files"""
    for file in Path.iterdir(directory):
        if Path.is_dir(file):
            convert_ui_files(file)
        elif Path(file).suffix == ".qrc":
            rc_file = Path(file)
            converted_file = directory / Path("rc_" + PurePosixPath(file).stem + ".py")
            command = "call {} && pyside6-rcc \"{}\" -o \"{}\"".format(ENVIRONMENT_LOCATION, rc_file, converted_file)
            subprocess.call(command, shell=True)


if __name__ == '__main__':
    start_dir = Path()
    convert_ui_files(start_dir)
    convert_qrc_files(start_dir)
