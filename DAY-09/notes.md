1. What is a Serializer?
   A Serializer in Django REST Framework converts complex Python objects (like Django models) into JSON and converts JSON back into Python objects.

2. Why are Serializers needed in APIs?
   APIs exchange data mainly in JSON format, while Django uses Python objects. Serializers act as a bridge between them.

3. Serialization vs Deserialization
   Serialization: Python object → JSON
   Deserialization: JSON → Python object

4. What is a ModelSerializer?
   A ModelSerializer is a shortcut serializer that automatically creates fields and validations based on a Django model.

5. How does DRF convert Django Model objects into JSON?
   DRF takes a model instance, passes it through a serializer, and the serializer returns data that is rendered as JSON in the API response.

6. Role of Validation in APIs
   Validation checks whether incoming data is correct, complete, and follows required rules before saving it to the database.

7. What is the difference between a QuerySet and serialized data?
   QuerySet: Collection of Django model objects.
   Serialized data: JSON-compatible Python data (dictionary/list) ready to be sent in an API response.

8. Why should APIs return proper error messages?
   Proper error messages help users understand what went wrong and how to fix their request.

9. Which part of DRF feels easier than plain Django?
  ModelSerializer feels easier because it automatically creates fields and validations, reducing boilerplate code.