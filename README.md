# Final-Project
Final AWS Project

In conclusion, this project demonstrates how AWS services can be leveraged to efficiently perform image compression. When an image is uploaded to S3, a lambda function triggers the creation of a task to upload the image to Pucket, and this task is stored in JSON format in the SQS queue. The task is then processed by executors running on EC2 servers, packaged in containers, which compress the image and return it to the S3 bucket. Upon completion of the compression process, a message is sent to the client's email address using SNS.

By utilizing AWS services like S3, lambda, SQS, EC2, containers, and SNS, the project achieves a highly scalable and efficient solution for image compression. This approach provides a secure and cost-effective solution for clients seeking to compress images. Overall, this project demonstrates how AWS services can be combined to achieve a reliable and scalable system for image compression in the cloud.
