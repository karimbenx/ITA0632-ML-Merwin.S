import pandas as pd

def find_s(training_data):
    hypothesis = ['0'] * (len(training_data.columns) - 1)
    for _, instance in training_data.iterrows():
        if instance.iloc[-1] == 'Malignant(+)':
            for i, val in enumerate(instance.iloc[:-1]):
                if hypothesis[i] == '0':
                    hypothesis[i] = val
                elif hypothesis[i] != val:
                    hypothesis[i] = '?'
    return hypothesis

def main():
    training_data = pd.read_csv('C:/Users/Merwin S/OneDrive/Documents/cancer.csv')

    print("Training Data:")
    print(training_data)

    specific_hypothesis = find_s(training_data)
    print("Most specific hypothesis:", specific_hypothesis)

if __name__ == "__main__":
    main()

