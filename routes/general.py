import flask


import flask
import urllib.parse

blueprint = flask.Blueprint("general", __name__, url_prefix="/")

@blueprint.route("/")
def index():
    args = flask.request.args

    if len(args) == 0:
        return flask.render_template("index.html")

    title = args.get("title", "")
    description = args.get("description", "")
    url = args.get("url", "")
    colour = args.get("colour", "") or args.get("color", "") or "000000"
    image = args.get("image", None)
    video = args.get("video", None)
    author_name = args.get("author_name", "")
    author_url = args.get("author_url", "")
    provider_name = args.get("provider_name", "")
    provider_url = args.get("provider_url", "")

    oembed_params = {
        "title": title,
        "author_name": author_name,
        "author_url": author_url,
        "provider_name": provider_name,
        "provider_url": provider_url
    }

    domain = flask.request.headers.get("Host")
    protocol = "https" if flask.request.is_secure else "http"
    base_url = "{}://{}".format(protocol, domain)

    oembed_link = base_url + flask.url_for("oembed.generator") + "?" + urllib.parse.urlencode(oembed_params) + ".json"

    return flask.render_template(
        "embed.html",
        embed_title=title,
        embed_description=description,
        embed_url=url,
        embed_colour=colour,
        embed_image=image,
        embed_video=video,
        oembed_link=oembed_link
    )