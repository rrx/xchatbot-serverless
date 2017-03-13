### Description

This is a simple chatbot that runs on Telegram

### Status
[![Build Status](https://travis-ci.org/rrx/xchatbot-serverless.svg)](https://travis-ci.org/rrx/xchatbot-serverless)


### Install Instructions

Set the environment variable "TELEGRAM_API_KEY" to be your telegram bot token.
Serverless will pick up this variable as part of the deploy process.

```
export TELEGRAM_API_KEY="<token>"
```

Install serverless:

```
npm install -g serverless
```

Setup API Gateway to accept a POST, and then forward to the lambda
function.  Don't forget to "Deploy API"

Update telegram to use the webhook:

```
curl --data "url=${INVOKE_URL}" \
  "https://api.telegram.org/bot${TELEGRAM_API_KEY}/setWebhook"
```

To deploy, run:

```
make deploy
```

Deploy will zip up the dependencies into "vendored/" and then run serverless
to upload to AWS Lambda

To test the lambda function:

```
make invoke
```

To check the lambda logs:

```
make logs
```
