from phdproject.taq.decompression.algorithm import decompress


def test_decompress_hola():
    assert decompress("hola") == "que hace"
