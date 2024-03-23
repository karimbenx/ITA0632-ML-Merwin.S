import pandas as pd

def candidate_elimination(training_data):
    specific_h = training_data.iloc[0, :-1]
    general_h = [['?'] * len(specific_h) for _ in specific_h]
    
    for _, instance in training_data.iterrows():
        print("Instance:", instance.tolist())
        if instance.iloc[-1] == 'Malignant(+)':
            specific_h = ['?' if specific_h[i] != val else val for i, val in enumerate(instance.iloc[:-1])]
            general_h = [[val if specific_h[i] == '?' else '?' for i, val in enumerate(general)] for general in general_h]
        else:
            general_h = [[specific_h[i] if specific_h[i] == val else '?' for i, val in enumerate(general)] for general in general_h]
        
        print("Specific Hypothesis:", specific_h)
        print("General Hypotheses:")
        for h in general_h:
            print(pd.Series(h))
        print("-------------------------------")
    
    general_h = [pd.Series(general) for general in general_h if '?' in general]
    return specific_h, general_h

def main():
    training_data = pd.read_csv('C:/Users/Merwin S/OneDrive/Documents/cancer.csv')

    specific_hypothesis, general_hypotheses = candidate_elimination(training_data)
    print("Most specific hypothesis:", specific_hypothesis)
    print("General hypotheses:")
    print("Specific Hypothesis:")
    print(specific_hypothesis)
    print("General Hypotheses:")
    for h in general_hypotheses:
        print(h)

if __name__ == "__main__":
    main()
