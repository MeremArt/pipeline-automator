# Automated S3 Data Pipeline

## Overview

This project demonstrates a production-ready serverless architecture that automatically processes files uploaded to Amazon S3. The pipeline handles both structured data (CSV) and images, performing intelligent processing based on file type.

## **Features**

✅ Dual File Type Support: Automatically detects and processes CSV files and images
✅ CSV Processing: Parses data, generates statistics, and creates formatted reports
✅ Image Resizing: Creates multiple optimized versions (thumbnail, medium, large)
✅ Real-time Notifications: Instant email alerts via Amazon SNS
✅ Serverless Architecture: Zero server management, infinite scalability
✅ Cost Effective: Pay-per-execution pricing (AWS Free Tier compatible)
✅ Production Ready: Includes error handling, logging, and monitoring

---

## **Project Structure**

```
User Upload → S3 Bucket (uploads/) → Lambda Function → Process File → S3 (processed/) → SNS → Email
                  ↓
            Event Trigger
                  ↓
         [File Type Detection]
                  ↓
        ┌─────────┴─────────┐
        ↓                   ↓
   CSV Processor      Image Processor
        ↓                   ↓
   Text Report       Resized Images (3 sizes)
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

## **Contributing**

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/new-feature`.
3. Make your changes and commit: `git commit -m "Add feature"`.
4. Push to your branch: `git push origin feature/new-feature`.
5. Submit a pull request.

---

## **License**

This project is licensed under the MIT License.
