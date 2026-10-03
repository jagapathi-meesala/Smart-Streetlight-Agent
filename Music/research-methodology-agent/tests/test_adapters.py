from adapters.portable_adapter import PortableAdapter

def test_adapter_contract_is_framework_neutral():
    assert PortableAdapter.framework_name == 'framework-independent'
