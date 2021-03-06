pip install --upgrade 'sentry-sdk[flask]'


function package_deploy {
  cd package
  poetry update
  poetry build
  poetry publish
}


python swallow.py