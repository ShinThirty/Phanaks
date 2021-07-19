# Phanaks

## Overview

This is an GIF search web service. It provides the following API:

HTTP GET /search/<search_term> (search_term is a string)

For example, this input:

```
/search/cat
```

will generate the following output

```
{
  "data": [
    {
      "gif_id": "3o6Zt481isNVuQI1l6",
      "url": "https://giphy.com/gifs/cat-smoke-smoking-3o6Zt481isNVuQI1l6"
    },
    {
      "gif_id": "BzyTuYCmvSORqs1ABM",
      "url": "https://giphy.com/gifs/hallmarkecards-cute-hallmark-shoebox-BzyTuYCmvSORqs1ABM"
    },
    {
      "gif_id": "v6aOjy0Qo1fIA",
      "url": "https://giphy.com/gifs/v6aOjy0Qo1fIA"
    },
    {
      "gif_id": "ToMjGppLes0ENI5osCc",
      "url": "https://giphy.com/gifs/cat-hot-fan-ToMjGppLes0ENI5osCc"
    },
    {
      "gif_id": "mlvseq9yvZhba",
      "url": "https://giphy.com/gifs/funny-cat-mlvseq9yvZhba"
    }
  ]
}
```

## Code structure

`flaskr` directory contains the source code of the web server and will be published during the production deployment.
`tests` directory contains unit tests.
`requirements.txt` contains the dependencies used in local development.
`setup.py` defines how the webserver is packaged and published. It also defines the runtime dependencies of the web server.
`setup.cfg` and `MANIFEST.in` defines some common configuration during local development.

## Development and Testing

Go into the directory where `setup.py` file locates and execute the following command to install dependencies. This directory should be your working directory
and the following content will assume that you're in this directory.

```
# Setup virtual environment
python3 -m venv venv
. venv/bin/activate

# Install development dependencies
pip install -r requirements.txt
```

Start the development server

```
export GIPHY_API_KEY=<api_key_to_giphy>
export FLASK_APP=flaskr
flask run
```

The development server will listen on `127.0.0.1:5000`.

You can make code changes and the development server will pick up the changes without restarting.

To execute unit test, run

```
coverage run -m pytest && coverage html
```

Coverage report in HTML format will be in `htmlcov` directory.

## Deployment to Production

When you are ready to publish the changes to production, run the following command to generate the distribution:

```
python setup.py bdist_wheel
```

You can find the distribution file in `dist` directory like following:

```
flaskr-1.0.0-py3-none-any.whl
```

Copy this file to the machine you want to run the web server and execute

```
mkdir <app_name>
cd <app_name>
python3 -m venv venv
. venv/bin/activate
pip install <location to flaskr-1.0.0-py3-none-any.whl>
gunicorn -c 'venv/lib/python3.8/site-packages/flaskr/configuration/gunicorn.conf.py' "flaskr:create_app()"
```

Note that if you are not using `python 3.8` as runtime, you need to change the path to the gunicorn configuration file accoridingly.

If everything goes right, now the web server should be up and listening on `127.0.0.1:8080`.
