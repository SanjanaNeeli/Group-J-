# Group J

## Title

Representing Visual Learning from Spatial-Temporal Sequences in the Mouse Primary Visual Cortex Using Multi-Class Classification Machine Learning and Graphical Analysis

## Project Question

How can we model the firing of neurons in the visual cortex of a mouse upon recognizing a stimulus using machine learning? 
Furthermore, after the model is finished, will it be responsive to an image despite various orderings of visual patterns or not? (If it is not, we can then prove that the visual cortex likely uses contextual visual information in image recognition instead of an expected "feed-in, feed-out" visual response.

## Project Description

The primary visual cortex (V1) has been extensively studied in the context of sensory processing but less so with respect to temporal processing, including the formation of memories specific to the temporal and ordinal characteristics of its input. The formation of spatiotemporal memories is critical to the ability of an organism to predict outcomes based on experience and detect potentially important deviations from expectations. To study this phenomenon, we used two-photon calcium imaging data from the primary visual cortex of awake mice while viewing sequential stimuli, including one sequence that had been presented to the mice over five days as well as variations that recorded the images presented. Our intended goal was to describe how V1 represents stimuli presented in  the context of a learned sequence with its representation to the same stimuli in an unlearned temporal context.

We initially compared the activity in V1 during recognition of known visual patterns and exposure to novel patterns by graphing activity patterns recorded from the two situations. Then, we recorded the global average activity among all cells and after comparing the two plots, we found a significant difference between the learned sequence and its variations. To build on these results, we used (1) logistic regression, a multi-class classification (2) Naive Bayes (3) XG Boost Classifier to determine if a model trained on an ordered pattern could accurately identify the ordered and disordered testing data. 

## Model Templates/Journal Articles

### ML template: 
https://acadgild.com/blog/logistic-regression-multiclass-classification

### Key text:
Decoding Neural Responses in Mouse Visual Cortex through a Deep Neural Network: https://arxiv.org/ftp/arxiv/papers/1911/1911.05479.pdf

### Background Reading: 

Number detectors spontaneously emerge in a deep neural network designed for visual object recognition: https://advances.sciencemag.org/content/5/5/eaav7903

How well do deep neural networks trained on object recognition characterize the mouse visual system? https://openreview.net/pdf?id=rkxcXmtUUS

High precision coding in mouse visual cortex: https://www.biorxiv.org/content/10.1101/679324v1.full.pdf

Neuronal Activities in the Mouse Visual Cortex Predict Patterns of Sensory Stimuli: https://sci-hub.tw/https://link.springer.com/article/10.1007/s12021-018-9357-1#

Decoding Neural Responses in Mouse Visual Cortex through a Deep Neural Network: https://arxiv.org/pdf/1911.05479.pdf

High-dimensional geometry of population responses in visual cortex: Carsen Stringer, Marius Pachitariu, Nicholas Steinmetz, Matteo carandini & Kenneth D. Harris

Learned spatiotemporal sequence recognition and prediction in primary visual cortex: Jeffrey P Gavornik & Mark F Bear

Architecture, Function, and Assembly of the Mouse Visual System: Tania A. Seabrook,Timothy J. Burbridge, Michael C. Crair, and Andrew D. Huberman



