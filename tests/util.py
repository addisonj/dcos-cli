
import requests

class ServerRequest(object):

    _base_url = "/v2/apps/"
    _headers = { "content-type": "application/json" }

    def _req(self, method, url=None, **kwargs):
        if not "headers" in kwargs:
            kwargs["headers"] = {}
        kwargs["headers"].update(self._headers)

        u = [ self._base_url ]
        if url:
            u += [ url ]
        try:
            return getattr(requests, method)(urlparse.urljoin(
                config.current.url, "/".join(u)), **kwargs).json()
        except ValueError:
            return None
        except requests.exceptions.ConnectionError:
            log.fatal(MISSING_SERVER.format(config.current.host))