# Patient-Information-Extraction-System

![Screenshot_1](https://github.com/user-attachments/assets/61d0adff-f22f-4b7c-a3c5-22ebd863c831)

This project is an AWS Lambda function that extracts patient information from documents stored in Amazon S3. It uses Amazon Textract to read and analyze the documents, capturing data such as patient name, age, and disease. The extracted information is then saved in a DynamoDB table for easy access and management.

•	<u><strong>Automatic Processing:</u></strong> Activates when new documents are uploaded to S3.<br>
•<u><strong>	Data Extraction:</u></strong> Retrieves patient details from various document formats.<br>
•<u><strong>	Storage:</u></strong> Saves extracted information in DynamoDB for organization.

<u><strong>Services Used:</u></strong> AWS Lambda, Amazon S3, Amazon Textract, Amazon DynamoDB

# Steps Taken:<br>
<strong>1) Creating an S3 bucket (uploadmedical-images):</strong>

![1) S3 bucket](https://github.com/user-attachments/assets/320177b5-003b-4d74-93c6-4ff8408b36b7)

<strong><br>2) Creating lambda python function (retrievimage):</strong><br>
<strong>Note: python code is available in the repository </strong>
![2) lambda function](https://github.com/user-attachments/assets/245a1e38-1a16-4884-a559-54914d0a4491)

<strong><br>3) IAM role for lambda (S3, DynamoDB, Textract, Cloudwatch Log Access):</strong><br>
This policy enables the Lambda function to interact with the specified AWS services and resources effectively.
![4) full dynamo access, s3 fullaccess, texract policy](https://github.com/user-attachments/assets/99f893da-9f44-4d1f-87d5-99bf99d45bf1)

<strong><br>4) Adding S3 event notification trigger:</strong><br>
As soon as the user uploads any image file in the S3 bucket. The lambda function gets notified immediately and will start performing the task of retrieving the image and sending it to textract for extraction of text.
![3) s3trigger](https://github.com/user-attachments/assets/47fd68f8-b15c-4a74-b5ad-b4975033f9e8)

<strong><br>5) Creating DynamoDB table (patientdetails):</strong>
![5) dynamodb table](https://github.com/user-attachments/assets/4be7a2d8-a4c5-4628-b7ac-1303916b63d9)

<strong><br>6) Testing by uploading the image:</strong>
# [Test image]
![john_doe](https://github.com/user-attachments/assets/ceeca757-a627-48af-8729-3b053bbc5d39)

![6) file upload](https://github.com/user-attachments/assets/e6b3ef8d-124b-4170-8bcb-9efb5fcfd46e)

<strong><br>7) Successfully logging details in Cloudwatch log:</strong>
![7) logdata](https://github.com/user-attachments/assets/46abbc37-e021-405b-8182-afd6010aa6fc)

<strong><br>7) Successfully data is written to DyanamoDB:</strong>

![8) dynamodb](https://github.com/user-attachments/assets/84b57d7d-6943-495d-a3ab-73b0c96b5410)










