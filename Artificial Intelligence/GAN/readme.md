Readme.md

The project is intended to get an understanding of the 

- Generative Adversarial Network
- Using GAN for Synthetic Data generation
- Understanding the Influence of Synthetic Data on Model Performance

Intention : 

- Read the MNIST dataset
- Create two classes. 5 and NOT 5
- Balance the classes using stratified sampling
    - Lot of data will be discarded in the process
- Train a Neural network model and check its performance
- Create a GAN and train it with MNIST data
- Generate Synthetic data of MNIST using GAN
- Train the model from scratch, this time with more data produced by GAN
- Compare the performance

Findings:
When the data is trained after applying the steps as mentioned in the question, it will create an
unbalanced dataset. The dataset has 315 data points belong to Class 5 and 63687 data points belng
to Class NOT 5. Even if all the predictions are 0, there will be 99.995 % accuracy.
After the data is generated and balanced after using synthesised data from GAN, we can see that
the model starts from a higher loss than in the earlier case and then it converges to better accuracy.
In this case the baseline accuracy is 50%. Hence the second model is a better solution.
The above approach can help in Synthetic data generation, which helps in balancing unbalanced
dataset. It can help in cases where the data collection is tricky or expensive. It also helps to ensure
that the models created are much more eﬀicient in production than a model which is trained using
a unblanced dataset.
