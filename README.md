# AFB Lambda subscriber

 This is a small project I built that helped me and my girlfriend find a new apartment through AF bostäder. 
 Manually going to the AFB website was tedious (not to mention time consuming) so I decided to automate it with a serverless function.
This function periodically checked their site for apartments I deemed "interesting," and sent me and my girlfriend an email if there were any new ones. 

I was originally running this as a cron job on my personal laptop, but since that didn't provide sufficient uptime I decided to throw it on AWS instead.

## AWS services used
- Lambda to actually run the code
- SAM to develop said Lambda locally
- EventBridge to set up a cron job
- DynamoDB to keep track of previously seen apartments to avoid duplicate emails (Way overkill, I know, but it was fast and easy to set up.)
- SES to send emails

## Deployment
If you really want to try deploying this project you can do so using

``` sam deploy --guided```

You might need to reconfigure some small things, but sam should tell you how.

Do note that you will need to run the Lambda through a user that has the correct permissions (AmazonDynamoDBFullAccess and AmazonSESFullAccess).

