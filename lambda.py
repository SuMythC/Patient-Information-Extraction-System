import json
import boto3
import logging

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize DynamoDB and Textract clients
dynamodb = boto3.resource('dynamodb')
textract = boto3.client('textract')

# Name of the DynamoDB table
DYNAMODB_TABLE_NAME = '<YOUR_DYNAMODB_TABLENAME>'  # Replace with your actual DynamoDB table name

def lambda_handler(event, context):
    logger.info("Event: %s", json.dumps(event))
    
    # Get the bucket name and object key from the event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']
    
    logger.info("Bucket: %s, Key: %s", bucket_name, object_key)
    
    try:
        # Call Textract to analyze the document
        response = textract.analyze_document(
            Document={
                'S3Object': {
                    'Bucket': bucket_name,
                    'Name': object_key
                }
            },
            FeatureTypes=['TABLES', 'FORMS']  # Customize feature types as needed
        )

        # Extract the text blocks from the response
        extracted_text = []
        for item in response['Blocks']:
            if item['BlockType'] == 'LINE':
                extracted_text.append(item['Text'])

        logger.info("Extracted Text: %s", extracted_text)

        # Parse patient information
        patient_name = None
        age = None
        disease = None
        
        for line in extracted_text:
            if "Patient name:" in line:
                patient_name = line.split(":")[1].strip()
            elif "Age:" in line:
                age = line.split(":")[1].strip()
            elif "Disease:" in line:
                disease = line.split(":")[1].strip()

        # Format the message
        if patient_name and age and disease is not None:
            message = f"{patient_name} is {age} years old and has {disease} disease."
            logger.info(message)
        else:
            logger.warning("Some patient information is missing.")

        # Store information in DynamoDB
        if patient_name and age and disease is not None:
            table = dynamodb.Table(DYNAMODB_TABLE_NAME)
            table.put_item(
                Item={
                    'PatientName': patient_name,  # Ensure this matches the primary key of your table
                    'Age': age,
                    'Disease': disease,
                    'DocumentKey': object_key  # Optionally store the S3 object key for reference
                }
            )
            logger.info("Patient information added to DynamoDB.") 
        else:
            logger.warning("No patient information was added to DynamoDB due to missing data.")

        return {
            'statusCode': 200,
            'body': json.dumps({
                'text': extracted_text,
                'message': message if patient_name and age and disease else 'Incomplete data'
            })
        }
    except Exception as e:
        logger.error("Error processing file: %s", str(e))
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            })
        }