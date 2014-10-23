from runzi_parser import *


def test_export_runzi_points():
    file_obj = open('test_files/runzi_file.txt')
    objects = export_runzi_points(file_obj)
    print objects
    assert len(objects) == 9259
