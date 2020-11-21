# Competitive_hackathons-skai

The folders contain the code for the 3 tasks assigned.

Techstack used:- 

### Programming language :- 
Python

### Libraries used :- 

* simple_transformers  :- For incorporating pretrained SOTA transformer model trained on german corpus (for task 1)
* sentence_transformer :- For finding the sentence embeddings at email level and clustering (for task 3,2)
* lightgbm             :- To extract feature importances for each class and deciding which services to merge with each other into a single service.
* sklearn              :- validation data preparation and cosine similarity used in task 3


## Snippet for task 2

![alt text](https://github.com/hailsatan13/Competitive_hackathons-skai/blob/main/final_services.PNG)

After application of our algorithm, we were able to cluster similar services. As an example, we showed 4 such clusters above (Cluster 1- EDA_S_BA_2FA,EDA_S_Order Management	,EDA_S_Peripheriegeräte	,EDA_S_Benutzerunterstützung)

Since the clusters were selected based on feature importance from a boosting algorithm as shown below, we feel appropriate clusters have been formed because if two services have similar features which are important to predict them indicates that both the services are of similar type and hence can be clubbed together
<br>
![alt text](https://github.com/hailsatan13/Competitive_hackathons-skai/blob/main/top100features.PNG)

Here top 100 embeddings features are used and we selected the model :- T-Systems-onsite/cross-en-de-roberta-sentence-transformer for embeddings which is the state of the art model for German sentence embeddings

## Brief about Task 3:- 
![alt_text](https://github.com/hailsatan13/Competitive_hackathons-skai/blob/main/task3.JPG)

Here we used sentence similarity based measure called cosine similarity on the sentence embeddings attained to find the best manual group for a new text.


The below segment of code formed the basis of our work that involved matching similarity from a given data and thresholding to form meaningful clusters:- 
![alt_text](https://github.com/hailsatan13/Competitive_hackathons-skai/blob/main/task31.JPG)
