# -*- coding: utf-8 -*-
from pyassets.manager import Manager
from pyassets.file_group import FileGroup
from os import path
from tests.filters.dummy_filter import DummyFilter

here = path.abspath(path.dirname(__file__))
static_base_dir = path.join(here, "static")

def test_manager_version():
    assert Manager.VERSION, 0.1

def test_adding_and_getting_groups_of_files():
    global static_base_dir
    manager = Manager(static_base_dir)

    js_group = ["js/file1.js", "js/file2.js"]
    manager.add_group("js", js_group)

    js_group = manager.get_by_name("js")
    assert type(js_group), type(FileGroup)
    files = js_group.get_files()
    assert len(files), 2
    for file in js_group:
        print("jsg iter", file)
        assert file in js_group

    for file in js_group.get_files():
        print("jsg iter - get files", file)
        assert file in js_group


def test_processing_files():
    global static_base_dir

    manager = Manager(static_base_dir)

    js_group = ["css/file1.css", "css/file2.css"]
    manager.add_group("js", js_group)

    df = DummyFilter()
    manager.add_filter(df)

    # get output from a manager
    output = manager.output_for_group("js")
    with(open(path.join(static_base_dir, "example_out.css"))) as f:
        # test if content fits
        assert f.read(), output

