'''
This code example clusters sentences using PyTorch and BERT embeddings.
I could also try: https://huggingface.co/sentence-transformers/stsb-xlm-r-multilingual 
'''

import torch
from transformers import BertTokenizer, BertModel
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

THR = 0.6
PLOT = False

# Load pre-trained BERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# --------------------
# Define sentences to be clustered
# sentences = ["The quick brown fox jumped over the lazy dog.",
#              "The lazy dog was not very quick.",
#              "Four score and seven years ago our fathers brought forth on this continent a new nation, conceived in liberty, and dedicated to the proposition that all men are created equal.",
#              "This sentence is completely unrelated to the others."]

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

# Tokenize and encode sentences using BERT tokenizer
tokens = [tokenizer.encode(sentence, add_special_tokens=True) for sentence in sentences]
max_len = max([len(token) for token in tokens])
padded_tokens = [token + [0]*(max_len-len(token)) for token in tokens]
attention_masks = [[float(i > 0) for i in token] for token in padded_tokens]

# Convert input to PyTorch tensors
input_ids = torch.tensor(padded_tokens)
attention_masks = torch.tensor(attention_masks)

# Compute BERT embeddings
with torch.no_grad():
    outputs = model(input_ids, attention_mask=attention_masks)

embeddings = outputs[0][:, 0, :].numpy()


clusters_range = range(1, len(sentences) + 1)
inertias = []
for k in clusters_range:
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(embeddings)
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
kmeans.fit(embeddings)

# Print clusters
print('')
print('Results:')
for i in range(num_clusters):
    cluster = np.where(kmeans.labels_ == i)[0]
    print("Cluster ", i+1, ":")
    for j in cluster:
        print("  ", sentences[j])

if PLOT:
    plt.plot(clusters_range, inertias, marker='o')
    plt.xlabel('Number of Clusters (k)')
    plt.ylabel('Sum of Squared Distances')
    plt.title('Elbow Curve')
    plt.show()
