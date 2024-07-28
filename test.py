from main import compress, decompress
import unittest

# Test cases
class TestCalculaMedia(unittest.TestCase):
    def test_1(self):
        resultado = compress("WWWWWWWWWWWWWWWWWWWW")
        self.assertEqual(resultado, "W(k)")

    def test_2(self):
        resultado = decompress("W(a)")
        self.assertEqual(resultado, "WWWWWWWWWW")

    def test_3(self):
        resultado = compress("AABBBCCCC")
        self.assertEqual(resultado, "AAB(3)C(4)")

    def test_4(self):
        resultado = decompress("AAB(3)C(4)")
        self.assertEqual(resultado, "AABBBCCCC")

    def test_5(self):
        resultado = compress("AAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBB")
        self.assertEqual(resultado, "A(d)B(m)")
    
    def test_6(self):
        resultado = decompress("A(d)B(m)")
        self.assertEqual(resultado, "AAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBB")

    def test_7(self):
        resultado = compress("")
        self.assertEqual(resultado, "la cadena no puede estar vacía")
    
    def test_8(self):
        resultado = decompress("")
        self.assertEqual(resultado, "la cadena no puede estar vacía")
    
    def test_9(self):
        resultado = compress("ABCDE")
        self.assertEqual(resultado, "ABCDE")

    def test_10(self):
        resultado = decompress("ABCDE")
        self.assertEqual(resultado, "ABCDE")
    
    def test_11(self):
        resultado = compress("12345")
        self.assertEqual(resultado, "la cadena solo puede contener letras")
if __name__ == '__main__':
    unittest.main()