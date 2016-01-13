# -*- coding: utf-8 -*-
from os import path
from pyassets.manager import Manager
from pyassets.filters.coffeescript_filter import CoffeeScriptFilter

here = path.abspath(path.dirname(__file__))
static_base_dir = path.join(here, "static")


def test_cs():
    global here
    expected_out = """(function() {
  var square;

  square = function(x) {
    return x * x;
  };

}).call(this);
    """
    manager = Manager(static_base_dir)

    js_group = ["coffee/test.coffee"]
    manager.add_group("cs", js_group)


    manager.add_filter(CoffeeScriptFilter())

    # get output from a manager
    output = manager.output_for_group("cs")

    assert output, expected_out.strip()



