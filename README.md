# Patient-Information-Extraction-System
This project is an AWS Lambda function that extracts patient information from documents stored in Amazon S3. It uses Amazon Textract to read and analyze the documents, capturing data such as patient name, age, and disease. The extracted information is then saved in a DynamoDB table for easy access and management.
•	Automatic Processing: Activates when new documents are uploaded to S3.
•	Data Extraction: Retrieves patient details from various document formats.
•	Storage: Saves extracted information in DynamoDB for organization.
Services Used: AWS Lambda, Amazon S3, Amazon Textract, Amazon DynamoDB
