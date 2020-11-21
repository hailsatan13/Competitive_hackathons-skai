import numpy as np
import pandas as pd

model1=pd.read_csv("sample_trial_german_bert_manual_16_512.csv")

model2=pd.read_csv("xlmroberta_trial_manual1.csv")

model3=pd.read_csv("xlmroberta_trial_manual.csv")

output_df=pd.DataFrame(model3['Id'])

output_df['Predicted']=np.where((model3['Predicted']==model2['Predicted']),model3['Predicted'],
                  (np.where((model1['Predicted']==model2['Predicted']),model2['Predicted'],
                  (np.where((model1['Predicted']==model3['Predicted']),model3['Predicted'],
                  (np.where((model1['Predicted']==model2['Predicted']) & (model3['Predicted']==model2['Predicted']) & (model3['Predicted']==model1['Predicted']), model1['Predicted'],model3['Predicted'] )))))))


output_df.to_csv("blend_top3_manual.csv",index=False)

