# 🚀 Automated S3 Data Pipeline

## 📝 Overview

This project showcases a **production-ready serverless pipeline** built on **AWS**, designed to automatically process files uploaded to **Amazon S3**.  
Whether it’s structured data (CSV) or unstructured image files, the pipeline intelligently routes and processes them—no servers, no stress.

Perfect for **developers**, **data engineers**, or anyone who wants to automate file processing like a pro.

---

## 🌟 Features

✅ **Dual File Type Support** – Instantly detects and processes both CSV files and images  
✅ **CSV Processing** – Parses data, generates statistics, and outputs formatted reports  
✅ **Image Resizing** – Automatically creates optimized versions: `thumbnail`, `medium`, and `large`  
✅ **Real-time Notifications** – Sends email alerts via **Amazon SNS** when processing completes  
✅ **Serverless Architecture** – Zero server management, infinite scalability  
✅ **Cost Effective** – Pay-per-execution (AWS Free Tier friendly)  
✅ **Production Ready** – Includes error handling, logging, and monitoring baked in

---

## 🧠 Architecture

```

User Upload → S3 Bucket (uploads/) → Lambda Function → Process File → S3 (processed/) → SNS → Email
↓
Event Trigger
↓
[File Type Detection]
↓
┌─────────┴─────────┐
↓ ↓
CSV Processor Image Processor
↓ ↓
Text Report Resized Images (3 sizes)

```

---

## 🛠 Setup Instructions

1. **Clone the repository**

```bash
git clone <repository-url>
cd s3-data-pipeline
```

2. **Install dependencies** (for local testing)

```bash
pip install -r requirements.txt
```

> `boto3` is already available in AWS Lambda environments.

3. **Configure Environment Variables** in Lambda:

- `SNS_TOPIC_ARN`: The ARN of your SNS topic for notifications.

4. **Deploy Lambda Code** to AWS:

- Zip the folder and upload via the AWS Lambda Console,
  **or** integrate with your preferred CI/CD pipeline.

---

## ⚡ Usage

1. Upload a CSV file or image to the S3 bucket under the `uploads/` folder.
2. Lambda triggers automatically on upload.
3. Depending on file type:

   - **CSV** → Parsed → Stats generated → Saved as `processed/<filename>_report.txt`
   - **Image** → Resized into `thumbnail`, `medium`, `large` → Saved to `processed/`

4. SNS sends you an email with processing details—like magic ✨

---

## 🧠 Figma Design

Take a peek at the **architecture and flow** here:
👉 [**View Figma Design**] https://lnkd.in/dauzaqxf

---

## 📽 Demo Video

See the pipeline in action:
👉 [**Watch the Demo on YouTube**] https://lnkd.in/dzYt9Haz

---

## 🤝 Contributing

1. Fork the repository.
2. Create a feature branch:

```bash
git checkout -b feature/new-feature
```

3. Make your changes and commit:

```bash
git commit -m "Add new feature"
```

4. Push to your branch:

```bash
git push origin feature/new-feature
```

5. Open a **Pull Request**.

---

## 📄 License

This project is licensed under the **MIT License**.
Feel free to build on it, remix it, and ship cool things 🚢
