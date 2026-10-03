from tools import select_methodology

def test_unexpected_field_rejected():
    r=select_methodology.run({'objective':'describe','secret':'abc'}); assert not r.ok

def test_wrong_input_type_rejected():
    r=select_methodology.run([]); assert not r.ok

def test_empty_objective_rejected():
    r=select_methodology.run({'objective':'   '}); assert not r.ok
