# Patient Information Extraction System
This project implements an **AWS Lambda function** that extracts patient information from documents stored in **Amazon S3**. The system uses **Amazon Textract** to analyze documents, extracting key details such as patient name, age, and disease, which are then saved to an **Amazon DynamoDB** table for further use and management.
![Screenshot_1](https://github.com/user-attachments/assets/61d0adff-f22f-4b7c-a3c5-22ebd863c831)

## Features
- **Automatic Processing**: The Lambda function is triggered whenever new documents are uploaded to the S3 bucket.
- **Data Extraction**: Extracts key patient details (name, age, disease) from uploaded medical documents.
- **Storage**: The extracted data is saved in a DynamoDB table, making it easy to access and manage patient information.

## Services Used
- **AWS Lambda**
- **Amazon S3**
- **Amazon Textract**
- **Amazon DynamoDB**
- **Amazon CloudWatch** (for logging)

## Workflow

### 1. **Creating an S3 Bucket**
The S3 bucket, named `uploadmedical-images`, is used to store the images from which patient details will be extracted.

![1) S3 Bucket](https://github.com/user-attachments/assets/320177b5-003b-4d74-93c6-4ff8408b36b7)

### 2. **Creating Lambda Python Function**
The Lambda function `retrievimage` processes the images uploaded to S3. It uses **Amazon Textract** to extract text data from images and then stores the relevant information in DynamoDB.

**Note:** The Python code for the Lambda function is available in the repository.

![2) Lambda Function](https://github.com/user-attachments/assets/245a1e38-1a16-4884-a559-54914d0a4491)

### 3. **IAM Role for Lambda**
An IAM role with the necessary permissions for Lambda is created, allowing it to access **S3**, **DynamoDB**, **Textract**, and **CloudWatch Logs**. This ensures the Lambda function can interact with all required AWS services.

![IAM Role for Lambda](https://github.com/user-attachments/assets/99f893da-9f44-4d1f-87d5-99bf99d45bf1)

### 4. **S3 Event Notification Trigger**
An event notification trigger is set up on the S3 bucket. When a new image is uploaded, the Lambda function is automatically triggered to start processing the image and sending it to **Amazon Textract** for text extraction.

![S3 Trigger](https://github.com/user-attachments/assets/47fd68f8-b15c-4a74-b5ad-b4975033f9e8)

### 5. **Creating DynamoDB Table (patientdetails)**
A DynamoDB table called `patientdetails` is created to store the extracted patient information.

![DynamoDB Table](https://github.com/user-attachments/assets/4be7a2d8-a4c5-4628-b7ac-1303916b63d9)

### 6. **Testing: Uploading Image**
A test image (e.g., a patient's medical report) is uploaded to the S3 bucket. This triggers the Lambda function, which processes the image and extracts the relevant details.

**Test Image:**
![Test Image](https://github.com/user-attachments/assets/ceeca757-a627-48af-8729-3b053bbc5d39)

**File Upload Process:**
![File Upload](https://github.com/user-attachments/assets/e6b3ef8d-124b-4170-8bcb-9efb5fcfd46e)

### 7. **Logging Details in CloudWatch**
The Lambda function successfully logs data to **Amazon CloudWatch** for monitoring and troubleshooting purposes.

![CloudWatch Log](https://github.com/user-attachments/assets/46abbc37-e021-405b-8182-afd6010aa6fc)

### 8. **Data Written to DynamoDB**
Once the patient details are extracted, they are stored in the **DynamoDB table** for easy access and management.

![DynamoDB Data](https://github.com/user-attachments/assets/84b57d7d-6943-495d-a3ab-73b0c96b5410)
