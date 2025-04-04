<img src="/doc/img/wordcloud-Photoroom.png" alt="wordcloud" height="500">


# Synthetic data generation model using GAN for associative models

This model is one of the first, if not the first, to generate synthetic data in associative models.

I give an example of a transaction table in subject-verb-object format. For example, the subject could be a customer or a company, the verb could be an action like “purchase”, “payment”, “return”, and the object could be a product or service. There are also optional date and amount columns, and you can input three mandatory columns or with optional columns

<img src="/doc/img/table_svo.png" alt="table_svo">

You can learn more about <a href="https://habr.com/ru/companies/deepfoundation/articles/804617/">associative data models</a> here.

<img src="/doc/img/assiciative_model.png" alt="assiciative_data_model">


## Why you need this model and what it does?

A key advantage of the model:
It preserves associative relationships (e.g., “users who buy X often take Y”), which makes synthetic data not just random, but practically applicable to tasks where hidden patterns are important. This distinguishes it from simply generating random numbers or context-free data.
