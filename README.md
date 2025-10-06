# S3 CSV Data Processing Lambda

## Overview

This AWS Lambda function automatically processes CSV files uploaded to an S3 bucket, generates a report, saves it back to S3, and sends notifications via SNS.

The project is organized in a modular structure for maintainability and ease of testing.

## **Features**

- Automatically triggered when a CSV file is uploaded to the `uploads/` folder in S3.
- Validates that only CSV files in the correct folder are processed.
- Parses CSV data and extracts column names and row count.
- Generates a formatted text report including a sample of the first 5 rows.
- Saves the report to a `processed/` folder in S3.
- Sends a success/failure notification via AWS SNS.

---

## **Project Structure**

```
s3-data-pipeline/
│
├── lambda_function.py        # Lambda entry point
├── processor/
│   ├── __init__.py
│   ├── s3_handler.py         # S3 upload/download logic
│   ├── csv_processor.py      # CSV parsing and utilities
│   ├── report_generator.py   # Report generation logic
│   └── sns_notifier.py       # SNS notification logic
├── requirements.txt          # Python dependencies
└── README.md
```

---

## **Setup Instructions**

1. **Clone the repository**

```bash
git clone <repository-url>
cd s3-data-pipeline
```

2. **Install dependencies** (if testing locally)

```bash
pip install -r requirements.txt
```

> Note: `boto3` is preinstalled in AWS Lambda.

3. **Set environment variables** in Lambda

- `SNS_TOPIC_ARN` : ARN of the SNS topic for notifications

4. **Upload Lambda code** to AWS

- You can zip the folder and upload it via the AWS Lambda console, or use a deployment pipeline.

---

## **Usage**

1. Upload a CSV file to the S3 bucket under the `uploads/` folder.
2. Lambda triggers automatically.
3. Processed report is saved to `processed/<filename>_report.txt`.
4. SNS notification is sent with processing details.

---

## **Example Flow**

```
uploads/my_data.csv  --> Lambda triggered
   ↓
  CSV parsed, rows counted
   ↓
  Report generated and saved to S3
   ↓
  SNS notification sent
```

---

## **Contributing**

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/new-feature`.
3. Make your changes and commit: `git commit -m "Add feature"`.
4. Push to your branch: `git push origin feature/new-feature`.
5. Submit a pull request.

---

## **License**

This project is licensed under the MIT License.
