import flask
import urllib

from utils import sqlite
from utils import invis_url

blueprint = flask.Blueprint("api", __name__, url_prefix="/api")
database = sqlite.Database()

@blueprint.post("/embed")
def embed():
    body = flask.request.get_json()

    if not body:
        return flask.jsonify({"error": "No JSON body"}), 400

    title = body.get("title", "")
    description = body.get("description", "")
    url = body.get("url", "")
    colour = body.get("colour", "") or body.get("color", "") or "000000"
    image = body.get("image", None)
    video = body.get("video", None)
    author_name = body.get("author_name", "")
    author_url = body.get("author_url", "")
    provider_name = body.get("provider_name", "")
    provider_url = body.get("provider_url", "")

    if colour.startswith("#"):
        colour = colour[1:]

    url_params = urllib.parse.urlencode({
        "title": title,
        "description": description,
        "url": url,
        "colour": colour,
        "image": image,
        "video": video,
        "author_name": author_name,
        "author_url": author_url,
        "provider_name": provider_name,
        "provider_url": provider_url
    })

    # remove empty params
    url_params = "&".join([x for x in url_params.split("&") if x])

    domain = flask.request.headers.get("Host")
    protocol = "https" if flask.request.is_secure else "http"
    base_url = "{}://{}".format(protocol, domain)
    url = base_url + flask.url_for("general.embed_viewer") + "?" + url_params
    invis_url_id = invis_url.generate_invis_url()
    invis_url_ = base_url + "/" + invis_url_id

    database.add(url, invis_url_id)

    return flask.jsonify({"url": url, "invis_url": invis_url_}), 200
