# Final-Project

Final AWS Project:

In conclusion, this project demonstrates how AWS services can be used to effectively perform image compression. When an image is uploaded to S3, a lambda function triggers the creation of a task to upload the image to Pucket, and this task is stored in JSON format in the SQS queue. The task is then processed by executors running on EC2 servers, packaged in containers, which compress the image and return it to the S3 bucket. Upon completion of the compression process, a message is sent to the client's email address using SNS.

One of the benefits of this project is that it is entirely implemented through a cloud formation file, making it easy to deploy and use. By leveraging AWS services such as S3, lambda, SQS, EC2, containers, and SNS, this project achieves a highly scalable and efficient solution for image compression. This approach provides a secure and cost-effective solution for clients seeking to compress images in the cloud.

Overall, this project demonstrates how AWS services can be combined to create a reliable and scalable system for image compression in the cloud. By building a system that is easy to deploy and use, the project offers a practical solution for clients seeking to optimize image compression and storage in the cloud. Excellent work on your project!




