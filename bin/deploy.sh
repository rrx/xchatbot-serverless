#!/bin/bash
set -e
BRANCH=${TRAVIS_BRANCH:-$(git rev-parse --abbrev-ref HEAD)}
if [[ $BRANCH == 'master' ]]; then
  STAGE="prod"
elif [[ $BRANCH == 'develop' ]]; then
  STAGE="dev"
fi
if [ -z ${STAGE+x} ]; then
  echo "Not deploying changes";
  exit 0;
fi

echo "Vendoring Python Requirements"
pip install -q -t vendored -r requirements.txt

echo "Downloading NLTK Libraries"
python -c "import lambda_utils as u;u.setup_nltk_on_lambda()"

echo "Deploying from branch $BRANCH to stage $STAGE"
#npm prune --production  #remove devDependencies
sls deploy --stage $STAGE --region $AWS_REGION
