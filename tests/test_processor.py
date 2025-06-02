import sys 
from pathlib import Path
import unittest
from unittest.mock import patch, MagicMock

sys.path.append(str(Path(__file__).parent.parent))

from src.data_processor import DataProcessor

class TestDataProcessor(unittest.TestCase):
    def setUp(self):
        """Set up a DataProcessor instance for testing."""
        self.processor = DataProcessor()
        self.processor.load_data()

    def test_load_data(self):
        """Test if data is loaded correctly."""
        self.assertIsNotNone(self.processor.data)
        self.assertEqual(len(self.processor.data), 3)

    def test_calculate_total_sales(self):
        """Test if total sales are calculated correctly."""
        self.processor.calculate_total_sales()
        self.assertIn('sales', self.processor.data.columns)
        self.assertEqual(self.processor.data['sales'].sum(), 85)

    def test_get_expensive_products(self):
        """Test if expensive products are filtered correctly."""
        expensive_products = self.processor.get_expensive_products(15)
        self.assertEqual(len(expensive_products), 2)
        self.assertTrue(all(expensive_products['price'] > 15))
        
    @patch('src.data_processor.load_data')
    def test_load_data_mocked(self, mock_load_data):  
        # 1. Create your test DataFrame
        test_df = pd.DataFrame({
            "product": ["A", "B", "C"],
            "price": [10, 20, 15],
            "quantity": [3, 5, 2]
        })
        
        # 2. Configure mock to return this DataFrame
        mock_load_data.return_value = test_df
        
        # 3. Now let's inspect:
        print("\n=== MOCK OBJECT ===")
        print(type(mock_load_data))          # <class 'unittest.mock.MagicMock'>
        print(mock_load_data)                # <MagicMock name='load_data' id='...'>
        
        print("\n=== RETURN VALUE ===")
        print(type(mock_load_data.return_value))  # <class 'pandas.core.frame.DataFrame'>
        print(mock_load_data.return_value)        # Your DataFrame contents!
        
        # 4. When called, it returns your DataFrame
        processor = DataProcessor()
        result = processor.load_data()  # Calls the mock
        
        print("\n=== CALL RESULT ===")
        print(result)  # Same as test_df
        
        
if __name__ == '__main__':
    unittest.main()
        

