default:

deploy:
	pip install -t vendored -r requirements.txt
	serverless deploy

invoke:
	serverless invoke --function chatbot

logs:
	serverless logs --function chatbot -t
