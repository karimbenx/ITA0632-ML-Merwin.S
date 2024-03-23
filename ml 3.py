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

def candidate_elimination(training_data):
    specific_h = training_data.iloc[0, :-1]
    general_h = [['?'] * len(specific_h) for _ in specific_h]
    
    for idx, instance in training_data.iterrows():
        print("\nInstance:", instance.tolist())
        if instance.iloc[-1] == 'Malignant(+)':
            specific_h = ['?' if specific_h[i] != val else val for i, val in enumerate(instance.iloc[:-1])]
            general_h = [[val if specific_h[i] == '?' else '?' for i, val in enumerate(general)] for general in general_h]
        else:
            general_h = [[specific_h[i] if specific_h[i] == val else '?' for i, val in enumerate(general)] for general in general_h]
        
        print("Specific Hypothesis:", specific_h)
        print("General Hypotheses:")
        for h in general_h:
            print(pd.Series(h))
    
    general_h = [pd.Series(general) for general in general_h if '?' in general]
    return specific_h, general_h

def main():
    training_data = pd.read_csv('C:/Users/Merwin S/OneDrive/Documents/cancer.csv')

    print("Training Data:")
    print(training_data)

    specific_hypothesis_find_s = find_s(training_data)
    print("\nMost specific hypothesis using FIND-S:", specific_hypothesis_find_s)

    specific_hypothesis_ce, general_hypotheses_ce = candidate_elimination(training_data)
    print("\nMost specific hypothesis using CE:", specific_hypothesis_ce)
    print("General hypotheses using CE:")
    for h in general_hypotheses_ce:
        print(h)

if __name__ == "__main__":
    main()
