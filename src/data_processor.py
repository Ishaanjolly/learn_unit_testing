import pandas as pd 

class DataProcessor: 
    def __init__(self):
        self.data = None
        
    def load_data(self):
        """Simulate loading data (would be file/database in real code)"""
        self.data = pd.DataFrame({
            "product": ["A", "B", "C"],
            "price": [10, 20, 15],
            "quantity": [3, 5, 2]
        })
        return self.data
    def calculate_total_sales(self): 
        if self.data is None:
            self.load_data()
        self.data['sales'] = self.data['price'] * self.data['quantity']
    
    def get_expensive_products(self, threshold = 10):  
        return self.data[self.data['price'] > threshold]

