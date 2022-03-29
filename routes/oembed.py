import flask

blueprint = flask.Blueprint('oembed', __name__, url_prefix='/oembed')

@blueprint.route("/")
def generator():
    args = flask.request.args

    title = args.get("title", "")
    author_name = args.get("author_name", "")
    author_url = args.get("author_url", "")
    provider_name = args.get("provider_name", "")
    provider_url = args.get("provider_url", "")

    oembed_json = {
        "version": "1.0",
        "type": "rich",
        "title": title,
        "author_name": author_name,
        "author_url": author_url,
        "provider_name": provider_name,
        "provider_url": provider_url
    }

    return flask.jsonify(oembed_json)