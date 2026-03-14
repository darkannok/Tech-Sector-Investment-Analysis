import pandas as pd
import matplotlib.pyplot as plt

class TechSectorAnalysis:
    def __init__(self, apple_data, microsoft_data):
        self.apple_data = apple_data
        self.microsoft_data = microsoft_data

    def compare_revenue(self):
        plt.bar(['Apple', 'Microsoft'], [self.apple_data['revenue'], self.microsoft_data['revenue']])
        plt.title('Revenue Comparison')
        plt.ylabel('Revenue in USD')
        plt.show()

# Example usage
apple_data = {'revenue': 274515}
 microsoft_data = {'revenue': 143015}
 analysis = TechSectorAnalysis(apple_data, microsoft_data)
 analysis.compare_revenue()