'''
https://huggingface.co/sentence-transformers/stsb-xlm-r-multilingual
'''

from transformers import AutoTokenizer, AutoModel
import torch

from sklearn.cluster import KMeans
import numpy as np


THR = 0.6

#Mean Pooling - Take attention mask into account for correct averaging
def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0] #First element of model_output contains all token embeddings
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)


# Sentences we want sentence embeddings for
# sentences = ['This is an example sentence', 'Each sentence is converted']

sentences = [
    "The patient is experiencing symptoms of fever, cough, and fatigue.",
    "The doctor prescribed antibiotics to treat the bacterial infection.",
    "The MRI scan revealed a fracture in the patient's left tibia.",
    "The surgeon performed a successful heart bypass surgery on the patient.",
    "The laboratory test confirmed the presence of elevated cholesterol levels.",
    "The weather forecast predicts clear skies and sunshine for tomorrow.",
    "There is a high chance of rain showers and thunderstorms in the afternoon.",
    "Strong winds are expected to reach speeds of up to 40 miles per hour.",
    "A heatwave warning has been issued, with temperatures expected to soar above 90 degrees Fahrenheit.",
    "A cold front is moving in, bringing with it a drop in temperatures and the possibility of snowfall.",
    "I enjoy cooking Italian dishes like pasta and pizza.",
    "Sushi is one of my favorite foods, especially the salmon rolls.",
    "I love indulging in a rich, creamy chocolate cake for dessert.",
    "Grilling burgers and hot dogs is a classic choice for summer barbecues.",
    "Fresh fruits and vegetables are essential for a healthy diet.",
    "I love spending time in my cozy home, especially during the winter.",
    "Home is where the heart is, and for me, it's a place of comfort and relaxation.",
    "I take pride in decorating my home with a personal touch and creating a warm atmosphere.",
    "The government implemented new tax policies to stimulate economic growth.",
    "There is an ongoing debate regarding immigration reform and border control.",
    "Political parties are campaigning for the upcoming elections, promising various policy changes.",
    "The president delivered a speech addressing the nation's concerns about healthcare and education.",
    "Protests erupted in the capital city demanding political transparency and accountability.",
    "International relations between countries have become strained due to trade disputes."
]

# Load model from HuggingFace Hub
tokenizer = AutoTokenizer.from_pretrained('sentence-transformers/stsb-xlm-r-multilingual')
model = AutoModel.from_pretrained('sentence-transformers/stsb-xlm-r-multilingual')

# Tokenize sentences
encoded_input = tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')

# Compute token embeddings
with torch.no_grad():
    model_output = model(**encoded_input)

# Perform pooling. In this case, max pooling.
sentence_embeddings = mean_pooling(model_output, encoded_input['attention_mask'])

print("Sentence embeddings:")
print(sentence_embeddings)



clusters_range = range(1, len(sentence_embeddings) + 1)
inertias = []
for k in clusters_range:
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(sentence_embeddings)
    inertias.append(kmeans.inertia_)


# ideal number of clusters is where >= THR of interia is captured
i = frac_inertia = inertia_so_far = 0
all_inertias = sum(inertias)
while inertia_so_far / all_inertias < THR:
    inertia_so_far += inertias[i]
    i += 1

# Cluster embeddings using KMeans
num_clusters = i
kmeans = KMeans(n_clusters=num_clusters)
kmeans.fit(sentence_embeddings)

# Print clusters
print('')
print('Results:')
for i in range(num_clusters):
    cluster = np.where(kmeans.labels_ == i)[0]
    print("Cluster ", i+1, ":")
    for j in cluster:
        print("  ", sentences[j])
