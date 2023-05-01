# T-distributed Stochastic Neighbor Embedding [t-SNE]

''' 
tSNE is basically dead by now 

tSNE can not work with high-dimensional data directly

tSNE consumes too much memory
'''

"""
At a high level, t-SNE constructs a probability distribution for the high-dimensional 
samples in such a way that similar samples have a high likelihood of being picked 
while dissimilar points have an extremely small likelihood of being picked. 
Then, t-SNE defines a similar distribution for the points in the low-dimensional embedding. 
Finally, t-SNE minimizes the Kullback–Leibler divergence between the two distributions with 
respect to the locations of the points in the embedding.

t-SNE takes a high dimensional dataset and reduces it to a low dimensional graph that retains a lot of the original information.
"""

tsne = TSNE()
params = {'angle': 0.5, 'early_exaggeration': 12.0, 'init': 'warn', 'learning_rate': 'warn', 'method': 'barnes_hut', 
          'metric': 'euclidean', 'min_grad_norm': 1e-07, 'n_components': 2, 'n_iter': 1000, 'n_iter_without_progress': 300, 
          'n_jobs': None, 'perplexity': 30.0, 'random_state': None, 'square_distances': 'legacy', 'verbose': 0}
tsne.set_params(**params)

X_train = tsne.fit_transform(X_train)
X_test = tsne.fit_transform(X_test)