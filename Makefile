default:

deploy:
	bin/deploy.sh

invoke:
	serverless invoke --stage prod --function webhook_post

logs:
	serverless logs --stage prod --function webhook_post -t

test:
	pytest tests
