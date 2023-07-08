import unittest
from main import validate_name, validate_country, validate_primary_language, validate_age_group

class ApplicationTests(unittest.TestCase):
    def test_validate_name(self):
        # Test cases for validating names
        self.assertTrue(validate_name("John"))  # Valid name
        self.assertFalse(validate_name("123"))  # Invalid name with digits
        self.assertFalse(validate_name("John Smith"))  # Invalid name with spaces
    
    def test_validate_country(self):
        # Test cases for validating countries
        self.assertTrue(validate_country("USA"))  # Valid country
        self.assertFalse(validate_country("123"))  # Invalid country
        self.assertFalse(validate_country("InvalidCountry"))  # Invalid country name
    
    def test_validate_primary_language(self):
        # Test cases for validating primary languages
        self.assertTrue(validate_primary_language("English"))  # Valid primary language
        self.assertFalse(validate_primary_language("123"))  # Invalid primary language
        self.assertFalse(validate_primary_language("InvalidLanguage"))  # Invalid primary language name
    
    def test_validate_age_group(self):
        # Test cases for validating age groups
        self.assertTrue(validate_age_group("5-10"))  # Valid age group
        self.assertFalse(validate_age_group("InvalidAgeGroup"))  # Invalid age group format
        self.assertFalse(validate_age_group("30-40"))  # Invalid age group range
    
if __name__ == '__main__':
    unittest.main()
