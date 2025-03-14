# Synthetic data generation model using GAN for associative models

This model is one of the first, if not the first, to generate synthetic data in associative models.

How it works:
· Associative rules are used to identify key relationships in the data (e.g., between items in transactions).
· GAN is trained on real data to generate synthetic transactions that preserve these associative relationships.
· This is useful for creating test data or for augmenting data in machine learning tasks.

I present an example of a training table in the subject-verb-object format. For example, the subject can be a client or a company, the verb can be an action like “purchase”, “payment”, “return”, and the object can be a product or service.

<img src="/doc/img/table_svo.png" alt="table_svo">

You can learn more about <a href="https://habr.com/ru/companies/deepfoundation/articles/804617/">associative data models</a> here

<img src="assiciative_model.png" alt="assiciative_data_model">
