<img src="/doc/wordcloud.png" alt="wordcloud.png">


# Synthetic data generation model using GAN for associative models

This model is one of the first, if not the first, to generate synthetic data in associative models.

I present an example of a table in the subject-verb-object format. For example, the subject can be a client or a company, the verb can be an action like “purchase”, “payment”, “return”, and the object can be a product or service.

<img src="/doc/img/table_svo.png" alt="table_svo">

You can learn more about <a href="https://habr.com/ru/companies/deepfoundation/articles/804617/">associative data models</a> here.

<img src="/doc/img/assiciative_model.png" alt="assiciative_data_model">


## Why you need this model and what it does?

Examples of Uses:
```
1. testing algorithms for recommender systems
   (specifically - Testing an algorithm for a marketplace to ensure that the system correctly suggests related products (e.g., phone cases along with smartphones)))
2. training ML models when data is scarce
   (specifically - Bank generates “fake” transactions that mimic fraud schemes to train the neural network to recognize them)
3. medical research
   (specifically - Investigating the relationship between genetic markers and diseases when real data is insufficient due to the rarity of the case).
4. User behavior simulation
   (specifically - Developing a mobile application where synthetic data helps to test how often users will use a certain button given their typical scenarios)
5. Training employees on realistic scenarios
   (specifically - Training retail analysts on synthetic shopping data where there are hidden patterns (e.g. seasonal demand for goods))
6. Academic experiments
   (specifically - Investigating the effectiveness of new associative algorithms on synthetic data with pre-known relationships (e.g., between items in a shopping cart)).
```

A key advantage of the model:
It preserves associative relationships (e.g., “users who buy X often take Y”), which makes synthetic data not just random, but practically applicable to tasks where hidden patterns are important. This distinguishes it from simply generating random numbers or context-free data.
